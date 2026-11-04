# Estimated Work Queue Wait Time (EWT v2) — how it's computed & why it reads in hours

**Sources:** Sprinklr RCA (prod18 / partner 161147 Sunrise GmbH, work queue `FLB_BackOffice 1st lvl Email`, 2026-09-03) · Confluence CCAAS 4836884858 / 5609029890 / 4644700461 / 4616161458 · Help: [View Estimated Wait Time and Handling Time](https://www.sprinklr.com/help/articles/assignment-engine-use-cases/view-estimated-wait-time-and-handling-time-for-casesmessages/645b65050104980882a5a6e9), [Work Queue Properties](https://www.sprinklr.com/help/articles/setting-up-queues/work-queue-properties/659803058361cf480fd18701), [Estimated wait time in Skill based routing](https://www.sprinklr.com/help/articles/additional-use-cases/estimated-wait-time-in-skill-based-routing/64b006cac834a85bda8c9fa1)

Companion to [[wait-time-queue]] (the two strategies + where the number surfaces). This file is the **internals + debug playbook** for the "wait time is showing hours" complaint.

## What the number actually is
- Not the wait of the case you're looking at. It's a **stored per-bucket historical average** for the queue, read at queue entry and stamped on the work.
- Formula (single exponential smoothing, updated **only when a case is assigned OUT of the queue**):
  `EWT(n) = α × actualWait(n-1) + (1 − α) × EWT(n-1)`
- **α** = work queue's `alpha` field if set, else platform default **0.3** (`WORK_QUEUE_WAIT_TIME_ALPHA`, partner-overridable).
- First case in a bucket returns **−1 / null** (no history).
- **actualWait** = wall-clock `unassignedFromQueue − assignedToQueue` **unless the queue has Business Hours attached** — then only staffed time counts. No Business Hours ⇒ **nights and weekends are counted**.

## The bucket key — the #1 cause of "wrong" values
`PRIORITY:<rank>π<skillId>:<level>…` (skills sorted, π-joined), or `DEFAULT` if neither.
- **Channel is NOT part of the key.** Live chat and email sharing the same skill + priority feed **one** number.
- Stored in Mongo `ae_workQueueTimeStatsV2`, `_id = <workQueueId>π<bucket>`, field `estimatedWorkQueueWaitTime` (ms).
- A single queue can hold dozens of buckets with wildly different values (real case: 34 buckets, 17 min → 63 h, 30 of them > 1 h).

## Where it surfaces (all read the same bucket doc, so they always agree)
- Queue record page / Unified Routing column **"Est. Work Queue Wait Time"**
- **Work Queue Properties API + IVR / bot node** → `WAIT_TIME_IN_MILLIS`, `WAIT_TIME_READABLE`
- Auto-response / welcome-message placeholders `wq_CASE:WAIT_TIME`, `SKILL_WAIT_TIME`
- Rule Engine condition **"Estimated Wait Time (Work Queue Wait Time)"**
- Report `ASSIGNMENT_ENGINE` → dimension **Bucket**, measurement **Estimated Wait Time (V2)**
- **Never** used for assignment. Routing decides on availability / skills / capacity / stickiness only.

### Readable rounding (why exact ≠ displayed)
`WAIT_TIME_READABLE` rounds hard: **≥ 12 h drops minutes, ≥ 1 day drops hours** → 26.6 h renders as **"1 day"**, 63.4 h as **"3 days"**. Use the `_EXACT` / `_IN_MILLIS` variants if you need the real figure.

## ⚠️ The node mixes live state with historical average — read this before announcing

The Work Queue Properties node/API returns fields from **three different systems in one payload**. Only one of them is historical, and it's the one people announce.

| Field (node variable) | Property | Source | Nature |
|---|---|---|---|
| availableAgent | `NUMBER_OF_AGENTS_AVAILABLE` | agent presence | **live** |
| pendingcases | `NUMBER_OF_PENDING_CASES` | queue depth | **live** |
| waitingTime | `WAIT_TIME_READABLE` / `WAIT_TIME_IN_MILLIS` | `ae_workQueueTimeStatsV2` bucket | **historical average** |
| queuePosition | `POSITION_IN_WORK_QUEUE` | live position | **live**, `-1` if case not yet queued |
| — | `IDLE_AGENTS` | available **and** zero capacity consumed | **live** |
| — | `NUMBER_OF_LOGGED_IN_AGENTS` | platform-wide login count | **live** |
| — | `MAX_IDLE_TIME_OF_AGENT` | longest idle among eligible agents | **live** |
| — | `OLDEST_CUSTOMER_WAIT_TIME` | longest current wait in queue | **live** |

**`waitingTime` has no term for available agents and no term for pending cases.** It cannot react to them. This produces the classic complaint:

> `availableAgent: 3` · `pendingcases: 4` · `waitingTime: 8 Hours 25 Minutes` · `queuePosition: -1`

Three agents free, four cases waiting — and the customer is told 8h25m. Working as designed; one overnight case in that bucket is enough (at α 0.3 a single 24 h wait on a bucket at 10 min lands it near 7h15m in **one** update).

### `queuePosition: -1` means the node ran too early
Per the help article, `POSITION_IN_WORK_QUEUE` returns **−1 when the case is not yet in the queue** ("to prevent errors when the property is accessed before case is put inside the queue"). If you see −1, the node fired **before enqueue** — so `waitingTime` is the queue's stored bucket value (DEFAULT/queue-level when no skill was set upstream), not anything about this case. **Move the node after queue entry** or position is unusable in your logic.

### Gate the announcement on live state
```
IF availableAgent > 0 AND pendingcases <= availableAgent
    → "An agent is available now, connecting you…"
ELSE IF waitingTime is credible
    → announce waitingTime
ELSE
    → offer callback / out-of-hours message
```
`IDLE_AGENTS` (available **and** free capacity) is the truest "can answer now" signal — better than `NUMBER_OF_AGENTS_AVAILABLE` alone.

> Note: `WAIT_TIME_READABLE` returns a **default of 1 minute** when the computed wait is under 30 seconds.

## Enablement
- DP `ASSIGNMENT_ENGINE_WAIT_TIME_V2_ENABLED.<partnerId>` = `true` → bucket-based v2 active.
- `acd.enabled.<partnerId>` = `true` → Unified Routing / ACD engine (work queue id is a Mongo ObjectId).

## Debug checklist ("EWT is showing hours")
1. Get the **case's real queue wait** first: `uCW.wkADs.firstWorkQueueDuration` (ms) on the case. Usually seconds — proving the displayed number isn't this case.
2. Identify the **bucket**: case priority (`uCW.pRank`) + required skills (`uCW.aRSC`).
3. Read `ae_workQueueTimeStatsV2` for `_id ^= <workQueueId>` and find that bucket's stored ms.
4. Check the queue doc (`ae_workQueueUserMapping`) for **`businessHoursId`** and **`alpha`**. Absent = wall-clock + α 0.3.
5. Look at the queue's recent history (14 d) — median / p75 / p90 of `firstWorkQueueDuration` per `cType`. If the queue drains a morning backlog, the estimate is *correct* and just reflects that.
6. Confirm which surface the customer read (all match, but rounding differs).

## Fixes, in order of impact
1. **Attach Business Hours to the work queue** — off-hours stops feeding the model. Biggest lever for any back-office queue.
2. **Don't route live chat into an email back-office queue**, or give chat its **own skill/queue** so it gets its own bucket. Channel isn't in the key.
3. **Raise α** on the queue (0.6–0.9) so the estimate tracks current staffing in ~3 assignments instead of ~15.
4. For customer-facing copy, use **`SKILL_WAIT_TIME` / `SKILL_WAIT_TIME_EXACT`** and gate on **`canAssignNewCase` / idle agents** so a chat arriving while agents are free is never told "1 day".
5. Switch strategy to **User Handling Time** (`AHT × position ÷ active agents`) — state-based, doesn't inherit the off-hours backlog.
6. Dev-team **reset** of the queue's `ae_workQueueTimeStatsV2` buckets — cosmetic only; refills after the next backlog unless 1–3 are done.

## Worked example (α = 0.3)
One chat that waited 63 h leaving a bucket sitting at 5 min moves it to `0.3×63h + 0.7×5min ≈ 19 h` **in one update**. Getting it back under 10 min needs **~15 consecutive 30-second exits** at α 0.3 — vs **3** at α 0.9.

## Known drawbacks (per Confluence)
- Refreshes only on assignment → stale while a queue is idle.
- One spike weighs heavily and decays slowly at α 0.3.
- No position-in-queue term.
- No channel separation in the bucket key.
- **Blind to live state** — ignores free agents and queue depth sitting in the same node payload.

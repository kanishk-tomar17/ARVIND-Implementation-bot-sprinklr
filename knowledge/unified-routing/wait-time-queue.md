# Average Wait Time & Number in Queue (Unified Routing 027)
**Source:** Product Foundation Courses → Unified Routing / 027 Average wait time number in queue (video transcript) · **Help:** search `site:sprinklr.com/help unified routing estimated wait time work queue properties position in queue`

## The three queue wait-time metrics (Unified Routing Manager)
- **Estimated work queue wait time** — **predictive**: how long a *new* case will wait before assignment (e.g. 13 sec).
- **Average wait time** — **actual** average wait of *previous* cases (time-filterable via the calendar icon).
- **Oldest customer waiting time** — how long the **first still-pending** case has waited (escalation risk — watch these).

## Use cases
- **Announce** the estimated wait to the customer on queue entry → they choose to wait, request a **callback/appointment**, or hear their **position in queue**.
- **Decide queue vs deflect** to another channel to cut wait in **peak periods**.
- Send **recursive updates** on position/wait so customers stay informed.

## Calculation methods (two)
- **Work queue wait time method** — exponential moving average of previous cases' wait times: `est = α·actual + (1−α)·prev_est` (e.g. α=0.9 → 0.9·10 + 0.1·10.6 ≈ 10.1).
- **Average handle time method** — `AHT × position-in-queue ÷ active agents` (e.g. 4 min × 8 ÷ 8 = 4 min).
- Actual wait can differ from estimate based on real queue conditions.

## Using wait time in the Rule Engine
After assigning a case to a queue, check the current wait time and branch:
- Condition: **applies to Universal Case → Estimated wait time** → a time period (e.g. 100 sec / 5 min). Pick the **estimation strategy** (work wait time vs user handling time). Also condition on **Position in queue** (e.g. > 5/10).
- **Auto-response:** build a **text template in Asset Manager** with **work-queue property placeholders** — wait time (rounded to nearest 5-min window / hours / days), exact ms, position in queue, and **skill-aware** wait time/position. Send via a rule action (**auto-respond / send SMS**, choose account + template). Can run **recursively**.

## Using wait time in IVR / bots
- **IVR — Work Queue Properties node:** select queue + name a variable → exposes **wait time (ms)**, **wait time readable** (play as a prompt, e.g. "2 minutes"), **number of pending cases** (position), **agents available**, **idle agents** (available + free capacity). Use in a decision box / operator-says node (e.g. no agents available → play out-of-business-hours message).
- **Conversational AI bot:** same **Work Queue Properties** node for prompts.
- ⚠️ If a **Set Skill node precedes** the Work Queue Properties node, the properties reflect **only matching-skill** agents/cases (e.g. English agents and English cases).

## Notes / gaps
- Some routing systems, calculation strategies, and placeholders are **DP-controlled** — check the KB or ask support to enable.
- "Idle agents" (available **and** free capacity) is the truest "can answer now" signal — better than "agents available" alone.
- Powers the customer-facing wait/position messaging used in [[../live-chat/customisation]] (dynamic wait time) and IVR/[[../conversational-ai/dialogue-nodes-advanced]] flows.

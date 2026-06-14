# Troubleshooting Assignment Issues (Unified Routing 030)
**Source:** Product Foundation Courses → Unified Routing / 030 Troubleshooting Assignment issues (video transcript) · **Help:** search `site:sprinklr.com/help unified routing assignment failures queue details monitor queue`

## A case is NOT getting assigned — check in order
1. **Is the case actually in the work queue?** Often it's **stuck in rules** (a rule didn't trigger) and never reached the queue. Check: **Work queue → View Details → Messages** (shows pending + in-progress cases); the top **"Customers waiting"** metric also tells you.
2. **Agent availability:** **Queue → Assignees** — are agents **part of the queue**, in **available** status, and **capacity < 100%**? An over-capacity agent never receives a case.
3. **Skills/proficiency** (only for All/Best skill matching): the case may need a skill no available agent has. Open the **pending case → properties → the custom field** where skills/proficiencies are tagged (or a back-end process), then confirm an **available agent with capacity** has those skills.
4. **Assignment Failures tab** — one entry per failed attempt (disabled by default for some partners; **enable via product team**). Reasons listed: **all users unavailable**, **skill/proficiency no match**, or **stickiness timeout** (waiting for the sticky agent).

## An AGENT is NOT getting cases — check
1. **Capacity consumed** (Assignees area). If full, clear what's blocking it — **cases, messages, AND tasks** all consume capacity. View current assignments via an **engagement dashboard** (case/message/task column, filter *assigned to* the agent) and clear them.
2. **Skills/proficiency:** the agent may lack the skill/proficiency the waiting cases require — edit in the **Agent step** (skills & capacity + proficiency).

## Queue Details tabs
- **Overview** (rollup), **Messages** (in-progress = assigned, pending = waiting), **Assignment Failures**, **Assignees** (list, availability filter, consumed capacity, skills/proficiency).

## Reallocate cases to another queue (temporary)
When a supervisor sees a backlog while other queues sit idle: add a **reallocation rule** — set **% of traffic** + **target queue** (e.g. 20% to Voice Connect, +10% to another). Scope by **duration** (end date/time, or "within business hours"). Lives under the queue's **(i) icon**.

## Monitor queue
**Monitor Queue** option → metrics: **customers waiting, abandoned %, SLA %, oldest customer waiting**, agent **status split**, and an agent list (like the **Supervisor Console** agent step; configurable columns).

## Notes / gaps
- The #1 root cause is the case **never reaching the queue** (stuck in rules) — check that *before* debugging routing.
- **Assignment Failures** is the single best diagnostic — enable it per partner.
- Reallocation rules are the supervisor's pressure-release valve for peak-period backlogs; pairs with [[routing-configuration]] backup queues.
- Completes the Unified Routing module: [[routing-types]], [[routing-configuration]], [[capacity-configuration]], [[agent-skills]], [[smart-routing]], [[stickiness-timeout]], [[wait-time-queue]].

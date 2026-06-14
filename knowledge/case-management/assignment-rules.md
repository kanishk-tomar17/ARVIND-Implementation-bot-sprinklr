# Case Management — Assignment Rules (the full assignment process)

**Source:** Product Foundation Courses → `Sprinklr Services - Case Management / 019_… Assignment Rules` (video transcript) · **Cross-check:** `site:sprinklr.com/help assignment engine`

How a case flows from "needs an agent" to "assigned", and the three rules that drive it.

## The end-to-end assignment process
1. A rule decides a case needs assigning → sets status **Awaiting Assignment** and puts the case into **two queues**: the **Pre-Assignment Processing** queue and the **Awaiting Assignment** queue (the latter just tracks current status).
2. **Pre-Assignment Processing rule** runs → tags the relevant **skills / custom fields** on the case, then moves it to the **Assignment Engine Processing** queue.
3. **Add-to-Work-Queue rule** (on the Assignment Engine Processing queue) → adds the case to the right **work queue(s)** based on those tags.
4. Work queues live in **Unified Routing / Assignment Engine** and contain the agents/users. The case is **assigned to an agent** based on availability + the queue's config.
5. On assignment, an **on-demand (Post-Assignment) rule** fires → sets status **Assigned** and moves the case to the **Assigned** queue.

## Rule 1 — Pre-Assignment Processing rule
- A **Case Update rule running on the trigger**; starts with a dummy condition (to let the trigger save) + a check that the case is in the **Pre-Assignment Processing queue** (so it doesn't run on every update).
- **Purpose: tag the deciding custom fields** the assignment will key off, e.g.:
  - **Language** (if agents are split by language).
  - **CSAT trend** — compare predicted vs initial CSAT → tag positive/negative/neutral.
  - **Market**, or any field mapped to an agent **skill**.
  - **Priority** — tag high/low and set the **priority rank** so urgent cases assign first.
- For **email**, optionally send an acknowledgement ("your ticket is going to an agent").
- Ends by removing the case from the Pre-Assignment Processing queue and adding it to the **Assignment Engine Processing** queue (still in Awaiting Assignment).

## Rule 2 — Add to Work Queue rule
- Runs on the **Assignment Engine Processing** queue (on trigger; same dummy + queue-check pattern).
- Reads the tagged custom fields/skills and routes the case into the correct **work queue**.
- **Skill-based vs Queue-based assignment:**
  - **Skill-based** = all agents in **one** work queue; skills assigned to agents; cases matched to agents by skill.
  - **Queue-based** = different agent categories in **different** work queues; cases routed to the queue whose agents have the matching skill.

## Rule 3 — Post-Assignment (on-demand) rule
- Fires when the work queue assigns the case → sets status **Assigned**, moves to the **Assigned** queue.

## Notes / gaps
- From the course video transcript (walked through a blueprint/sandbox environment). Exact conditions vary per client. Priority-rank must be enabled at environment level. Related: `unified-routing/*` (work queues, capacity), `case-management/bot-rule.md`.

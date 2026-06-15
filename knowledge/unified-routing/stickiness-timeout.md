# Stickiness & Timeout Settings (Unified Routing 026)
**Source:** Product Foundation Courses → Unified Routing / 026 Stickiness capacity timeout settings (video transcript) · **Help:** search `site:sprinklr.com/help unified routing stickiness timeout assignee capacity`

## What stickiness is
**Stickiness** routes a **returning case back to the agent who last handled it** — they have the context, so the customer doesn't repeat themselves. Benefits: continuity/personalisation, higher CSAT, efficient agent use. Can also target a configurable **preferred agent**.

## How it works
Customer message → case → work queue → **normal first-time assignment** (skill/priority). Agent handles, then applies a **closing** or **awaiting-response** macro. On follow-up:
- **Within the stickiness timeout** → assigned directly to the **last engaged agent** (can **breach capacity**).
- **After the stickiness timeout** → either **wait** for the agent (stickiness wait timeout) or assign to **any available agent**.
- **Agent logged out** → assign to another available agent immediately.

## Timeout settings (Queue → Assignees tab)
- **Stickiness timeout** — window during which a new message counts as a follow-up and routes to the sticky agent (e.g. **1 day**).
- **Enable assignee capacity timeout** (checkbox):
  - **Unchecked** → within the stickiness timeout, assign to the sticky agent **regardless of capacity** (over-and-above).
  - **Checked** → honour capacity, exposing:
    - **Active conversation timeout** — how long capacity may be **breached** for the returning case (e.g. reopened within 1 hr → ignore capacity; later → check availability/capacity).
    - **Stickiness wait timeout** — if the sticky agent is unavailable/full, how long the case **waits** before general assignment.
- **Availability statuses to wait in** — pick statuses (e.g. lunch, tea break) where the case should still wait for the sticky agent.
- **Consider last case feedback for assignment** — e.g. **60%**: only re-assign to the same agent if the last CSAT exceeds the threshold; otherwise assign elsewhere (avoid a bad-feedback agent).

### Worked example (1 day / 30 min / 15 min)
- Reopened within **30 min** → assigned to the agent regardless of capacity (if available).
- Reopened after 30 min (e.g. 5 hrs, still < 1 day) → if agent available with free capacity, assign; if full, **wait 15 min** then general assignment.
- Reopened after **1 day** → assigned directly to anyone else (no wait, no sticky agent).

## Channel guidance
- **Email:** stickiness timeout ~**7 days**, wait timeout **3–4 hrs**.
- **Voice:** **no** active conversation timeout, **don't** wait for the sticky agent — assign ASAP to the next available agent.

## Stickiness in the Rule Engine
In the **case update rule → assign action**: set **"preferred agent based on user mapping" = yes/no** (= use stickiness). Or use a **custom field storing an agent ID** as the stickiness agent (**"entity to prefer assignee"** = e.g. *last engaged user* custom field). Common pattern: an **"owner"** custom field stores the first agent, used to prefer them on reopen. **"Entity to not prefer assignee"** excludes an agent.

## Notes / gaps
- Capacity-breach vs wait is the core trade-off: breach for fast continuity, wait to protect capacity — tune per channel.
- CSAT-gated stickiness prevents re-routing an unhappy customer back to the same agent — a quality safeguard.
- Stickiness interacts with [[capacity-configuration]] (the breach) and [[routing-configuration]] (what happens after the wait).

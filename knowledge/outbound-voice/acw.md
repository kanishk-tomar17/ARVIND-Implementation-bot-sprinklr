# After Call Work (ACW) (Outbound Voice 171)
**Source:** Product Foundation Courses → Outbound Voice / 171 ACW (video transcript + demo) · **Help:** search `site:sprinklr.com/help after call work ACW disposition plan`

## What it is
**After Call Work (ACW)** captures what a call was about and whether it was resolved — a **snapshot for reporting** plus **workflows** (update CRM, schedule a callback, etc.).

## Key terms
- **ACW** = After Call Work.
- **Disposition plan** — a **repetitive form** used inside an ACW.
- **Dispositions** — fields recording the **primary outcome** of the call (with **sub-dispositions**).
- **Fields** — objects storing agent-input info.

## Disposition plan
Built in the **Disposition Plan Builder** (Voice Care module): configure **dispositions, sub-dispositions, and fields** the agent fills during/after a call. Two parts: **add dispositions** + **add fields**. Field **data types:** text area, date, date-time, number, pick list, text input, multi-pick-list (each field can have **validations**, e.g. date must be DD-MM-YYYY).

## Adding a disposition plan to an ACW
**Sprinklr Service → After Call Work** module → create a new ACW → add a **Screen node** (Nodes dropdown) → add a **Call Disposition** input component (**only one per screen**; a **disposition group** lets you include multiple disposition plans) → select the disposition plan.

## Use cases
Record the interaction for reporting; create workflows (actions based on the interaction); update the brand's database (addresses/phones); add the customer to a **calling list**.

## Example (with scheduled callback)
- Disposition plan: dispositions **First Call Resolution** (sub: Query / Complaint) and **Not First Call Resolution** (sub: Add to CRM / Escalate / Email to customer). Fields: *comments by agent*, *date of callback* (date validation).
- ACW: Screen node + disposition plan + a **loop** (iterate the plan to read the callback date) + a **Schedule a callback** node (number via resource selector, **time for callback = the agent-input date**, assign to a **work queue**).
- Runtime: on call end the **ACW pops up** (timer **configurable**; can also pop **during** the call or for **unconnected** calls) → agent picks **primary outcome** (FCR) + **secondary** (Query) + comments + callback date → **Next** → callback scheduled, agent freed for the next call.

## Notes / gaps
- ACW + disposition plan is what makes outbound calls **reportable** ([[reporting]]) and drives [[post-call-workflow]] / [[retry-strategy]] (business-outcome retries key off dispositions).
- "When the ACW pops up" (before/during/after, connected/unconnected) and its timer are all configurable — set per campaign need.
- The **Schedule a callback** node is the in-ACW path to re-dial (vs the journey-based callback).

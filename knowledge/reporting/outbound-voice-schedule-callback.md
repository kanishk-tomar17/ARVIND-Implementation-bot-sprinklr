# Outbound Voice — Scheduled Callback (Reporting 082)
**Source:** Product Foundation Courses → Reporting / 082 Outbound Voice Use Cases - Schedule Callback (video transcript + Call Back Summary report screenshot) · **Help:** search `site:sprinklr.com/help scheduled callback report task data source voice status`

## What it is
Reporting on **scheduled callbacks** — callbacks created either on **missed calls** or by an **agent per the customer's need**. Shows when callbacks were scheduled, their status, and related details.

## Data source
Use the **Task report** (SPR Task) data source — all metrics/dimensions come from here.

## Key metrics & dimensions
- **Task Count** — number of tasks created. Filter **Task Type = Scheduled Callback** to count callbacks. (Task Type can also be profile/priority/assignment tasks per workflow.)
- **Callback Case** — the parent case + number the callback is associated with.
- **Callback Number** — the customer phone number to call back.
- **Conversation Time** — when the call first came into the system.
- **Callback Triggered By** — user/agent who created the callback.
- **Created Time** — when the callback was scheduled.
- **Callback Assigned User / Assigned To** — agent the task is assigned to.
- **Due Date** — when the task is scheduled/due.
- **Callback SLA** = Due Date − Created Time.
- **Called At** — when the callback was actually made.
- **Call Duration** — length of the callback call.
- **Task Status** — Completed / Pending / Open / Skipped / Cancelled / Expired.
- **Voice Status** — the callback's call status (Call Complete, Agent Missed Offer, Customer Didn't Connect, etc.).

## Standard report + custom metrics
- The standard **Call Back Summary** report plots these as an **extract** (case, created, due, first conversation, callback SLA, assigned to, task count).
- For counts, build custom metrics on **Task Count + Task Type**:
  - **Total Scheduled Callbacks** = Task Count, filter Task Type **containing Scheduled Callback**.
  - **Yet to be Called** = filter **Voice Status containing "Callback Schedule"**.
  - **Completed** = filter **Voice Status containing "Call Complete"**.

## Notes / gaps
- Uses the **Task** data source (distinct from Voice report); callbacks are configured in Inbound/Outbound Voice (disposition → schedule callback). Custom metrics via [[custom-metrics]] + [[filtering]].
- Part of Reporting (Voice/Outbound): [[outbound-voice-overall]], [[outbound-voice-campaign-management]], [[outbound-voice-agent-performance]], [[outbound-voice-ingestion-report]].

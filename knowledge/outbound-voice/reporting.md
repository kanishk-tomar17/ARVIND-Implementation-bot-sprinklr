# Outbound Voice — Reporting (Outbound Voice 174)
**Source:** Product Foundation Courses → Outbound Voice / 174 Reporting (video transcript) · **Help:** search `site:sprinklr.com/help outbound reporting call summary agent summary dashboard` (per-dashboard videos + the reporting blueprint)

## Context
Sprinkler ships **sample dashboards** to monitor day-to-day outbound calling. Outbound call types: **predictive, preview, manual outbound, scheduled callback**. Purposes: telesales/telemarketing, relationship maintenance + cross-sell, and **miscall management** (when agents are busy, auto-schedule callbacks so no customer is lost).

## The standard reports (chronological, ~5–6)
1. **Upload Contacts report** — every outbound centre starts from an **upload file** (customer details + phone). Provided as an **extract**: file name, unique ID, customer name, **phone number** (the number dialed), plus details (e.g. location).
2. **Inventory report** (call report + ingested data) — the upload file **combined with Sprinkler calling data** (how many calls made, was it a **complete call** / customer connected): file name, upload date, lead count, template.
3. **Campaign Management dashboard** — overview of **campaigns + segments** (pacing ratio, churn rate, connectors, calling profile/dialer): per campaign/segment, the **dialer** (predictive/preview) and **number of agents** assigned.
4. **Call Summary report** — every outbound call by **conversation ID**: start time, disconnect time, phone number, time statistics, call properties.
5. **Agent Summary report** — per agent (today/week): calls made, calls **talked to a customer**, time in **login/ready/manual-outbound** states, break time, scheduled callbacks → spot over/under-performers, build **incentive** structures.
6. **Agent Live Monitoring dashboard** — supervisors/leadership see, at a point in time per segment/queue, how many agents are **available / on calls / filling ACW** → workforce management.
7. **Scheduled Callback dashboard** — miscall management: e.g. 50 customers called, 20 unaddressed → 20 callbacks scheduled → how many called today / after 24h / 2 days, with a **Callback SLA** (goal: **reduce callback SLA** — call back ASAP so the lead isn't lost).

## Notes / gaps
- These ~5–6 dashboards (upload → inventory → campaign → call/agent summary → live monitoring → callback) are the **OOTB outbound reporting suite**; the full list + per-metric detail is in the **reporting blueprint** (separate videos per dashboard).
- **Callback SLA** is the headline miscall metric; **agent state times** (ready/manual/break) drive performance/incentives.
- Completes the Outbound Voice module: [[data-ingestion]], [[dialers]], [[campaign-creation]], [[retry-strategy]], [[suppression-list]], [[skill-based-assignment]], [[post-call-workflow]], [[manual-call-controls]], [[acw]], [[agent-desktop]], [[callback]].

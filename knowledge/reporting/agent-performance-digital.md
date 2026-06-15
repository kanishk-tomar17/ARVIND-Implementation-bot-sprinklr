# Agent Performance — Macro, Availability, Occupancy (Reporting 070)
**Source:** Product Foundation Courses → Reporting / 070 Agent Performance - Macro, Agent Availability, Occupancy (video transcript + agent-performance widget builder screenshot) · **Help:** search `site:sprinklr.com/help reporting agent performance time in status occupancy macro`

## What it is
Key KPIs to measure **agent performance** on digital channels, across: **agent hygiene** (status changes, login/logout), **case performance** (assignment, response, handle time, messages), and **macro usage**.

## Status-change (hygiene) widgets
- **Time in Status** (metric) — plot **Agent** + **Date**; filter by **Availability Status**. Records use **Status Assigned Time** / **Status Remove Time** dimensions. ⚠️ A record is created **only when the status is removed**, so a single status spanning days lands entirely on the assign date (e.g. Available 10 AM → removed next day 11 AM = 25 hours on day 1) — can confuse clients.
- **Time Spent in Status** (alternate metric) — avoids that confusion: a record is created **every 30 minutes**, so per-day data never exceeds 24h and rolls into the next day correctly. Choose per use case (build custom metrics if needed).

## Login/logout report
- Metric **Time in Login Status** + **Agent Status Assigned Time** / **Login Status Remove Time**.
- ⚠️ Same metric name appears twice — one is the **measurement (metric)**, one is a **dimension**; use the dimension for plotting times.
- Filter **Login Status = Logged In** → shows login→logout times; **= Logged Out** → logout→login times.

## Case performance widgets
- **Current cases assigned** — metric **Current Assignment** (case count with the agent right now) vs **Agent**.
- **Historical case assignment** — metric **Agent Unique Case Count** (unique cases assigned to a user) vs **Date**.
- **Average assignment duration** — metric **Case User SLA** (time from user assignment to any action — from the SLA report).
- Also: cases replied, **average response time**, messages published, **case handle time**.

## Macro report widgets
- **Case Macro Usage Count** per macro, and **average time to apply a macro** (Case Macro SLA).

## Occupancy / availability
- **Availability Report** — time agents spend in each status (hygiene).
- **Occupancy Report** — time spent in status per hour (occupancy).

## Notes / gaps
- Metrics derive from the records in [[backend-structure-digital]]; built via [[creating-widget]] / [[custom-metrics]]. Live counterpart in [[live-reporting-digital]].
- Part of Reporting (Digital): [[live-reporting-digital]], [[volume-sla]], [[survey-reports]], [[other-modules-reporting]], [[backend-structure-digital]], [[common-metrics-dimensions]].

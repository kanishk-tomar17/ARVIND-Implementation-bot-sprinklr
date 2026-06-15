# Live Reporting — Digital Reports (Reporting 069)
**Source:** Product Foundation Courses → Reporting / 069 Live reporting - Digital reports (video transcript + Agent Monitoring screen screenshot) · **Help:** search `site:sprinklr.com/help live reporting agent monitoring queue monitoring supervisor`

## What it is
Live reporting for digital channels — for **supervisors** to monitor agent availability, queue workload, customer wait time, and case aging in real time (to avoid escalations). Three screens: **Agent Monitoring, Queue Monitoring, Case Queue** use cases.

## Agent Monitoring screen
The supervisor home page → Agent Monitoring. Shows filters + an agent table.
- **Filters:** **Agent Status** (Available / Unavailable / Connection Issue…), **Agent State** (Idle / working a case). E.g. filter Available + Idle to see available-but-idle agents.
- **Key filter fields:** **Login Current Status**, **Agent Current Status**, **User Current Status**, **User Current State** — use these to slice agents by status/state (supervisor can also **change** an agent's current state/status here).
- **Table columns:** Agent name, time idle, **User Current State** (e.g. Idle since 53 min), **Login Current Status** (e.g. logged in 2h 16m), **Time in Current Status**, **Time in Current State**, **Time in Current Login Status**.
- **Manage Columns** — add more columns (e.g. Average Handle Time, Case Processing SLA). ⚠️ Note: handle time / Case Processing SLA are **historical** metrics (not live), driven by the selected time duration — discouraged on a live dashboard; review them in a report instead.

## Queue Monitoring screen
Omni-channel view of all **work queues** on the left, each as a card. Per queue you can show metrics: **SLA, Total Agents Available, Currently Active Cases, Active Agents, Customers Waiting**, etc. — to see current workload vs available agents.

## Case Queue use cases
Monitor the cases agents are working on, including the **oldest aging case** in a queue — to pre-empt client escalations.

## Notes / gaps
- Live counterpart to the historical [[backend-structure-digital]] reports; agent metrics overlap [[agent-performance-digital]]. Voice live reporting in [[live-reporting-voice]].
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[creating-widget]], [[agent-performance-digital]], [[volume-sla]], [[survey-reports]], [[other-modules-reporting]].

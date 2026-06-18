# Agent Monitoring Features (Supervisor Console 043)
**Source:** Product Foundation Courses → Supervisor Console / 043 Agent Monitoring Features (video transcript + Live Agent Monitoring screen screenshot) · **Help:** search `site:sprinklr.com/help supervisor console agent monitoring whisper barge live evaluation`

## What it is
The **Live Agent Monitoring** screen (Supervisor Console 2.0) — real-time visibility into team staffing, what each agent is doing, live cases/calls, and key agent KPIs. Solves a supervisor's pain points: onboarding/training new agents (high attrition), ensuring calls/cases are assigned when agents are productive, and real-time visibility.

## Status vs State
- **Status** is a **superset** of state (Available, Unavailable, Busy, On Leave).
- **State** (within Available) — Idle, on Inbound Call, on Outbound Call, customer-ring/call-ringing, on Hold, or live-chat states (video/audio call initiated via live chat). All monitored live.

## Summary views
- **Agent Status** — counts of Available / Unavailable / Busy / On Leave.
- **Agent State** — Logged Out / Idle / Agent Never Logged In (with counts + %).

## Agent table columns
Agent, **User Current Status** (Available/Unavailable/On Leave/Busy), **Time in Current Status**, **Login Current Status** (Logged In/Out), **Time in Current Login Status**, **Agent Number of Calls Taken**, current assignments / consumed capacity.

## Key actions (per agent)
- **Continuous listen / Whisper / Barge** into live calls — whisper = live guidance to the agent; barge = join the conversation.
- **Take over the call** (e.g. angry customer the agent can't manage).
- **Live on-call case evaluation** — score the agent on call performance.
- **Change agent status** — make Available, set to Break, or **log out** an underperforming agent so others can take over.
- See **live cases** the agent is working (omni-channel: WhatsApp, Facebook, social, voice).

## Filters
Filter agents by **location, skills, manager, availability status**.

## Live UI — VERIFIED (prod8, 2026-06-18)
**Access:** Launchpad → **Supervisor Console** (persona app; URL `/care/supervisor-console/<id>?wTab=team`; the persona is built on the **Workforce Management** app shell).

**Layout = persona dashboards, not fixed screens.** Left rail has **Shared Dashboards** (+ **Settings**). The console's "screens" are **persona-configurable dashboards shared from Reporting** — *this prod8 persona has only the **Agent Monitoring** dashboard enabled* (Queue/Callback/Campaign/Home etc. are separate dashboards that must be added per persona; not present here). **+ Add New Dashboard** adds more.

**Agent Monitoring dashboard — 4 sub-tab views:** **Team Overview** · **Performance Overview** · **Call Analytics** · **Compliance Score**.

**Top controls (Team Overview):**
- **Status quick-filter chips:** **All** (default) · **All Agents** · **Available** · **Busy**.
- **Search** (agent), **date selector** (default **Today**), **timezone** (e.g. Asia/Kolkata).
- **Manage Columns**, **Filter**, **Export**, **Refresh**; per-row + header **checkboxes** (bulk select), **Pagination**.

**Manage Columns = a ~1,235-metric library** (search box; **10 selected** by default; Reset / Cancel / Save). **Default 10 columns:** Agent · User Current Status · Agent Time in Current Status · Login Current Status · Agent Time in Current Login Status · Agent Unique Cases · Agent CCM_Agent_Assigned Cases · Agent Volume of Published Messages · Agent Case Macro Usage Count · Agent Response SLA.

**Per-agent Row Actions (⋮) — verified here:** **Send Message** · **View Activity**. *(Whisper / Barge / Take-over / live on-call evaluation are **voice live-call** actions — they require shared Voice Applications + Unified Assignment permission and surface on a live call, not in this static row menu.)*

**Live status values seen:** User Current Status = **Available / Busy / Unavailable / UnAvailable / Connection Issue**; **Login Current Status** = **Logged In / Logged Out**; each with **time-in-status** (e.g. "10d 4h 43m"). "--" = no data for that metric/agent.

## Notes / gaps
- Omni-channel; voice live-listen requires shared voice applications + Unified Assignment Engine permission (see [[queue-monitoring]]). Overlaps the Reporting live agent monitoring ([[live-reporting-digital]]).
- **Verified-live caveat:** the per-screen feature set depends entirely on which Reporting dashboards are shared into the persona — the rich whisper/barge/queue/callback screens from the course videos are *capabilities*, enabled per persona, not guaranteed present in a given environment (this prod8 had only Agent Monitoring).
- Part of Supervisor Console: [[home-page-features]], [[queue-monitoring]], [[callback-monitoring]], [[campaign-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[best-practices]], [[persona-builder]].

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

## Notes / gaps
- Omni-channel; voice live-listen requires shared voice applications + Unified Assignment Engine permission (see [[queue-monitoring]]). Overlaps the Reporting live agent monitoring ([[live-reporting-digital]]).
- Part of Supervisor Console: [[home-page-features]], [[queue-monitoring]], [[callback-monitoring]], [[campaign-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[best-practices]], [[persona-builder]].

# Queue Monitoring Features (Supervisor Console 044)
**Source:** Product Foundation Courses → Supervisor Console / 044 Queue Monitoring Features (video transcript + Queue Monitoring screen screenshot) · **Help:** search `site:sprinklr.com/help queue monitoring screen supervisor SLA abandon rate skills`

## What it is
The **Queue Monitoring** screen gives a supervisor a **bird's-eye view of all queues** in operation — queue metrics, agent availability/status, agent skills, idle counts. Most features mirror the Agent Monitoring screen ([[agent-monitoring]]); the difference is the **filter**: Agent Monitoring passes a **team** filter; Queue Monitoring passes a **queue** filter.

## Why it matters
Critical for voice service centres (calls land on voice board/IVR → deflect to queue). The supervisor ensures **SLA** is met (cases answered within X time, varies per partner) and **abandon rate** stays low, acting in real time.

## Layout & features
- **Left panel:** all queues, each card showing top metrics (SLA %, Total Calls, Answered, Abandoned, Total Agents, Available Capacity, Cases in Progress, Waiting). Acts as a **filter** — click a queue to load its data; bird's-eye view of others simultaneously.
- **Queue Summary:** Customers Waiting, **Call Abandon %**, SLA %, **Oldest Customer Waiting Time**, Average Wait Time.
- **Agent Status** + **Agent State** for that queue's staffing.
- **Agents table:** Agent, User Current Status, Time in Current Status, User Current State, User Manager, **User Skills (CSV)** — same controls as Agent Monitoring (manage/add columns, export, hide summary, filters, edit/add skills, logout via activity, peer-to-peer chat).
- **Customizable** — time range, add/remove metrics; summary widgets added per client request via **support ticket**.

## Real-time supervisor actions
Make agents available, add more agents to a queue, **change agent skills** (assign a skill where customers wait), send announcements/messages.

## Configuration
- Raise a **support ticket** to customise the queue summary.
- Share all **voice applications** (to live-listen / spy calls).
- Create **quick filters**, map users to a custom field, define **agent skills** (skill-based assignment).
- Grant **Unified Assignment Engine** permission (roles & governance).

## Customer example
HDFC uses Queue Monitoring extensively — supervisors monitor continuously and act on any SLA drop (announcements, messages, skill changes). Every IVR→queue→agent partner monitors the queue.

## Notes / gaps
- Same screen as Reporting [[live-reporting-voice]]; complements [[agent-monitoring]]; actions tie to [[announcement]] and [[peer-to-peer-chat]]. KB article details features + config + roles.
- Part of Supervisor Console: [[home-page-features]], [[agent-monitoring]], [[callback-monitoring]], [[campaign-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[best-practices]], [[persona-builder]].

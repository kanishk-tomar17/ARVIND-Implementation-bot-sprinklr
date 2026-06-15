# Live Reporting — Voice (Queue Monitoring) (Reporting 075)
**Source:** Product Foundation Courses → Reporting / 075 Live Reporting - Voice Report (video transcript + Queue Monitoring screen screenshot) · **Help:** search `site:sprinklr.com/help queue monitoring screen voice SLA abandon rate supervisor`

## What it is
The **Queue Monitoring screen** gives supervisors a **bird's-eye view of all queues** in operation — overall queue metrics, agent availability/status, agent skills, idle counts. Most features mirror the Agent Monitoring screen ([[live-reporting-digital]]); the difference is the **filter passed**: Agent Monitoring passes a **team** filter; Queue Monitoring passes a **queue** filter.

## Why it matters
Crucial for voice service centres: calls land on the voice board/IVR → deflect to a **queue**. The supervisor ensures the **SLA** (cases answered within X time — varies per partner) is met and the **abandon rate** stays low, taking real-time actions.

## Layout & features
- **Left panel:** list of all queues, each card showing top metrics (SLA %, Total Calls, Answered Calls, Abandoned, Total Agents, Available Capacity, Cases in Progress, Waiting). Acts as a **filter** — click a queue to load its data (bird's-eye view of others simultaneously).
- **Queue Summary:** Customers Waiting, **Call Abandon %**, SLA %, **Oldest Customer Waiting Time**, Average Wait Time.
- **Agent Status** (Available, etc.) + **Agent State** (Idle…) for that queue's staffing.
- **Agents table:** Agent, User Current Status, Time in Current Status, User Current State, User Manager, **User Skills (CSV)** — same column/feature set as Agent Monitoring (manage columns, export, hide summary, filters, edit/add skills, logout via activity, peer-to-peer chat).
- **Customizable** — add/remove metrics, set time range; summary widgets added per client request via a **support ticket**.

## Real-time supervisor actions
Make agents available, add more agents to a queue, **change agent skills** (assign a skill where customers are waiting), send announcements/messages.

## Configuration steps
- Raise a **support ticket** to customise the queue summary.
- Ensure all **voice applications** are shared (to live-listen / spy on calls).
- Create **quick filters**, map users to a custom field, define **agent skills** (for skill-based assignment).
- Grant **Unified Assignment Engine** permission (roles & governance) to make the screen work.

## Customer example
HDFC uses Queue Monitoring extensively — supervisors watch it continuously and act on any SLA drop (announcements, messages, skill changes). Every partner handling IVR→queue→agent monitors the queue.

## Notes / gaps
- Voice live counterpart to [[live-reporting-digital]]; uses voice reports from [[voice-backend-structure]]. KB article details all features + config + roles.
- Part of Reporting (Voice): [[voice-backend-structure]], [[inbound-voice-ivr]], [[inbound-voice-agent-performance]], [[inbound-voice-queue-report]].

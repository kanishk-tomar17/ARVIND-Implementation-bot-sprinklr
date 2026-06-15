# Callback Monitoring Features (Supervisor Console 045)
**Source:** Product Foundation Courses → Supervisor Console / 045 Callback Monitoring Features (video transcript + Scheduled Callbacks / Callback Manager screenshot) · **Help:** search `site:sprinklr.com/help callback manager supervisor reschedule no show`

## What it is
The **Callback Manager** lets a supervisor monitor scheduled callbacks — view a summary (scheduled / cancelled / completed), assign/distribute them, and take action.

## Why callbacks matter
A callback is scheduled when a customer is busy / agents are busy, to call back at a suitable time. Benefits: **reduce contact-centre wait time** (schedule a callback when the queue backlog is high), **customer retention** (avoid long holds), and **team productivity** (distribute pending callbacks).

## Callback Manager screen
**Supervisor Console → Callbacks tab.** Shows **Scheduled Callbacks** with: Case Number, Campaign Name, **Callback Assigned To** (agent/work queue), **Previous Connect Time**, **Callback Time**, **Customer Phone Number**. Filter by **Today**, Assignee Type, Campaign, Assigned To.
- **Search** callbacks by phone number.
- **Manual Call** — supervisor connects directly to the customer (becomes part of the callback) — useful for escalated calls.
- **Customer 360 view** (arrow icon) — case history, recordings, transcripts → evaluate what the conversation should be.

## Callback statuses
Expired, Pending, Completed, **No Show** (callback assigned but the agent wasn't available / didn't pick) — tracks agent-level performance. Filter to see how many callbacks are assigned per agent.

## Reschedule (e.g. agent absent)
Search the agent's name → **bulk-select** their callbacks → **Reschedule** → either:
- **Assign to a queue** (group of users — first available agent in the queue gets it), or
- **Assign to a specific agent** (e.g. a backup agent).
- Change the **callback date/time**; add a **note** (reason for rescheduling).
Or **Cancel** the callback if no longer needed.

## Manage Columns & task custom fields
Each callback is a **task** (sub-task of its case). Add **task custom fields** via Manage Columns (e.g. ACW disposition/sub-disposition = call outcome); filter by task custom fields. Standard filter **Campaign** shows campaign-associated calls (e.g. preview-dialer outbound calls without a scheduled callback).

## Notes / gaps
- Ties to the callback flow ([[disposition-plan]], [[acw-builder]]) and outbound campaigns; reporting counterpart in [[outbound-voice-schedule-callback]].
- Part of Supervisor Console: [[home-page-features]], [[agent-monitoring]], [[queue-monitoring]], [[campaign-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[best-practices]], [[persona-builder]].

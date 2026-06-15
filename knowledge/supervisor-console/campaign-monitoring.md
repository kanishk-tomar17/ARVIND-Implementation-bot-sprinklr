# Campaign Monitoring Features (Supervisor Console 046)
**Source:** Product Foundation Courses → Supervisor Console / 046 Campaign Monitoring Features (video transcript + Campaign Monitoring screen screenshot) · **Help:** search `site:sprinklr.com/help campaign monitoring screen supervisor outbound dialer`

## What it is
The **Campaign Monitoring** screen gives a supervisor a **live view of outbound campaign performance**. Campaigns are mostly **sales** (outbound); two dialer types: **Preview** and **Predictive** — automated calling where a work queue + agents are mapped to a dialer; when an agent becomes available they get a call, fill ACW, then auto-receive the next call (more calls = more sales).

## Screen layout
Comes with Supervisor Console; enable via **support ticket**. Same look/feel as Queue Monitoring but with **campaign cards** on the left instead of queue cards.
- **Campaign cards / Voice Campaign Summary** metrics: **Dialed Calls, Connected Calls, Not Connected Calls, Connectivity %** (connected ÷ dialed), **Abandoned %**, **AHT**, **Live Calls**, **In-Flight Calls**.
- **Agent Status** + **Agent State** + agents table (status/state/manager) for the campaign.

## Why / supervisor actions
Gives a clear view of campaign conversion: how much data ingested, calls done/abandoned, leads pending vs staffing. Supervisor can:
- Go to the **segment** → **edit** it / change the data (ingest better data if connectivity is low → more sales).
- **Add more agents** to the campaign if data is huge and agents are few.
- Plus all core monitoring actions (live-listen, edit/add skills, log out via activity, send message, change agent status, manage columns).

## Configuration
Same as agent/queue monitoring (support ticket to enable + customise; voice apps shared; skills + Unified Assignment Engine permission).

## Notes / gaps
- Recently built; Telefonica at full scale, migration planned from the older **Campaign Manager** screen. Reporting counterpart in [[outbound-voice-campaign-management]]; campaign/segment/dialer config in Outbound Voice module. KB article linked in-deck.
- Part of Supervisor Console: [[home-page-features]], [[agent-monitoring]], [[queue-monitoring]], [[callback-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[best-practices]], [[persona-builder]].

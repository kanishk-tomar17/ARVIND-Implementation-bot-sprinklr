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

## Customizable View — columns & sharing (how to add a column for everyone)
Campaign Monitoring does **not** take its columns from a Reporting dashboard — it has its own **Views** system, owned by supervisors/campaign managers (no admin needed). The view dropdown sits **top-left** of the screen (e.g. "Default View ⌄"); the section selector next to the agent table (e.g. "Agent Monitoring / All Agents") picks which sub-view you're editing.

**To add a column and make it visible to other people:**
1. **Options (⋮) → Manage Views → Create View**.
2. Name the view and **specify the users / user groups / workspaces / workspace groups to share it with** → **Save**.
3. In the new view, open **Manage Columns** → add/remove columns or metrics. Columns are split **Active Columns** (toggled on, shown in the table) vs **Inactive Columns**.
4. **⋮ → Update View → Save.** Column changes are **not** persisted otherwise.
5. Users pick the view from the top-left dropdown.

**Scope caveats (important):**
- A view's column set is **per-view, and views are personalized** — editing **Default View** changes it for you only. To reach a whole team you must **create a shared view**.
- Sharing targets **users / user groups / workspaces** — **not personas**. "Everyone on persona X" = share with the **user group** that carries that persona; there is no persona-level column default here.
- Shared views are opt-in on the dropdown, not forced as the landing view.
- The Agent View dashboard can also be pushed via **Share Dashboard** (multiple users or workspaces).

*(Source: help — Customizable View in Campaign Monitoring `campaign-monitoring/customizable-view-in-campaign-monitoring/655478fa65649c53cad9df3e`.)*

## Configuration
Same as agent/queue monitoring (support ticket to enable + customise; voice apps shared; skills + Unified Assignment Engine permission).

## Notes / gaps
- Recently built; Telefonica at full scale, migration planned from the older **Campaign Manager** screen. Reporting counterpart in [[outbound-voice-campaign-management]]; campaign/segment/dialer config in Outbound Voice module. KB article linked in-deck.
- Part of Supervisor Console: [[home-page-features]], [[agent-monitoring]], [[queue-monitoring]], [[callback-monitoring]], [[announcement]], [[peer-to-peer-chat]], [[best-practices]], [[persona-builder]].

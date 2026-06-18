# ACW Builder (Inbound Voice 162)
**Source:** Product Foundation Courses → Inbound Voice / 162 ACW builder (video transcript + demo; "Use cases of an ACW" slide) · **Help:** search `site:sprinklr.com/help after call work ACW builder disposition schedule callback`

## What it is
**After Call Work (ACW)** = post-call work where the brand captures **what the call was about / whether resolved** (a snapshot for reporting) and runs **workflows** (update CRM, schedule a callback, etc.).

## Key terms
- **ACW** — after call work.
- **Disposition plan** — repetitive **form** used inside the ACW (see [[disposition-plan]]).
- **Screen** — the ACW screen the agent sees.
- **Dispositions** — fields recording the **primary outcome**; **fields** store agent-input info.

## Disposition plan recap
Built in the **Disposition Plan builder (Voice Care)**: configure **dispositions, sub-dispositions, and fields**. Field data types: **Text Area, Date, Date-Time, Number, Pick List, Text Input, Multi Pick List**. Example plan: dispositions **First Call Resolution** (sub: Query / Complaint) and **Not First Call Resolution** (sub: Add to CRM / Escalate / Email to customer); fields like "Comments by agent", "Date of callback" (date format DD-MM-YYYY).

## Build an ACW (demo)
- **Sprinklr Service → After Call Work module → Create new ACW.**
- Add a **Screen node** (from the nodes dropdown) → add a **Call Disposition** component → select the **disposition plan**. (Only **one** call-disposition component per screen; **disposition groups** allow multiple disposition plans.)
- **Schedule callback:** add a **loop** to iterate the disposition plan (to read the agent-entered callback date) → a **Schedule Callback node**: **callback number** (hard-coded or from resource selector), **callback time** (= the date the agent input in the ACW), and the **work queue** to assign the callback to.

## Use cases
Record interaction for **reporting**; create **workflows** based on the interaction; **update the brand DB** (addresses, phone numbers); **add the customer to a calling list**.

## Agent experience
After the call ends (via call controls or customer hangs up), the **ACW pops up**. Configurable: the **timer**, and **when** it pops (before/after/during the call, or even for **unconnected** calls). Agent selects primary outcome (e.g. FCR), secondary (e.g. Query), fills fields, sets callback date → **Next** → callback scheduled, agent freed for next call.

## Live builder — VERIFIED (prod8, 2026-06-18)
**Access:** Launchpad → **After Call Work** (Resolve) → **ACW Manager** at `/care/after-call-work/manager`. Sub-nav: **Manager · Disposition Plans · Global Disposition Field Library** (the reusable disposition-field/data-type library). List cols: Process Name · Maximum Time · Maximum Time Unit · Created By/On · Last Modified. Row actions: Edit · Edit Settings · Translations · Clone · Share · Delete · View Reports · View Usages.

**Create New ACW → settings form first:** Name\*, Description, **Type\*** (**Optional ACW · Mandatory ACW · Mandatory ACW with time limit for agent · …with no early exit**), **After Call Work Timeout** + **Agent Status when ACW timeout happens** (for time-limit types), **Auto Wrap Settings** (Auto Wrap Up Time / Same as ACW Timeout), **Advanced Settings** (Allow ACW during call, **Trigger ACW as soon as call starts**, Keep Case Assigned After Call, Show/Timeout ACW for not-connected outbound calls, Disable ACW Redial, Custom Dialer Support in Redialer), **Extension Settings** (Number of Extensions Allowed Per Call, Extension Time). Save → opens the node builder.

**Node builder** (same engine as the IVR builder: canvas + **Add Element** palette + Save / **Save & Deploy**; Manage Resources; Activity). **Palette — 4 categories:**
- **USER COMMUNICATION:** **Screen** (the agent's ACW form screen — host the **Call Disposition** component → pick a disposition plan; one call-disposition per screen, disposition *groups* for multiple), **Transition Screen**.
- **CUSTOMER COMMUNICATION:** Send SMS/Email/Whatsapp · Send Survey · **Schedule Callback** · Reschedule Callback · Cancel Callback.
- **SYSTEM ACTIONS:** Get/Update/Create/Count Records · Decision Box · Add API · Add Note · **Add Loop / Break Loop** · Custom Fields Action · Add or Remove from Queues · Update Properties · Add to suppression list · Call Another Flow · Embed Workflow · Execute Action.
- **FLOW ACTIONS:** Go To Node · End Execution.

Classic schedule-callback ACW = **Screen** (Call Disposition) → **Add Loop** over the disposition fields → **Schedule Callback** (callback number, callback time = agent-entered date, work queue).

## Notes / gaps
- ACW builder hosts the [[disposition-plan]] + schedule-callback flow; ACW pop-up is triggered from [[call-controls]]; callback feeds the dialer/callback. Completes Inbound Voice. Macro: `create_acw` (ledger).
- Part of Inbound Voice: [[telephony-integration]], [[voice-connectivity]], [[custom-fields]], [[ivr]], [[persona]], [[care-console]], [[guided-workflows]], [[call-controls]], [[disposition-plan]].

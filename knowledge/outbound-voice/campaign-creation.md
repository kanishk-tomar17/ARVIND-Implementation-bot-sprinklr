# Voice Campaign Creation (Outbound Voice 166)
**Source:** Product Foundation Courses → Outbound Voice / 166 Voice Campaign Creation (video transcript) · **Help:** search `site:sprinklr.com/help voice campaign manager components segment base filter`

## What a voice campaign is
A **blended tool** to drive outbound-voice business objectives — configure **why / when / how** to call customers, strategising the dialer operation for **maximum outreach + agent efficiency**. The **Voice Campaign Manager** holds all the components below.

## Journey (agent-first / preview example)
Campaign manager configures campaign + settings → **dialer** places outbound calls on customer **segments** → **Unified Routing** assigns to a free agent → agent **previews** customer info and accepts → customer answers → converse (call controls: hold, wait, mute) → agent fills **disposition in ACW**.

## Business use cases
Sales pitch / convert **buying-intent** customers (website intent → segment → call), **awareness drives / offer rollouts** (retention), real-time authentication, telemarketing/sales, collections/debt recovery, customer service (outbound IVR), appointment reminders (healthcare/salon), surveys/market research.

## Components of the Voice Campaign Manager
- **Start/End date + Business Hours** — operational window (e.g. Mar 1–Apr 30, 9–5, excluding weekends/holidays); a **business-holidays list** is configurable.
- **Dialer profile** (the "brain") — how/when the system dials (e.g. predictive + **pacing ratio**); **agent queues** distribute by skill/availability. ([[dialers]])
- **Retry strategy + Dial plan** — how often/when to redial, and the order across a customer's numbers. ([[retry-strategy]])
- **Suppression list** — exclude numbers (opted-out/inappropriate); **upload a file** pre-campaign, or an agent adds a number via an **ACW workflow** when the customer says "don't call me." ([[suppression-list]])
- **Post Call Workflow** — after a call: update records, schedule follow-ups, trigger **SMS/email** (e.g. offer links). ([[post-call-workflow]])
- **Sequential vs simultaneous calling** (= **list/segment weightage**): **sequential** dials segments one after another by priority (segment A in the morning, B in the evening); **simultaneous** runs segments in parallel with **weightages** (e.g. 40/30/30 → per 100 calls, 40 from A, 30 B, 30 C).
- **Skill-based assignment** — assign by skill; either **100%-proficiency only** or **best-skill fallback** when the top agent isn't available. ([[skill-based-assignment]])
- **Maximum + daily attempts** — cap calls per number per day/campaign (prevents over-dialing).
- **Channels** — simultaneous communication paths; split resources (e.g. 100 channels → allow 50 for outbound, reserve 50 for inbound/service).
- **Ringtones** — customise (standard or branded music).
- **Share configuration** — who can view/edit (e.g. restrict Delhi campaigns from Bangalore admins).

## Customer data & segment activation
- **Base filters** — foundational data layer; inclusion criteria (e.g. a geography, or interacted in the last 6 months) → only relevant data enters the campaign.
- **Activate Segment** — granular cuts from base data with different targeting (e.g. recent purchasers) + tailored messaging.
- **Sorting criteria** — order calls by attributes + **lead creation time** (demographics, purchase history, recency) → reach the right people first.
- **Sub-campaigns + calendaring** — group similar segments under a theme/objective (e.g. a product launch) and **schedule** them for specific time slots.

## Notes / gaps
- The campaign is the **orchestration layer**; each component has its own deeper topic (linked above) — this file is the map.
- Segment weightage (simultaneous) vs sequential priority is the key dialing-strategy decision; channels cap protects inbound capacity.
- Base filter → segment → sort → sub-campaign is the data-targeting funnel; built on [[data-ingestion]] leads.

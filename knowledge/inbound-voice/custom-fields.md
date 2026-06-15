# Custom Fields (Inbound Voice 155)
**Source:** Product Foundation Courses → Inbound Voice / 155 Custom fields (video transcript + demo) · **Help:** search `site:sprinklr.com/help custom field voice value source external API`

## What it is
Custom fields capture **additional data** (customer info) — used in **reporting** and shown to the **agent** during a voice call. Significance: capture business-specific data, **enhanced reporting/analysis** (customer behaviour, where agents get stuck in the flow), better data organization.

## Types (same set as Governance [[custom-fields]])
**Single Select List, Multi Select List, Text, Number, Date, Text Area, Text Multi** (comma-separated values).

## Create a custom field (voice context)
**Sprinklr Voice → Route → Enrichment → Custom Fields → Create Custom Field**:
- Pick **type**, enter **name**, choose **asset type(s)** — account / ad / audience / brand / campaign / workspace / **case / profile / task** (in **Voice** the main three are **Task, Case, Profile**). One field can be added to multiple asset types.
- **Values source** (for select lists):
  - **Manual:** define values (e.g. Yes/No) the agent picks from.
  - **System:** values pulled from a source — **Users / Accounts / Workspaces** (e.g. agent selects from users; "all selected" shows all).
  - **External:** define an **API** whose response populates the field values.
- **Visibility control:** show to specific **workspace / users / user group** (default = all workspaces).
- **Advanced visibility filters:** show the field only when **another custom field has a value** (e.g. show only when Social Network = Twitter), or by asset property / layout.
- **Asset-level config:** mark as **mandatory**, include in **filtering**, enable for **contact replacement**, or **auto-fill**.

## Notes / gaps
- Same engine as Governance [[custom-fields]]; this is its voice/enrichment context (Task/Case/Profile), incl. **System** and **External (API)** value sources. IVR system nodes set these fields ([[system-nodes]]).
- Part of Inbound Voice: [[telephony-integration]], [[voice-connectivity]], [[ivr]], [[persona]], [[care-console]], [[guided-workflows]], [[call-controls]], [[disposition-plan]], [[acw-builder]].

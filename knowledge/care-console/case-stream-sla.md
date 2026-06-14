# Care Console — Case Stream: Filters, SLA & Case Inactivity Timers

**Source:** Product Foundation Courses → `Care Console - Case Stream Filters, SLA, Case Inactivity Timers` (video `035_…`, transcript read) · **Cross-check:** `site:sprinklr.com/help case stream`

How agents triage the case stream: filters, SLA/inactivity timers, sorting, and quick indicators.

## Case stream filters
- **Filter icon** in the case stream → filter by **custom fields** and **Select duration** (a few key CFs + duration shown by default; more CFs added on request).
- Common uses: filter by status (assigned / non-assigned), by duration (e.g. last 90 days). Agents see only relevant cases and pick accordingly.

## SLA timers / indicators
- **SLA** = Service Level Agreement; can be defined per **brand** or per **user group**.
- The stream shows **approaching SLAs** and a per-case SLA timer; clicking the indicator filters to cases about to breach so agents fix those first.
- Tied to the agent KPIs:
  - **FRT** = First Response Time (when the agent sends the first response).
  - **CRT** = Case Resolution Time (average time to resolve a case).
- These timers help agents protect FRT/CRT and avoid breaches.

## Case inactivity timer (last-reply timer)
- Runs when the **agent has replied and the customer/fan hasn't responded yet** — shows "you replied last, awaiting customer."
- Lets agents skip cases waiting on the customer and instead work cases where SLA is about to breach.

## Case sorting
- **Sort** option → sort by case due date, custom fields, creation time, case description, engagement score, queue assignment time, etc., **ascending/descending**.

## Quick indicators (shown upfront on the case card)
- At-a-glance flags so agents triage fast: **engagement score** (e.g. 0), **notes added** (e.g. "6 notes" → opens collaboration widget with supervisor notes), **case tags**, **country/brand** (e.g. prioritise Kuwait cases), **replied/not-replied** indicator, **case creation time**, **queue assign time**, and **survey sent/completed** (so agent can close/transfer without picking it up).
- Many are default; additional custom-field values can be enabled via a **support request**, configured per brand/workflow.

## Notes / gaps
- From the course video transcript. Exact default vs request-enabled fields vary per brand. Related: `care-console/overview.md`.

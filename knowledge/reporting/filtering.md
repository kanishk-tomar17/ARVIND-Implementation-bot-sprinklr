# Filtering (Reporting 064)
**Source:** Product Foundation Courses → Reporting / 064 Filtering (video transcript + widget filter condition dropdown screenshot) · **Help:** search `site:sprinklr.com/help reporting dashboard section widget filters priority quick filters`

## What it is
How filters work in reporting dashboards — at three levels, their **priority**, AND/OR behaviour, quick filters, favorites, and user-context filters.

## Three filter levels + priority
1. **Dashboard filters** (top of the dashboard) — apply to the whole dashboard.
2. **Section-level filters** — apply to all widgets in a tab/section (e.g. a section defaulted to Direction = Inbound).
3. **Widget filters** — apply to a single widget (set from inside the widget or from outside).

When all three are applied, the platform enforces a **filter priority** (more specific levels refine the broader ones).

## AND vs OR behaviour
- **Multiple values in the SAME dimension** (e.g. several accounts) → combined with **OR** (any of them).
- **Different dimensions / an additional filter** (e.g. Account + Direction) → combined with **AND** (both must hold).

## Filter conditions
When applying a filter, the operator can be:
- **Containing** — include the selected values.
- **Not Containing** — exclude the selected values.
- **Exists** — show data only if the field exists (e.g. Exists = false on Account → no cases, since every case has an account).

## Quick filters & favorites
- **Quick filters** — create reusable filter shortcuts.
- **Star (favorite) a filter** → it stays applied **by default** every time the dashboard opens.

## Other
- **User-context filters** — scope data by user context.
- A widget can **"Ignore all dashboard/section filters"** (checkbox in advanced options) to stand independent.

## Notes / gaps
- Filters are set in the widget's [[creating-widget]] advanced options and at dashboard/section level ([[dashboard-feature-overview]]).
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[creating-widget]], [[custom-metrics]], [[export-schedule-export]], [[backend-structure-digital]], [[common-metrics-dimensions]].

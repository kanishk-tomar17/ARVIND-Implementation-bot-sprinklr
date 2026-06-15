# Common Errors & Troubleshooting — Voice Report (Reporting 084)
**Source:** Product Foundation Courses → Reporting / 084 Common Errors & Troubleshooting - Voice Report (video transcript + Scheduled Exports + Network-tab config-ID screenshot) · **Help:** search `site:sprinklr.com/help reporting dashboard ID widget ID export config ID troubleshooting`

## What it is
Troubleshooting reporting issues — two parts: (1) **finding configuration IDs** for reporting assets (to give the engineering team when debugging), and (2) common reporting errors + how to debug.

## Finding configuration IDs
- **Dashboard ID** — open the dashboard; the **URL changes** to include the dashboard's unique ID. Pick it directly from the URL (unique per dashboard).
- **Widget ID** — right-click → **Inspect** → **Network** tab → **Clear** existing queries → **refresh the widget** → click the **reporting query** call → **Payload** → expand the request → under the **`additional`** section you'll find the **widget ID** (the **dashboard ID** is also there — matches the URL).
- **Export Config ID (widget)** — Inspect → Network → Clear → widget **⋮ → Export Widget → Export as Excel** (any format) → click the **scheduled call** → **Preview** → the unique ID at the top is the **export ID** (also under the **export types** tab). Unique per export trigger.
- **Export Config ID (dashboard)** — same steps at the **dashboard level** (clear calls, trigger a dashboard export, read the scheduled call's preview ID).
- **Scheduled Exports ID** — from the **Scheduled Exports** list (Settings → Scheduled Exports).
- **Pipeline ID** — also locatable for engineering debugging.

## Why
These IDs (dashboard, widget, export config, scheduled export, pipeline) are what the **engineering team needs** to debug issues — e.g. an export not triggering, or an export file not matching the dashboard layout.

## Common errors (part 2)
The session also walks through the basic reporting problems that come up and how to debug/solutionise them (provide the relevant config IDs + describe the discrepancy).

## Notes / gaps
- Closes the Reporting module. Applies across digital + voice dashboards built in [[creating-widget]] / [[export-schedule-export]]. When stuck, capture the config IDs above and raise a ticket per the GROOT escalation path.
- Part of Reporting: ties to [[export-schedule-export]], [[organising-creating-dashboards]], and all voice/digital report files.

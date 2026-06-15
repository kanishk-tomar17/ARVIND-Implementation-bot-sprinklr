# Export & Schedule Export (Reporting 066)
**Source:** Product Foundation Courses → Reporting / 066 Export & Schedule Export (video transcript + Export Dashboard config screenshot) · **Help:** search `site:sprinklr.com/help reporting export schedule export external storage S3 SFTP`

## Four ways to export
1. **On-demand export** — export a widget or dashboard now in a chosen format.
2. **Schedule export to email** — receive the data dump by email on a schedule.
3. **Schedule export to external storage** — **S3 bucket, SFTP, FTP** (standard for data dumps).
4. **Reporting APIs** — client pulls data programmatically.

## Supported formats
**JSON** (API + external storage only — NOT on-demand), **CSV, Excel, PDF, PNG** (+ PPT/HTML for dashboard export).

## On-demand export
- On a dashboard/widget → **Export**. Choose a **tab** (or a single widget), pick the **format** (e.g. Excel).
- For a tab with multiple widgets: choose **each widget as a separate sheet** or **all widgets in a single sheet**.
- **Export** → a **notification** appears; click it to download.

## Export Dashboard config (screen)
- **Dashboard** + **Date Range**.
- **Filters** — apply dashboard filters or a new set.
- **Sections to export** — e.g. Inbound Case Level Dump, Conversation Dump, Case Journey Extract, Message Dump, Status & Login/Logout Dump, Agent Assignment Dump, Queue Dump (Select All option).
- **Export Type** — PDF, Excel, PNG, PPT, HTML, CSV, JSON.
- **PDF Layout** (Portrait/…), **Number of PDFs** (e.g. one PDF per tab), **Email Embed Format**.
- **Format options** — Show Filters, Show Annotations, Show Metrics Definition, Skip Empty Exports; **Widget View** = Default View (data points on Y) or Expanded View (all data points).
- **Export Cover Page** toggle (with brand logo).

## Schedule export to email
- From **Export** → **Advanced and Schedule Export Setting**: select date range, tab, format, single-vs-separate sheets.
- **Frequency** — every 30 min, hourly, daily at a set time (hour:minute), etc.
- **Recipients** — Sprinklr users or external email addresses; set subject, etc. → Export (scheduled).
- **Manage:** Settings → **Schedule Exports** lists all scheduled exports with their times; switch off or edit any.

## Schedule export to external storage
- In the schedule, choose **External Storage** → **Add New Storage Destination** → select **FTP / SFTP / S3** and enter the details (work with the client's IT/Ops to set up).
- Once added, specify the **path**; files land in the configured folder (a subfolder is created per extract name, e.g. "Standard Social Extract").

## Notes / gaps
- Exports a dashboard built per [[organising-creating-dashboards]] / [[creating-widget]] with [[filtering]] applied. Standard raw-extract dashboards feed the backend structure ([[backend-structure-digital]]).
- Part of Reporting (Digital): [[organising-creating-dashboards]], [[dashboard-feature-overview]], [[creating-widget]], [[filtering]], [[custom-metrics]], [[backend-structure-digital]], [[common-metrics-dimensions]].

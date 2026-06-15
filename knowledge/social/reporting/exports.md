# Scheduled Exports & Data Export (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- Lets you download Reporting dashboards or widgets in multiple formats (PDF, Excel, PNG, PPT, CSV) — as a one-time download or on an automated schedule with email delivery.
- Schedules can run immediately, by minute, hourly, daily (with or without weekends), weekly, or monthly, and can deliver to Sprinklr users/groups or external email addresses.
- Exports can be stored externally (FTP, SFTP, S3, GCP) instead of, or in addition to, email.
- Dashboards can also be shared read-only outside Sprinklr via an External Shareable Link.
- An Audit Trail tracks every change and run on scheduled exports for accountability.
- See related: [[reporting]], [[engagement-dashboards]], [[data-engine]].

## Key features & how to use

### Data export capabilities (what supports export)
- Documents which modules across the platform support export, marked Yes/No per feature.
- Social Core: engagement dashboards, reporting, asset management, editorial calendars, rule engine selections, audience profiles, reporting overviews.
- Marketing: editorial calendars, asset management dashboards, audience profiles, segment managers, custom metrics, CXM settings.
- Advertising: ads reporting dashboards, custom metrics, ads benchmarking, scheduled exports, segment managers, ads campaigns, product catalogs.
- Research: listening dashboards, topics, themes, business locations, benchmarking.
- Care: agent console column exports, supervisor console user activity reports.

### Export options in Social Reporting
- Formats: PDF, Excel, PNG, PPT, CSV.
- Open: New Tab icon > Reporting (under Analyze) > pick a custom dashboard > Options icon (top right) > Export.
- Choose **Sectional Export** or **Advanced Export**.
- Sectional Export steps: select Dashboard Sections to Export > choose Export Type > Export.
  - PDF: Portrait/Landscape; one or multiple PDFs.
  - EXCEL: widgets separated or combined; **limit of 100,000 rows**.
  - Also PNG, PPT, CSV.
- Advanced Export: click "View Advance & Scheduled Export Settings", configure, then Export.
- Advanced Export fields:
  - Dashboard Details: Dashboard name, Date Range, "Exclude today's data" toggle.
  - Filters: apply existing dashboard filters or new filters.
  - How to Export: Add cover page image, Export Cover toggle, Export Type, Export Name, Widget View (Default View / Expanded View), Storage (Default, FTP/SFTP, or S3).
  - What to Export: Amount of Data; Data Labels (As on Dashboard / Hide for All Widgets / Show for All Widgets).
  - When to Export (schedule): Tags; Schedule (Download Immediately, Minutes, Hourly, Daily, Daily exclude weekend, Weekly, Monthly); Add End Date; Recipients (Sprinklr users/groups or external email); "Send me a copy of export" toggle; Subject, Sender, Reply to; Email Footer Note; "Contextual Data" toggle; "Scheduling Status" toggle.
- To set up a schedule via Settings: Reporting > Options icon > Scheduled Exports > "Add Scheduled Export" > fill "When to Export" > Export.
- Manage existing scheduled exports: Edit, Clone, Trigger (run immediately), Delete, Status toggle (enable/disable).

### Daily scheduled reports excluding weekends
- New Tab > Reporting (under Analyze) > Dashboard Menu icon (top left) > "Scheduled Exports" under Settings.
- Click "Add Scheduled Export" (top right).
- In "When to Export (schedule)", set the Schedule dropdown to **Daily** or **Daily (Exclude Weekend)**.

### Include definitions in reporting exports
- Adds an extra column of metric definitions to the exported Excel sheet.
- New Tab > Reporting (under Analyze) > hamburger menu > "Scheduled Exports" under Settings.
- Complete the required fields and check the **Include Metric Definitions** checkbox.

### Store exports in a non-Sprinklr environment (FTP/SFTP/S3/GCP)
- In Advanced & Scheduled Export Settings, two storage options:
  - **Default** — sends export by email (checked by default).
  - **External Storage** — transfers/stores exports on FTP, SFTP, S3, and/or GCP.
- Selecting both sends by email AND to external storage. Once set, exports save automatically with no manual intervention.
- You can edit an existing FTP/SFTP external storage config; custom SFTP folders can be created and connected.
- Set up an external source: New Tab > Governance Console > All Settings (within Listen) > search "External Sources" in Platform Settings > "Add External Source" > select storage type (FTP/SFTP/S3/GCP) > complete fields > Save.

### Export dashboard mapping (for BI tools)
- Exports a field-mapping file (CSV or Excel) listing dimensions/fields for API calls, used to recreate widgets in BI tools like Tableau or Google Data Studio.
- Capability is a Dynamic Property — must be enabled via your Success Manager / a support request.
- Grant permission: New Tab > Governance Console > All Settings (Platform Setup) > Workspace Roles or Global Roles > Create Role > add the **"Export Dashboard Metadata"** permission > Save.
- Run it: Reporting > open dashboard > Options icon (top right) > "Export Dashboard Mapping" > you get notification "Dashboard metadata exported successfully" > Notifications icon > download the file.
- Output CSV fields: Display Name, Field Name, Field Type, Report Name, Report Engine, Report Engine Display Name, Description, Filters used. Multi-tab dashboards produce separate sheet tabs per widget set.

### External shareable link (share dashboards read-only outside Sprinklr)
- Supports: widget tabs, Quick Filters, target metrics on widgets, section-level date ranges.
- Requires the **External Share** permission.
- Available for any reporting dashboard: Listening, Benchmarking, Reporting, Advocacy Reporting, Ads Reporting, Care Reporting.
- Steps: New Tab > pick Reporting/Insights capability > open dashboard > Options icon > "Get External Link" > set Date Range > set Expiry Date (default 7 days) > optionally check "Hide PII Data" > "Auto Sync" > "Password Protection" (+password) > "Rolling Time Range" > "Generate URL" > copy link.
- Auto Sync: dashboard changes synchronize to the external link; if off, use "Sync Now" for manual updates.
- Link auto-enables on generation; revoke by sliding the "Link Sharing" toggle left.
- Dashboard Manager columns: "External Sharing Status" (Active/Inactive) and "External Link Share Expiry" (expiry date).
- Usage reporting (data source: Audience Activity): Dashboard Module, Activity Count (total clicks), Unique Activity Count (clicks across different browsers), Dashboard Name, External Dashboard Link.

### Scheduled exports audit activity
- Audit Trail logs every key change/run on scheduled export configs, showing old and new values.
- Logged events: PII Data Hidden/Unhidden, Export File Name Format Changed, Storage Options Changed, Widget View Changed, Export Format Changed, Export Name Changed, Export Type Changed, Image Changed, Data Labels Settings Changed, Export Settings Edited, Scheduled Time Changed, Recipient User Added/Removed, Email Configurations Changed (sender, reply-to, subject, email copy, custom text, footer), Automated Export Triggered (with success/failure status).
- Controls: Refresh (update log), Sort (by time), Filter ("Run History" or "All Logs").

## Common issues & fixes
- **Not receiving export by email or platform notification:** In Notifications > Scheduled Exports, Email and Platform notifications must each be enabled to receive those respective deliveries. For other users, check Platform Settings > Users > "Notification Preferences" tab. Persistent in-platform issues: contact tickets@sprinklr.com.
- **Email blocked as spoofing:** If the Sender field holds an email internal to your org, security may block it (export sends from user1@alerts.sprinklr.com). Fix: change/remove the Sender entry — it can be plain text like "Sprinklr Reporting".
- **Whitelist domains** with IT: sprinklr.com, alerts.sprinklr.com, amazonses.com, email.sendgrid.com, sendgrid.net.
- **Export failing (scheduled or one-time):**
  - A widget not loading can fail the export — edit and save the failing widget(s).
  - If a dashboard shows a "Switch to Sections" button, it isn't in sections; click it, confirm sections, save.
- **Scheduled export failing (owner-related):** Exports run using the owner's access.
  - Owner inactive → export fails and deactivates. Fix: clone the export to become the new owner.
  - Owner not logged in recently → password may be expired (check last login in Platform Settings > Users). Fix: clone or ask owner to log in.
  - Owner lost dashboard access → export fails. Fix: restore access or clone the export.

## Notes & gaps
- **Permissions/prerequisites:** External Shareable Link needs the "External Share" permission; Export Dashboard Mapping needs the "Export Dashboard Metadata" permission AND is a Dynamic Property enabled only via Success Manager/support request.
- **Limits:** Excel export capped at 100,000 rows; external shareable link defaults to 7-day expiry and refreshes every 15 minutes until expiry.
- **External shareable link limitations:** Desktop web browsers only; view-only (no editing); not supported on Internet Explorer; filters not supported for Standard Dashboards; not supported when the dashboard owner is inactive.
- **Owner dependency:** Scheduled exports always render using the owner's credentials and data access — keep owners active and logged in.
- Gaps: the source articles do not specify exact file-size limits for FTP/SFTP/S3/GCP transfers, retry behavior on failed scheduled runs, or the full Yes/No matrix per individual feature in the data-export-capabilities table (it lists ~120+ features but the per-feature status was not enumerated here).
- See related: [[rule-engine]], [[sla-monitoring]], [[care-console]], [[data-engine]].

## Sources
- Data Export Capabilities — https://www.sprinklr.com/help/articles/scheduled-exports/data-export-capabilities/6454dded0d27fc559bbeb525
- Export Options in Social Reporting — https://www.sprinklr.com/help/articles/scheduled-exports/export-options-in-social-reporting/6454dc5ef65d86626c82b999
- External Shareable Link — https://www.sprinklr.com/help/articles/scheduled-exports/external-shareable-link/6454d9ecf65d86626c82b98b
- Daily Scheduled Reports Excluding Weekends — https://www.sprinklr.com/help/articles/scheduled-exports/daily-scheduled-reports-excluding-weekends/6454d96e0d27fc559bbeb512
- Include Definitions in Reporting Exports — https://www.sprinklr.com/help/articles/scheduled-exports/include-definitions-in-reporting-exports/6454ef28f65d86626c82b9d0
- Store Sprinklr Scheduled Exports in a Non-Sprinklr Environment (FTP/SFTP/S3/GCP) — https://www.sprinklr.com/help/articles/scheduled-exports/store-sprinklr-scheduled-exports-in-a-nonsprinklr-environment-ftpsftps3gcp/65036bad503ed17eb5c4d7af
- Export Dashboard Mapping Option in Reporting — https://www.sprinklr.com/help/articles/scheduled-exports/export-dashboard-mapping-option-in-reporting/6454dac70d27fc559bbeb516
- Scheduled Exports Audit Activity — https://www.sprinklr.com/help/articles/scheduled-exports/scheduled-exports-audit-activity/674998ed64bece084358872f
- Troubleshoot Export Problems — https://www.sprinklr.com/help/articles/scheduled-exports/troubleshoot-export-problems/6454d895f65d86626c82b987

# Getting Started with Reporting Dashboards (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- Reporting Insights centralizes data from all your social channels and accounts so you can customize, expand, and drill into metrics by building dashboards and widgets.
- Access: New Tab icon > Sprinklr Social tab > Reporting (within Analyze).
- Reporting Home is the hub to view and manage all Reporting Dashboards and Folders in Sprinklr.
- Two main building blocks: dashboards (the containers) and widgets (individual charts/metrics inside them).
- Most behavior is governed by roles and permissions under Reporting > Dashboards and Reporting > Settings. See [[reporting]] and [[engagement-dashboards]].

## Key features & how to use

### Reporting Home — overview & navigation
- Open via New Tab icon > Sprinklr Social > Reporting (within Analyze).
- From any dashboard, jump back via Home in the "Show Dashboards" dropdown.
- Visibility: switch between list or grid view; organize dashboards by tags, owner, or type.
- Bulk actions: select multiple dashboards with checkboxes to share, delete, or manage tags together.
- Export: use the horizontal ellipsis (…) menu to export the home page view.
- Filtering: click Add Filter to narrow results and find a specific dashboard.

### Create a Reporting Dashboard
1. New Tab icon > Sprinklr Social > Reporting (within Analyze).
2. Click the Create Dashboard icon (top-right corner).
3. In the Create Dashboard pop-up, enter:
   - Name for the dashboard.
   - Starter Dashboard Type (from the drop-down).
   - Tags (as needed).
4. Click Save (bottom-right) to create it.

### Manage Reporting Dashboards
All actions below start by hovering over the dashboard's Options icon.
- **Edit name & tags:** Options > Edit, make changes, click Update.
- **Share:** Options > Share, set Visibility, click Share.
  - Workspace(s) = visible to all users in those workspaces. User(s)/User Group(s) = visible only to those specified.
  - Dashboards shared with you appear in the Shared Dashboard section.
- **Lock:** Options > Lock. A Lock icon appears to the right of the dashboard name. Once locked, the only allowed actions are share, clone, or unlock.
- **Clone:** Options > Clone, enter a Name, click Clone. Note: cloning embeds the channel-specific filter in the backend, so the new dashboard reports exclusively on that channel.
- **Extend:** Options > Extend, name the child dashboard, click Extend. Creates a Child Dashboard linked to a Parent. Child dashboards have no edit access — you can only apply dashboard filters on them without changing the parent's filters; editing the parent edits all children. Contact your Success Manager to enable.
- **Delete:** Options > Delete, then confirm Delete (permanent).
- **Export:** Options > Export. Choose Sectional Export (one-time) or Advanced Export (scheduled). Pick File Format and Sections, click Export. You're notified (top-right) when processing completes. Files export in their original extensions (PDF, Excel, CSV, PNG) rather than a ZIP, for security/confidentiality.

### Reporting Dashboard Manager (manage all dashboards in one place)
- Permission required: enable the "Dashboard Manager View" permission on a role (Platform Setup via Governance Console, under the Conversations tab settings).
- Location: within Sprinklr Social settings; lists all dashboards with metadata — topics, folders, tags, ownership, and external sharing status.
- Actions: create, edit, clone (with custom name), share (configurable visibility/permission), delete (permanent), and export the manager data to Excel.
- Organization: search by dashboard name or tags; group by type, owner, or tags; filter; and auto-refresh at a configurable interval.
- External sharing tracking columns: "External Sharing Status" (Active/Inactive) and "External Link Share Expiry" (expiration date).
- Dashboard creation fields here: Name, folder, starter template, tags, and auto-refresh settings.

### How to find metrics within Reporting
- **Step 1 — Identify the data source:**
  - Social Analytics — for data on posts published by the brand.
  - Inbound Analytics — for data on comments, messages, or reviews.
- **Step 2 — Check the Glossary:**
  - Channel-specific metrics (Facebook, Instagram, Twitter/X, LinkedIn, etc.) — use the Reporting Glossary for that channel (also accessible directly on the channel).
  - For Inbound Analytics, refer to the glossary in the help articles.
- Purpose: narrow the search and choose metrics relevant and accurate for the dashboard's audience; understand the underlying data before plotting.

### Filters in Reporting Dashboard
- **Widget-level filters:** apply only to an individual widget; available on **custom dashboards only** — standard reporting dashboards cannot be filtered at the widget level.
  - Open the dashboard (or create one) > create the widget > widget Options icon > Edit Widget.
  - In Edit Widget, set filters in the Filters section: pick dimension, filter type, and values.
  - The same filter can be applied via the Funnel icon outside the widget. Add time-based metric/dimension filters for time-based values.
- **Dashboard-level filters:**
  1. Click the Filter icon (top-right).
  2. Click "Select Quick Filter" for an existing filter, or "Add Filter" for new parameters.
  3. The panel shows total values selected out of all filter values.
  4. Click "Apply Filter" (bottom-right).
  5. Click Save in the filter panel to save it as a Quick Filter.
- **Date range & timezone:** apply date range via the Duration Picker (top of dashboard); choose predefined or custom range — only data in range is shown. Timezone options: Sprinklr Timezone, Account Timezone, Geographic Timezone.
- Also supports multi-keyword filtering with Boolean operators (AND, OR, NOT), custom aggregation definitions, comma-separated multi-select values, and multi-level widget sorting.

### Quick Filter in Locked Mode
- Quick Filters personalize dashboard data without changing the underlying structure; this is a user-governed entity enabled via roles and permissions.
- **Permission required:** "Quick Filter in Locked Dashboard" under Reporting > Dashboards (to view Quick Filters in lock mode).
- **Lock a dashboard:** Reporting (under Analyze in Sprinklr Social) > search and open the dashboard > More Options icon > Lock.
- **On a locked dashboard:** locked filters cannot be overridden by Quick Filters. View users can apply shared or self-created Quick Filters; even Edit-access users cannot modify Quick Filters while locked.
- **On an unlocked dashboard:** any Quick Filter can be overridden/edited by View or Edit users.
- **View-permission behavior:** can only select shared or self-created Quick Filters; cannot add, edit, rename, delete, or share them. Applied Quick Filters become locked (individual filters can't be modified); removing the applied Quick Filter returns the dashboard to its default locked state.
- **Quick Filter vs. Locked Filter interaction:**
  - Partial application — compatible parts apply, incompatible parts are ignored (e.g., if Social Network = YouTube is locked and the QF has Instagram/Facebook, only the non-network parts apply).
  - Fully incompatible — notification: "This Quick Filter cannot be applied with the current locked filter values on the dashboard."
- Best practices: avoid applying/starring filters when locking; proactively share Quick Filters with View users; confirm dashboards are shared with View users; restrict View users to locked dashboards.

### Custom Metrics Governance
- Lets you control who can use a custom metric across workspaces and users.
1. New Tab icon > Sprinklr Social > Reporting (within Analyze).
2. Open Custom Metrics: Reporting Home > Settings icon (top-right) > "Custom Metrics". (On a dashboard: Options icon > Settings > "Custom Metrics".)
3. Hover the Options icon next to the metric > "Governance".
4. Either check "Share with everyone" (all workspaces and/or users/user groups), OR provide specific "Workspace(s) to share with" and "User / User groups".
5. Click "Share" (bottom-right).
- **Prerequisite:** enable the DP flag `CUSTOM_MEASUREMENT_REPORT_GOVERNANCE_ENABLED` (contact your Success Manager). See [[data-engine]].

### Reporting Roles & Permissions
- Configured under Reporting > Dashboards and Reporting > Settings; modifiable per user role/responsibility.
- **Dashboard permissions:** View, Create, Edit, Delete, Export, Share (across workspaces), User Sharing (with users/user groups), Clone, Lock (lock/unlock).
- **Widget permissions:** Create, Edit, Delete, Export, Clone, Lock; plus Change Widget Chart (change visualization) and Lock SLA Preset.
- **Specialized dashboard permissions:** SLA Dashboard, Campaigns Dashboards, SED Dashboards, Inbound Tag Dashboard, Profile Overview; and Enable Drilldown (drill into data points). See [[sla-monitoring]].
- **Settings permissions:** Custom Metrics, Scheduled Reports, Annotations, Data Sources, Target Metrics, Dashboard Manager View; plus Explore permissions (Create, View, Edit, Delete).

### Deactivation notification & re-add permission
- Reporting dashboard users see a notification bar at the top highlighting recently deactivated accounts, so engagement opportunities aren't missed.
- **Grant the permission:**
  1. New Tab icon > Platform Modules > All Settings (within Listen).
  2. Platform Settings > Workspace Roles or Global Roles.
  3. Click Create Role.
  4. In Create New Role, set a Name (e.g., Marketing Team, Customer Care Team), optional Description, assign Users/User Groups, and under Role Permissions search and select "Account Notify Admin Bar View".
  5. Click Save.
- **Notification bar actions:** "Re-Add the accounts" via the accounts settings window, or "Notify Admin" via email and UI push notification. See [[care-console]].

## Common issues & fixes
- **Quick Filter won't apply on a locked dashboard:** locked filters take precedence and can't be overridden; if fully incompatible you'll see "This Quick Filter cannot be applied with the current locked filter values on the dashboard." Only compatible parts apply.
- **Can't filter a widget individually:** widget-level filters work on custom dashboards only — standard reporting dashboards have no widget-level filtering.
- **Custom Metrics Governance option missing:** the `CUSTOM_MEASUREMENT_REPORT_GOVERNANCE_ENABLED` DP flag must be enabled (via Success Manager).
- **Can't edit an extended (child) dashboard:** by design — children have no edit access; edit the parent instead (which propagates to all children).
- **Dashboard Manager not visible:** the role needs the "Dashboard Manager View" permission.

## Notes & gaps
- Several features are gated and require enabling by your Success Manager: Extend (parent/child dashboards) and Custom Metrics Governance (DP flag).
- Key permissions to pre-check: "Quick Filter in Locked Dashboard", "Dashboard Manager View", "Account Notify Admin Bar View", and the relevant Reporting > Dashboards / Settings permissions.
- The articles do not specify hard numeric limits (e.g., max dashboards, widgets, export size, auto-refresh interval values, or link-share expiry durations).
- Exact starter dashboard types and the full Custom Metrics build flow are not detailed in these articles — only the governance/sharing step is covered.
- Glossary metric definitions are referenced but not enumerated here; consult the per-channel Reporting Glossary.

## Sources
- Reporting Home - Overview & Navigation — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/reporting-home-overview-navigation/649c26c4564e3e25f803f248
- Create a Reporting Dashboard — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/create-a-reporting-dashboard/6453425c0d27fc559bbe8851
- Manage Reporting Dashboards — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/manage-reporting-dashboards/64534e5ff65d86626c828f3f
- Reporting Dashboard Manager to Manage All Your Dashboards — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/reporting-dashboard-manager-to-manage-all-your-dashboards/669df3fa5b7503688d20aa1f
- How to Find Metrics within Reporting — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/how-to-find-metrics-within-reporting/645b96080104980882a5a748
- Filters in Reporting Dashboard — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/filters-in-reporting-dashboard/6569dde444f32b4163d576d5
- Quick Filter in Locked Mode — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/quick-filter-in-locked-mode/67ef6ad379ba2163f6c06862
- Custom Metrics Governance in Reporting Dashboard — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/custom-metrics-governance-in-reporting-dashboard/650335cc923c104940d18429
- Reporting Roles & Permissions — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/reporting-roles-permissions/649c25d5564e3e25f803f247
- Permission to Deactivation and Re-Add Notification in Reporting Dashboard — https://www.sprinklr.com/help/articles/getting-started-with-reporting-dashboard/permission-to-deactivation-and-readd-notification-in-reporting-dashboard/6502ba43923c104940d17d71

# Engagement Dashboards & Columns (Sprinklr Social — Engagement)
**Source:** sprinklr.com/help — Engagement sub-area (multiple articles; see links below)

## What it is
- Engagement Dashboards manage a team's response workflows from organized, customizable dashboards inside Sprinklr Social > Engage.
- Each dashboard holds configurable columns that surface relevant inbound, outbound, workflow, or channel-specific messages for quick action.
- In a column you can view, act on, assign, engage with, and bulk-action messages, then export, search, and resolve them.
- The third pane (message/profile detail panel) gives a single-location snapshot of message + profile + conversation, plus quick actions.
- The Community Management Persona App rolls engagement and reporting dashboards into one focused workspace. See [[engagement-dashboards]], [[care-console]].

## Key features & how to use

### What you can do with Engagement Dashboards
- Build personalized channel dashboards with columns configured to show relevant content.
- View, act on, engage with, and assign messages within columns.
- Export column contents to an Excel spreadsheet.
- Search within a column by keyword, user, or message tag.
- Run bulk actions on multiple messages across multiple columns.
- Use third-pane actions to see message and profile information in one place.
- Choose from multiple workflow configuration options.

### Create an Engagement Dashboard
- Open New Tab icon > Sprinklr Social > Engagement Dashboards (within Engage). The list shows all previously created dashboards.
- Click **Create Dashboard** (top right).
- In **Add New Dashboard**, enter **Dashboard Name** (required) and **Folder name** (required).
- Select **Tags** from the dropdown (multiple tags allowed) to organize dashboards in the Dashboard Menu.
- Click **Add** (bottom right) to save.
- Click **Add Column** (top right) to choose a channel and start building columns.

### Create a Channel-Specific Column
- Open Engagement Dashboards (New Tab > Sprinklr Social > Engage).
- Create or open a dashboard (Dashboard Name + required Folder Name; optional Tags).
- Click **Add Column** (top right) — this shows all currently available channels; select one to create a channel-specific column.
- Article does not enumerate specific channel names, permissions, or limits.

### Create an Outbound Column
- New Tab > Sprinklr Social > Engagement Dashboards (within Engage); open desired dashboard and click **Add Column** (top right).
- In **Add New Column**, search and select **Outbound** as the source.
- Pick the outbound column type:
  - **All Messages** — all messages
  - **Sent** — posts that are sent
  - **Scheduled** — posts scheduled for publication
  - **Draft** — posts in draft state
  - **Group Messages** — all group messages
  - **Approval Required** — scheduled posts awaiting approval
  - **Approval Sent** — scheduled posts waiting for approval
  - **Approval Queue** — posts in the approval queue
  - **Rejected** — posts rejected by an approver
- Provide basic info: **Name**, **Status**, and add **Channels** from the dropdown.
- Configure **Outbound Properties** (message status, user assignment, priority, spam designation, sentiment).
- Add **Custom Properties** to include/exclude messages based on applied properties.
- Click **Create Column** (bottom right).
- Limits: a **Standard Outbound Dashboard** allows only Export, Sort, and Clone actions; it cannot be shared with other users and cannot have new columns added.

### Create a Workflow Column
- Open Engagement Dashboards (Sprinklr Social > Engage); open dashboard and click **Add Column** (top right).
- In **Add New Column**, search and select **Workflow** as the source.
- Choose a workflow column type: **Queues**, **Partner Queues**, **Assigned By Me**, **Assigned To Me**, **Enhanced Queues**, **Enhanced Partner Queues**, **Multiple Queues**.
- Basic config: enter **Name**, select **Queues**, choose **Channel(s)** and **Media Type(s)** from dropdowns (preview renders on the right pane).
- Configure **Workflow Properties** — set the message's workflow status, user assignment, priority, spam designation, and sentiment.
- Add **Custom Properties** to specify which messages to include/exclude based on applied properties.
- Click **Create Column**.
- See [[rule-engine]], [[sla-monitoring]] for routing/queue context.

### Select Account Groups in Engagement Dashboard Columns
- Steps to add a column: open Engagement Dashboards > select dashboard > **Add Column** > select a **Source** (column category icon) > choose **Column Type** > enter **Name** and **Description**.
- Under **Accounts**, select the accounts or **account groups** per your needs.
- Provide **Basic Information** (preview renders on the right), then **Workflow Properties** (workflow status, assignment, priority, spam, sentiment), **Custom Properties** (include/exclude messages), and **Channel Custom Properties** as needed.
- Click **Create Column**.
- Permission: the ability to add **account groups** while creating engagement columns is **DP-controlled** — contact your Success Manager to enable it.

### New Third Pane Experience — Inbound Columns
- Gives a snapshot of the message plus profile and conversations, with quick actions.
- Access: Engagement Dashboards > select dashboard > **Add Column** > select a social channel source > choose column type > enter **Name**, **Description**, add **Channels** and **Accounts** > set **Custom Properties** > **Create Column**.
- Open the pane: hover the **Inbound Message Options** icon and select **Open Details** (or double-click the asset).
- **Thread Section:** conversation view mirroring the native channel — original posts, comments, replies, with brand mentions highlighted.
- **Message tab:** Overview, Properties, Cases, Collaborate, Tasks, Attachments, Activity, Audit, Product Insights, Location Insights.
- **Profile tab:** Overview, Properties, Cases, Collaborate, Attachments, Tasks, Activity.
- The Collaborate section expands up to 60% when adding long notes (messages + attachments).

### New Third Pane Experience — Outbound Columns
- Gives a message snapshot and lets you perform Quick Actions.
- Benefits: external users can collaborate on content; view/edit message properties without entering edit mode (fewer clicks); future and completed tasks visible upfront; easy activity tracking.
- Access: Engagement Dashboards > select dashboard > **Add Column** > choose **Outbound** > pick column type (All Messages, Sent, Scheduled, Draft, Group Messages, Approval Required, Approval Sent, Approval Queue, Rejected) > set name, description, channels, accounts, custom properties > **Create Column** > hover the message options icon and select **Open Details**.
- Tabs: **Overview** (basic details, associated entities, campaign info), **Properties** (view/edit system + custom fields), **Collaborate** (team messaging with emoji reactions and search), **Attachments** (upload, preview, delete multiple files), **Tasks** (view past, create new), **Activity** (chronological changes and user actions).
- Preserves formatting when copying content; text area expands up to 60%.

### Community Management Persona App
- Consolidates engagement and community-management dashboards into one workspace; gives a top-level summary of how much people engage with your brand and your responses.
- **Left navigation:** single-click access to all engagement and reporting dashboards.
- **Home page widgets:** weekly summary of message volume and people engagement, response rate, follower trend.
- **Onboarding flow:** guided learning journey with videos and in-platform practice; progress tracked per step.
- **Focused dashboards:** shows only dashboards relevant to daily engagement on assigned channels.
- Capabilities: monitor via engagement dashboards; use the out-of-box **Smart Triage** dashboard, which auto-categorizes messages by intent; use the dashboard switcher; track metrics via reporting dashboards ([[reporting]]); share custom dashboards within the app for centralized action and progress monitoring.

## Common issues & fixes
- **Cannot add account groups to a column:** the account-groups capability is DP-controlled — contact your Success Manager to enable it.
- **Cannot share, add columns to, or act beyond Export/Sort/Clone on an outbound dashboard:** this is expected for a **Standard Outbound Dashboard**; create a custom outbound dashboard instead if you need more actions or sharing.

## Notes & gaps
- "What you can do" article lists capabilities (export, search, bulk actions, third pane) but no step-by-step config — steps live in the per-column setup articles.
- Channel-specific column article does not list the specific channel names available, nor its permissions/limits.
- Workflow column article documents no explicit limits or permissions.
- Export troubleshooting, file-size/row limits, and metric definitions for the persona app widgets (e.g. how response rate is calculated) are not specified in these articles.
- "Status" (outbound) and exact difference between Approval Required vs Approval Sent are named but not fully defined in the source.
- Related ARVIND topics: [[engagement-dashboards]], [[rule-engine]], [[sla-monitoring]], [[reporting]], [[care-console]], [[data-engine]].

## Sources
- What can you do with Engagement Dashboards — https://www.sprinklr.com/help/articles/engagement-dashboard-fundamentals/what-can-you-do-with-engagement-dashboards/6450dc2fd85662201933c821
- Select account groups in Engagement Dashboard columns — https://www.sprinklr.com/help/articles/engagement-dashboard-fundamentals/select-account-groups-in-engagement-dashboard-columns/649ac653efca565f6513b8a5
- Create an Engagement Dashboard — https://www.sprinklr.com/help/articles/dashboard-column-setup/create-an-engagement-dashboard/69dcc730ef08b45eb011afe7
- Create an Outbound Column — https://www.sprinklr.com/help/articles/dashboard-column-setup/create-an-outbound-column/6450f5e9d85662201933c85f
- Create a Workflow Column — https://www.sprinklr.com/help/articles/dashboard-column-setup/create-a-workflow-column/641beadf55c4c33ae8b81420
- Create a Channel-Specific Column — https://www.sprinklr.com/help/articles/dashboard-column-setup/create-a-channel-specific-column/641beadca1367f1be7db85a6
- Access new third pane experience for Inbound Columns — https://www.sprinklr.com/help/articles/message-third-pane/access-new-third-pane-experience-for-inbound-columns/645b3854e66f2e36b4518786
- Access new third pane experience for Outbound Columns — https://www.sprinklr.com/help/articles/message-third-pane/access-new-third-pane-experience-for-outbound-columns/6454a4790d27fc559bbeb49d
- Community Management Persona App — https://www.sprinklr.com/help/articles/community-management-insights/community-management-persona-app/641beae4a1367f1be7db85a7

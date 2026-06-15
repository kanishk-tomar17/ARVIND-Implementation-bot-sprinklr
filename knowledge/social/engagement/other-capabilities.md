# Other Engagement Capabilities (Sprinklr Social — Engagement)
**Source:** sprinklr.com/help — Engagement sub-area (multiple articles; see links below)

## What it is
- A set of supporting capabilities inside [[engagement-dashboards]] (Sprinklr Social > Engage > Engagement Dashboards) that improve agent workflow, privacy, governance, and security.
- Covers column-level usability (quick filters, condensed message previews), agent productivity (reminders, processing clock), governance/audit (activity tab, account re-add notifications), and security/privacy (NSFW blurring, hidden attachments, timed logout / secure access).
- Several features are gated by Dynamic Properties (DPs) or permissions and require enablement via Sprinklr Support / Success Manager.

## Key features & how to use

### Customize Quick Filter in Engagement Columns
- Lets users build personalized filters in engagement columns using standard fields, custom fields, and non-standard system fields; frequently used filters can be marked as favorites.
- Steps: New Tab icon > Engagement Dashboards (under Sprinklr Social in Engage) > open dashboard > hover top of column bar > click Filter icon > **Add Filter** > pick from **Filters** tab (standard) or **Custom Fields** tab (custom) > **Apply Filters** (bottom right).
- Mark a favorite: hover the filter and click the **Favorite** icon to surface it upfront in the standard filters list.
- **Include All / Exclude All** options appear in Quick Filters for all inbound and outbound engagement dashboard columns — include or exclude all values you select.
- Note: Include All / Exclude All do NOT auto-select all field values. A **Select All** option for single/multi-select custom fields must be enabled via support ticket.

### Enhanced Message Preview in Engagement Columns
- Shows a condensed preview for rich text channels (emails, forums, and similar) to reduce scrolling.
- By default only the **first 3–5 lines** are shown; a **View Full Message** option opens the complete content in a modal popup.
- Controlled by DP: `ENGAGEMENT_RENDER_MINIMIZED_TEXT_FOR_RICH_TEXT_CHANNELS`.
  - Enabled: rich text channels show a short plain-text snippet (~3–5 lines) in columns and message lists.
  - Disabled: previews render as before, without truncation.

### Set Reminders on Engagement Dashboard
- Set time-based reminders on inbound messages (tweets, Facebook messages, etc.); reminders pop up at scheduled times and can target multiple recipients and a responsible team member.
- Steps: Engagement Dashboards (Sprinklr Social > Engage) > Dashboard Menu icon > select dashboard/column > hover the **Options** icon on the message column > **Reminders** > fill the **Add New Reminder** pop-up > **Add**.
- Add New Reminder fields: **Send To** (recipients), **Calendar** (date/time), **Message** (reminder text), **Assign To** (responsible user), **Queue**, **Macros** (template dropdown).
- Multiple reminders per message are allowed. Edit: open reminder, change, **Save**. Delete: select reminder, click Delete icon, confirm **Yes**.
- Configured reminders display in the left pane under the **Reminder** section.

### Processing Clock on Messages
- Measures time spent on a message for accurate response/processing-time assessment.
- Starts when the message's **third pane** is opened (double-click the message); pauses when the third pane is closed.
- Steps: New Tab > Engagement Dashboards > double-click message to open third pane (clock starts) > click **Close** icon (top right of Message Pane) to pause.
- Resumes when the same or another agent re-opens the third pane.
- To stop resumption from a paused state, apply a **macro configured with the "Stop Processing User" action** (related: macro configured with "Stop Processing Clock" action prevents pause-to-resume on close). See [[rule-engine]] / macros.

### View Audit History with Activity Tab in Engagement Dashboards
- Review and restore previous versions of an engagement dashboard and track all changes over time (protects against accidental edits).
- Steps: New Tab > Engagement Dashboards > select dashboard > **Options** icon (top-right menu) > **Activity** > view the **Dashboard Audit Log** pane > use **Copy** icon to duplicate a version or **Restore** icon to restore it.
- Tracked events — Dashboard level: Compare Mode (Enabled/Disabled), Added, Updated, Locked, Shared, Restored. Tracked fields: Dashboard Name, Folder, Tags. Column level: Filters Added/Updated (filter/field name), Quick Filters Added/Updated (filter/field name), Exports Triggered (column).
- On restore: selected metrics and dimensions stay the same, but the value/data reflects the most recent updates.

### NSFW Content Blurring in Sprinklr Social
- Uses machine learning to identify and manage NSFW, triggering, or objectionable content across social streams; can blur/censor sensitive media and flag accounts that frequently share it.
- Content handling: organizations can blur OR completely remove objectionable media.
- Account-level moderation: repeat-offender accounts can be blocked or auto-blurred — share account IDs with Sprinklr Support; flagged accounts' posts then follow the configured action.
- Custom detection: can be trained to blur specific objects/themes (e.g., violence, competitor logos) — contact Support to configure.
- Bio-based filtering: ML detects NSFW links/offensive language in account bios and blurs/flags those profiles.
- Controlled by DP: `MARK_MEDIA_AS_NSFW`. Enabled: all media flagged sensitive, routed through sensitive-content workflows, blurred by default until revealed. Disabled: standard processing; media visible unless manually marked sensitive.
- Enable via Support at tickets@sprinklr.com.

### Managing Permissions for Hidden Attachments in Engagement
- Protects sensitive attachments (PDFs, screenshots, other media containing account statements / PII) by concealing them by default.
- Users without access see: "This media is private and you don't have permission to access it." Restriction also applies to exports.
- Permission name: **Hide Attachments** (in the Engagement permissions section).
- Inverse logic: users WITH the permission CANNOT view sensitive attachments; users WITHOUT it CAN view them. This lets admins explicitly restrict specific roles.
- Controlled by DP: `HIDE_ATTACHMENTS_PERMISSION_ENABLED`. Enable via Success Manager or tickets@sprinklr.com.

### Permission to Control Account Re-Add Notification in Engagement Dashboard
- A notification bar alerts engagement dashboard users about accounts deactivated within the last 30 days; authorized users can re-add the account or request admin help.
- Grant access by creating a role with the right permission: New Tab > **All Settings** (under Listen's Platform Modules) > Platform Settings > **Workspace Roles** or **Global Roles** > **Create Role** > fill **Name**, optional **Description**, **Users and User Groups**, and under **Role Permissions** search/select **Account Notify Admin Bar View** > **Save**.
- Actions on the notification bar: re-add accounts via account settings; Notify Admin (email + UI push notification).
- Limits/config:
  - Admins receive one notification per account per 3-day period; configurable at partner level via `ACCOUNT_RE_ADD_NOTIFICATION_INTERVAL`.
  - Recipients: account/account-group subscribers and the account owner.
  - Delivery: both email and UI push notification.
  - Internal/data-platform flag: `ACCOUNT_NOTIFY_ADMIN_BAR_ENABLED`.

### Timed Logout and Multiple Secure Access
- Assign multiple credentials with different access levels to the same social account, including time-limited access and forced logout. Supported only on **Safari** browser as of now.
- Setup: Listen > Platform Modules > **All Settings** > **Edit** next to the account > **Sprinklr Secure Access** section > choose a **Role** > enter **User Name** and **Password** > set **Provisioned Users / User Groups** > **Calendar** icon under **End Date** to set expiry > **Add More Users \ User Groups** (each can have a different end date) > assign other roles as needed > **Save**.
- Usage: Sprinklr Social > **Owned Social Accounts** > **Manage Customer** tab > **Secure Access** > hover **Options** icon > **Login as Role** (Admin, View Only, etc.) > auto-logged into the social account with that role's permissions.

## Common issues & fixes
- Quick Filter "Include All / Exclude All" does not select every value — there is no built-in Select All for single/multi-select custom fields; raise a support ticket to enable it.
- Hidden attachment shows "This media is private and you don't have permission to access it" — expected when the user holds the **Hide Attachments** permission (inverse logic) or lacks access; restriction also blocks the attachment in exports.
- Timed Logout / Secure Access not working in Chrome or other browsers — feature is Safari-only as of the article date.

## Notes & gaps
- Enablement dependencies: Enhanced Message Preview (`ENGAGEMENT_RENDER_MINIMIZED_TEXT_FOR_RICH_TEXT_CHANNELS`), NSFW (`MARK_MEDIA_AS_NSFW`), Hidden Attachments (`HIDE_ATTACHMENTS_PERMISSION_ENABLED`), and Re-Add notification interval (`ACCOUNT_RE_ADD_NOTIFICATION_INTERVAL`) are Dynamic Properties — typically enabled by Sprinklr Support / Success Manager (tickets@sprinklr.com), not self-serve.
- Permissions required: **Hide Attachments** (Engagement section); **Account Notify Admin Bar View** (role permission) for re-add notifications.
- Processing Clock: articles reference both a "Stop Processing User" macro action and a "Stop Processing Clock" macro action — confirm the exact macro action name in-platform before configuring.
- Account re-add window is fixed at "within 30 days"; the articles do not specify whether this 30-day window is configurable.
- NSFW custom object/theme detection and account-level blocking are configured by Sprinklr Support; the articles do not expose a self-serve UI for these.
- Articles do not specify license/edition requirements or interactions with [[care-console]], [[sla-monitoring]], or [[reporting]] beyond what is listed.

## Sources
- Customize Quick Filter in Engagement Columns — https://www.sprinklr.com/help/articles/other-engagement-capabilities/customize-quick-filter-in-engagement-columns/64df6970c86d912cb59da88e
- Enhanced Message Preview in Engagement Columns — https://www.sprinklr.com/help/articles/other-engagement-capabilities/enhanced-message-preview-in-engagement-columns/69c3ab2c3d2bda6aa7420c99
- Set Reminders on Engagement Dashboard — https://www.sprinklr.com/help/articles/other-engagement-capabilities/set-reminders-on-engagement-dashboard/6454a2f50d27fc559bbeb491
- Processing Clock on Messages — https://www.sprinklr.com/help/articles/other-engagement-capabilities/processing-clock-on-messages/6454a2f6f65d86626c82b915
- View Audit History with Activity Tab in Engagement Dashboards — https://www.sprinklr.com/help/articles/other-engagement-capabilities/view-audit-history-with-activity-tab-in-engagement-dashboards/695e5b4eed1e4535a502de80
- NSFW Content Blurring in Sprinklr Social — https://www.sprinklr.com/help/articles/other-engagement-capabilities/nsfw-content-blurring-in-sprinklr-social/69f0a9c2fc216852d09bb8f3
- Managing Permissions for Hidden Attachments in Engagement — https://www.sprinklr.com/help/articles/other-engagement-capabilities/managing-permissions-for-hidden-attachments-in-engagement/695e5be0f0afa271d1af772b
- Permission to Control Account Re-Add Notification in Engagement Dashboard — https://www.sprinklr.com/help/articles/other-engagement-capabilities/permission-to-control-account-readd-notification-in-engagement-dashboard/64564d2fe66f2e36b4514d7d
- Timed Logout and Multiple Secure Access — https://www.sprinklr.com/help/articles/other-engagement-capabilities/timed-logout-and-multiple-secure-access/64df6fa3d8ffbe0c80350c86

Related GROOT topics: [[engagement-dashboards]], [[rule-engine]], [[reporting]], [[sla-monitoring]], [[data-engine]], [[care-console]]

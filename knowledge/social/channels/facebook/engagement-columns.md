# Facebook — Engagement Columns (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- Engagement Columns are live, filterable feeds of Facebook content added to an [[engagement-dashboards|Engagement Dashboard]] so consultants can monitor and respond from one place.
- Every Facebook column type is created the same way: open an Engagement Dashboard → **Add Column** (top-right) → pick **Facebook** (or **Facebook Workplace**) as the source → choose the column type → fill **Basic Information** + optional [[rule-engine|Workflow/Custom Properties]] → **Create Column**.
- The "Add New Facebook Column" picker exposes these types in one list: **Inbox, Posts, Comments, Replies, Messenger, Events, Shares, Group Posts, Group Comments, Group Replies**, plus Facebook Dynamic Posts and Instagram-related types (out of scope here).
- Several "column types" in these articles are actually the **Posts** column with a specific filter set: Dark Posts (Published Status = Only Unpublished), Page Recommendations (Media Type = Recommendation), and External Mentions (Show only Mentions On External Sources).
- A live **Column Preview** pane on the right renders the feed as you configure it, so you can confirm before saving.

## Key features & how to use

### Facebook Posts column
- Add Column → Facebook → **Posts**.
- Basic Information: **Name** (required), **Description**, **Account** (one or more Facebook accounts — chips shown inline).
- **Post Type** dropdown: **All / Fan Post / Brand Post**.
  - **Brand Post** — posts your brand published on its own account.
  - **Fan Post** — posts by fans where the brand was mentioned/tagged.
- Additional filters visible in the dialog: **With Brand Comments**, **Sponsored Post**, **Media Type**, **Keywords** (comma-separated; only posts containing them are fetched), **Exclude Keywords**, **Default Date Range** (e.g. Lifetime), **Countries**, **Show** (All messages).
- Click **Create Column** (bottom-right).

### Facebook Comments column
- Add Column → Facebook → **Comments**.
- Basic Information: **Name**, **Description**, **Account**.
- **Comment Type** dropdown: **All / Brand Comment / Fan Comment**.
  - **Brand Comment** — comments the brand made on its own posts or posts where it was mentioned/tagged.
  - **Fan Comment** — comments made by fans on your Facebook posts.
- Same shared filters as Posts (Sponsored Post, With Brand Comments, Keywords/Exclude Keywords, Default Date Range, Countries, Show). Preview shows threaded comments with a **View Conversation** link.
- Click **Create Column**.

### Facebook Replies column
- Add Column → Facebook → **Replies**.
- Basic Information: **Name**, **Description**, **Account**.
- Reply-specific dropdowns: **Comment Type**, **Reply Type**, **Show Edited** (All / …), **Sponsored Post**, **With Brand Comments**, **Exclude Keywords**, **Show**.
- Displays all replies to comments on the selected account (including replies to brand posts and brand mentions). Preview marks each item as **Reply** with a **View Conversation** link.
- Click **Create Column**.

### Facebook Page / Profile column (Inbox)
- Add Column → Facebook → **Inbox**.
- In the **Accounts** tab pick the account type:
  - **Facebook Page** — all posts, comments, replies for a particular Facebook Page.
  - **Facebook Profile** — all posts, comments, replies for a particular Facebook Profile added in Sprinklr.
- Enter Name, Description, Accounts, plus Workflow Properties (status, assignment, priority, Spam, sentiment) and Custom Properties (include/exclude messages).
- Click **Create Column**. This is the consolidated inbox view for one page/profile.

### Facebook Messenger column
- Add Column → Facebook → **Messenger**.
- Basic Information: **Name**, **Description**, **Account**.
- Produces a column of Messenger conversations — both sent and received direct messages for the account.
- Review the preview, then click **Create Column**.

### Facebook Dark Posts column
- Dark Posts = targeted/sponsored posts that do NOT appear on the brand timeline; they show only in the feeds of users being targeted.
- Add Column → Facebook → **Posts** (there is no separate "Dark Posts" type).
- Basic Information: Name, Description, Account.
- Set **Published Status** = **Only Unpublished** (this is what isolates dark posts).
- Optional Workflow + Custom Properties.
- Click **Create Column**. Dark posts render with a black **Dark Post** badge/icon in the feed.

### Facebook Shares column
- Add Column → Facebook → **Shares**.
- Basic Information: Name, Description, Account.
- Optional Workflow Properties (status, assignment, priority, Spam, sentiment) and Custom Properties (include/exclude).
- Click **Create Column** to see shares of the account's content.

### Facebook Page Recommendations column
- Recommendations = social feedback/recommendations left on a Facebook Page; monitor and reply to optimize business performance.
- Add Column → Facebook → **Posts**.
- Enter Name, optional Description, select Account(s).
- Set the **Media Type** dropdown = **Recommendation**.
- Click **Create Column**. To respond, click the **Comment icon** below a recommendation message.

### Facebook Workplace column
- Facebook Workplace = Meta's collaboration tool (group work, instant messaging, video conferencing, news sharing).
- Add Column → choose **Facebook Workplace** as the source (separate from the standard Facebook source).
- The "Add New Facebook Workplace Column" picker offers exactly three types:
  - **Group Posts** — posts made in the Workplace group.
  - **Group Comments** — comments on group posts.
  - **Group Replies** — replies to comments within the group.
- Enter Name, Description, Accounts, plus Workflow and Custom Properties; preview renders on the right.
- Click **Create Column**.

### Facebook External Mentions column
- External Mentions = mentions of the brand NOT posted to the brand's own Facebook Wall — fetched from external Facebook profiles/pages.
- Add Column → Facebook → **Posts** (a.k.a. "Post").
- Enter Name, Description, select Account(s).
- Tick the checkbox **Show only Mentions On External Sources**.
- Other fields available in this dialog: **Show Edited**, **Media Type**, **Keywords / Exclude Keywords**, **Default Date Range**, **Countries**, **Sort** (e.g. Descending), **Published Status**, **Campaign**, **Branded Content**, **Show Only Shared Posts** checkbox, **Refresh Time**, **Column Color**, **Notify new Messages** checkbox.
- Set Workflow + Custom Properties, then click **Create Column**.

## Common issues & fixes
- **External mentions appear late / incomplete** — Facebook delivers external mentions through a non-real-time update path, so processing is delayed. This is expected behavior, not a misconfiguration.
- **Brand's own posts polluting the External Mentions column** — brand @-mentions are counted as external mentions; exclude brand messages (via Custom Properties / Post Type filters) to keep the column clean.
- **Dark posts not showing** — they only surface when **Published Status = Only Unpublished**; a default Posts column will not show them.
- **Account deactivated warning** — the Inbox/preview can show a banner like "Account … and N other accounts have been deactivated recently. Please re-add to see data" — re-add the affected accounts to restore the feed.

## Notes & gaps
- Prerequisites: the Facebook (or Facebook Workplace) accounts must already be added/authenticated in Sprinklr; Workplace requires the Facebook Workplace source specifically.
- **Workflow Properties** = properties applied (auto or manual) that set a message's workflow status, user assignment, priority, Spam designation, and sentiment. **Custom Properties** = filters to include/exclude messages by applied property.
- The articles do **not** specify required user permissions, role requirements, account/column limits, or quotas for any of these column types.
- "Page Recommendations" and "External Mentions" are configuration variants of the **Posts** column, not standalone menu entries — confirm by the filter you set (Media Type = Recommendation / Show only Mentions On External Sources checkbox).
- Field availability varies slightly by column type; the dialogs share a common Basic Information block (Name, Description, Account, Keywords, Date Range, Show).

## Sources
- Create a Column for Facebook Posts — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-facebook-posts/63ea1c7df6e2cc7d18f962bd
- Create a Column for Facebook Comments — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-facebook-comments/63ea6752f6e2cc7d18f9639c
- Create a Column for Facebook Replies — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-facebook-replies/63ea687ff6e2cc7d18f963a3
- Create a Facebook Page/Profile Column — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-facebook-pageprofile-column/63ea6109f6e2cc7d18f96376
- Create a Column for Facebook Messenger — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-facebook-messenger/63eb96eef6e2cc7d18f995a5
- Create a Column for Facebook Dark Posts — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-facebook-dark-posts/63ea5f82f6e2cc7d18f96375
- Create a Column for Facebook Shares — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-facebook-shares/63eb9805ef1b447d6c61e4aa
- Create a Column for Facebook Page Recommendations — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-facebook-page-recommendations/63eb95d0f6e2cc7d18f9959c
- Create a Facebook Workplace Column — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-facebook-workplace-column/63ea6471f6e2cc7d18f9637d
- Create a Column for External Mentions — https://www.sprinklr.com/help/articles/add-facebook-column-in-engagement-dashboard/create-a-column-for-external-mentions/63eb2f96ef1b447d6c61b4fa

Related: [[engagement-dashboards]] · [[publishing]] · [[reporting]] · [[rule-engine]] · [[asset-manager]]

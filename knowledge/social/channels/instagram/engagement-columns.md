# Instagram — Engagement Columns (Sprinklr Social — Instagram)
**Source:** sprinklr.com/help — Instagram channel (multiple articles; see links below)

## What it is
- Engagement Dashboards in [[engagement-dashboards]] let agents monitor and reply to Instagram activity in dedicated columns — one column per content/conversation type.
- For Instagram you add columns via **Add Column** (top-right) → search/select **Instagram**, then pick a column type.
- The Instagram column-type list (in the "Add New Instagram Column" picker) is: **Inbox, Media, Comment, Story, Mention, Comment Mention, Replies, Tagged Media, Direct Messages**.
- Instagram **Dark Posts** are added from the **Facebook** source (not the Instagram source), because they are pulled through the associated Facebook Ads account.
- All column builders share the same layout: left = config (Basic Information, Workflow Properties, Custom Properties), right = live **Column Preview** pane. Finish with **Create Column** (bottom-right); **Cancel** discards.

## Key features & how to use
Common navigation for every column type below: New Tab icon → **Sprinklr Social** → under **Engage**, **Engagement Dashboards** → open a dashboard (Dashboard Menu icon, top-left) → **Add Column** (top-right) → search/select **Instagram** (a tile in the searchable "Add New Column" grid).

Common config fields (vary slightly by type, seen in screenshots):
- **Name** (required), **Description**, **Account** (required; multi-select chips).
- **Post Type** dropdown — All / Brand Post / Fan Post (where applicable).
- **Keywords** (only posts containing these are fetched), **Default Date Range** (e.g. Lifetime), **Sort** (e.g. Descending), **With Liked Posts**, **Campaign**, optional **Refresh Time**.
- **Workflow Properties** — set workflow status, user assignment, priority, Spam flag, sentiment.
- **Custom Properties** — include/exclude messages based on applied properties.

### Posts column (Brand Post / Fan Post)
- Add Column → Instagram → **Inbox**, then enter Name / Description / Account.
- Choose **Post Type**:
  - **Brand Post** — all posts the brand made on its own Instagram account.
  - **Fan Post** — posts made by fans where the brand was mentioned/tagged.
- **Create Column**.

### Comments column
- Add Column → Instagram → **Comment**.
- Set Name / Description / Account, then pick comment type:
  - **Brand Comment** — comments the brand made on its own or tagged/mentioned posts.
  - **Fan Comment** — comments fans made on brand posts.
  - **All** — both.
- Preview renders in the right pane → **Create Column**.

### Replies column
- Add Column → Instagram → **Replies**.
- Enter Name / Description / Account — shows all replies to comments on the associated Instagram account.
- **Create Column**.

### Direct Messages (DM) column
- Add Column → Instagram → **Direct Messages**.
- Set Name / Description / Accounts, configure Workflow Properties and Custom Properties → **Create Column**.
- Reply window limits (important): the fan must have sent at least one DM in the **past 7 days**; you **cannot reply after 7 days** — respond natively instead.
- DMs deleted natively on Instagram are also deleted in Sprinklr.
- Supported inbound DM media: text, images, audio messages, hearts, stickers, boomerang videos, layout photos, carousel posts, story tags. **Not supported:** Instagram video posts as DM, photo stories as DM, reel videos.

### Media column (by media type)
- Add Column → Instagram → **Media**.
- Under **Media Type**, select one, multi-select, or **Select All**: **Photo, Video, Carousel, IGTV Post, Instagram Reel** (screenshot shows these exact options).
- Set the rest of Basic Information (Name, Account, Post Type, Keywords, Date Range, Sort) → **Create Column**.

### Tagged Media column (tagged posts)
- Add Column → Instagram → **Tagged Media**.
- Enter Basic Information; configure Workflow + Custom Properties → **Create Column**.
- Posts shown match the brand handle's **Tagged** section on Instagram.
- If **manual approval of tags** is enabled on the Instagram account, posts must first be approved natively before they appear in Sprinklr's tagged column.

### Story Mentions column (via DM column)
- Add Column → Instagram → **Direct Messages**.
- Set Name / Description / Accounts; under **Instagram Story Mention**, pick the desired option from the dropdown.
- Configure Workflow + Custom Properties → **Create Column**.

### Story Mentions via Rule Engine
- New Tab → **Sprinklr Social** → under **Triage**, **Manage Rules** → **Create New Rule**.
- Rule details: Name, Description, context = **Inbound**; set Activation Date / Rule Execution Batch (or defaults) → **Next**.
- In Rule Builder, add conditions (Add Condition → Add another Condition):
  - **Channel** = Instagram
  - **Message Type** = Instagram Direct Message
  - **Message Subtype** = Story Mention
  - **Account** = your account
- Add Action on the Yes/No branch → **Save** (or **Save as Draft**).
- See [[rule-engine]].

### Story Mentions via Reporting widget
- New Tab → **Sprinklr Social** → under **Analyze**, **Reporting** → open a dashboard → **Add Widget** → **Create Custom Widget**.
- **Widget Name** (+ optional Add Description); **Data Source** = **Inbound Analytics**.
- Choose a visualization (e.g. Table); plot e.g. **Inbound Message** + **Inbound Count (Sum)**.
- Under **Define Advanced Options → Filters**, set **Media Type** = **Story_mention**.
- **Add to Dashboard**. See [[reporting]].

### Dark Post column
- Dark Posts = specifically targeted/sponsored posts; they don't appear on the timeline like organic/boosted posts but show as sponsored content to targeted users.
- **Prerequisite:** the associated **Facebook Ads account** must be added to pull Instagram Dark Posts and their comments. See [[facebook]].
- Add Column → select **Facebook** (not Instagram) → pick **Instagram Dark Posts** (the Facebook type list also has **Instagram Dark Post Comments** and **Instagram Dark Post Replies**).
- Set Name / Description / Accounts; under **Associated Instagram Account**, choose account(s) to filter comments/replies.
- Configure Workflow + Custom Properties → **Create Column**.

### Branded Content / Paid Partnership collab posts
- Feature surfaces influencer/creator collab posts (Instagram "paid partnership with" label) to drive traffic.
- **Prerequisites:** brand and creator must accept each other as brand/creator on their Instagram profiles; **re-add your Instagram account after Data Partner (DP) enablement** to pull posts. Comments can be fetched for paid-partnership posts (even during DP approval stage); for normal collab posts, comments fetch only if you are the initiator/primary account.
- Five ways to view them:
  1. **Outbound column** — Add Column → **Sent**, name it, select Instagram, set **Branded Content** = **Yes**.
  2. **Inbound column** — Add Column → Instagram → **Media** tab (or **Comments** tab for threads), set **Branded Content Conversation** = **Yes**.
  3. **Editorial Calendar** ([[publishing]]) — Filters → search "Branded" → **Is Branded** = True.
  4. **Reporting** ([[reporting]]) — Filters → search "Branded" → **Is Branded** = True.
  5. **Rule Engine** ([[rule-engine]]) — Create New Rule → Inbound → condition **Is Branded Content Conversation** → add actions to tag/organise.

### Delete Instagram comments
- In an Instagram **Comment** column, select the comment → hover the **options menu (…)** icon → **Delete** (top of the menu, alongside Hide, Open Details, Reminders, Sentiment, Email, Suggest, Update Tags, Translate, Mark as Spam, Mark Secure, Preview on a Rule, Create Case, Associate/Dissociate Cases).
- Deletion is **permanent** — removes the comment from **both Sprinklr and the native Instagram feed**.

## Common issues & fixes
- **Can't reply to a DM / story mention** — the fan must have messaged within the last 7 days; after 7 days the reply window is closed in Sprinklr, reply natively on Instagram.
- **Tagged posts missing** — if tag approval is enabled on Instagram, approve them natively first.
- **Dark Posts / branded comments not pulling** — confirm the Facebook Ads account is connected (Dark Posts), and re-add the Instagram account after DP enablement (branded content).
- **Comment deletion is irreversible** — it also deletes natively; confirm before deleting.

## Notes & gaps
- Prerequisites/permissions: connected Instagram account(s) (Business/Creator via Facebook); for Dark Posts a linked Facebook Ads account; for branded content, DP enablement + mutual brand/creator acceptance. Specific user-permission/role requirements are not stated in these articles.
- The "Story Mention via DM column" article labels the column type **Direct Message** (story mentions arrive as DMs), then adds the **Instagram Story Mention** option — this is the canonical path; the Rule Engine and Reporting methods are alternatives for routing/measuring rather than a standalone story column.
- Articles do not document per-column data-retention limits, max columns, or bulk-delete behaviour.
- Reporting media-type filter value is exactly **Story_mention** (underscore, case as shown).

## Sources
- Create a Column for Instagram Posts — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-posts/63e389cda9d511790301664d
- Create a Column for Instagram Comments — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-comments/63e38d4a55780d70a15bd9f6
- Create a Column for Instagram Replies — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-replies/63ec70e3ef1b447d6c6272b6
- Create Engagement Column for Instagram Direct Messages — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-engagement-column-for-instagram-direct-messages/645930110104980882a57ea6
- Create a Column for Instagram by Media Type — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-by-media-type/63e38ffa55780d70a15bda05
- Create a Column for Instagram Tagged Posts — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-tagged-posts/63e4a636a9d51179030176a5
- Create a Column for Instagram Story Mentions — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-story-mentions/63e48aae55780d70a15be989
- Create a Column for Instagram Story Mentions using Rule Engine — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-story-mentions-using-rule-engine/63e48bb6a9d5117903017621
- Create a Column for Instagram Story Mentions using Reporting Widgets — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-story-mentions-using-reporting-widgets/63ec704cef1b447d6c6272a9
- Create a Column for Instagram Dark Post — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/create-a-column-for-instagram-dark-post/63e38ba2a9d511790301665d
- View Branded Content (Paid Partnership Collaborations) for Instagram on Engagement Dashboard — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/view-branded-content-paid-partnership-collaborations-for-instagram-on-engagement-dashboard/6457c2b9e66f2e36b4515bd8
- Delete Instagram Comments — https://www.sprinklr.com/help/articles/create-an-instagram-column-in-engagement-dashboard/delete-instagram-comments/63ec71dcf6e2cc7d18fa250e

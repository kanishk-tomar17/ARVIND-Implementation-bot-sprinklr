# LinkedIn — Engagement (Sprinklr Social — LinkedIn)
**Source:** sprinklr.com/help — LinkedIn channel (multiple articles; see links below)

## What it is
- How consultants engage with LinkedIn content inside Sprinklr's [[engagement-dashboards]] (Sprinklr Social > Engage).
- Covers building LinkedIn engagement columns, applying LinkedIn reactions (single and multi-account), replying to direct messages on LinkedIn Company Pages, and toggling comments on/off for posts.
- Works across LinkedIn Profiles, LinkedIn Company Pages, and LinkedIn Showcase Pages (Showcase Pages behave like Company Pages).
- All actions run from the same place: a column in an Engagement Dashboard, via the message's Options (three-dot) icon.

## Key features & how to use

### Create an engagement column for LinkedIn
- Path: New Tab icon > Sprinklr Social > **Engagement Dashboards** > Engage.
- Click **Add Column** (top-right).
- In the dialog, select **LinkedIn** (the source list is searchable), then pick a **column type**. Available LinkedIn column types (from the "Add New LinkedIn Column" screen):
  - Company Inbox, Company Status Update, Company Status Comments, Company Status Replies
  - Direct Sponsored Contents
  - Profile Network Update, Profile Comments, Profile Replies
  - Articles, Recommendations, Endorsements
  - Private Messages
  - Articles Comments, Article Replies
  - Brand Likes
- Fill **Basic Information** — a live **Column Preview** renders on the right panel as you configure.
- Set **Workflow Properties** — controls the message's workflow status, user assignment, priority, Spam designation, and sentiment. See [[rule-engine]].
- Set **Custom Properties** — filters the column to messages carrying the chosen applied properties.
- Click **Create Column**.
- Like / delete comments from the column: open the dashboard (Dashboard Menu icon), find the message, hover the **Options** icon, choose **Like** or **Delete**.

### Use LinkedIn reactions (like, unlike, react, multi-account)
- Path: New Tab > Sprinklr Social > **Engagement Dashboards** > open the dashboard from the Engagement Home window.
- Hover the message's **Options** icon to open the reaction picker (a row of reaction icons appears at the top of the menu).
- Six reactions available (left to right in the picker): **Like, Celebrate, Support, Love, Insightful, Funny** (hovering shows the label, e.g. "Funny").
  - Like — simple show of interest/support.
  - Celebrate — company news and professional milestones.
  - Support — empathy during challenging times.
  - Love — deeper connection to content.
  - Insightful — quality contributions / in-depth data.
  - Funny — humor and wit.
- **Unlike:** hover the Options icon and select **Unlike**.
- **Like from multiple accounts:** in the same Options menu choose **Like from multiple accounts** (top of the menu, with an arrow to expand). A **Select Accounts** pop-up opens; hover each desired account and pick its reaction.
- Same Options menu also surfaces related actions: Reshare, Send to Advocacy, Open Details, Reminders, Sentiment, Email, Suggest, Update Tags, Translate, Mark as Spam, Mark Secure, Preview on a Rule.

### Direct messages from LinkedIn Company Pages to profiles
- What's supported: a LinkedIn Page **cannot initiate** a DM to a profile, but it **can reply** to a DM started by a profile.
- Permission required: admin must have **"Manage messages to the Page"** to reply on the company's behalf.
- Reply steps:
  1. New Tab > Sprinklr Social > **Engagement Dashboards** > Engage.
  2. Click the **Dashboard Menu** icon (top-left) and select your dashboard.
  3. Find the message from the LinkedIn profile and click **Reply**.
  4. Type in the **"Enter your reply here..."** field (rich-text formatting + multi-line supported).
  5. Choose **Save as Draft** (for later) or **Send** (deliver now).
- Limits: 8,000-character max per message; backfill is max 500 messages across the last 500 threads.
- If the Company Page has DMs disabled on LinkedIn, profiles cannot message it.
- After enabling DM functionality, you must **re-add the LinkedIn Company Page** in Sprinklr to access direct messages.

### Disable / enable comments on LinkedIn posts
- Works for both LinkedIn Company and LinkedIn Profile posts; controllable at publish time (see [[publishing]]) or later from Engagement Dashboards.
- Permission required: **"Toggle Comment"** under Role Level Permissions > Account Types, for both **LINKEDIN** and **LINKEDIN COMPANY** account types.
- Steps (from a dashboard):
  1. New Tab > Sprinklr Social > **Engagement Dashboards** > Engage.
  2. Go to the target post in its column.
  3. Click the **Options** icon next to the post.
  4. Select **Disable Comments** (the menu toggles to **Enable Comments** when already disabled).
- The Options menu on a post also shows: Boost Post, Delete, Reshare, Sentiment, Email, Suggest, Create Canned Response, Update Tags, Translate, Mark as Spam, Mark Secure, Preview on a Rule.

## Common issues & fixes
- **Disabling comments deletes existing comments:** when you disable comments on a post, all existing comments on that post are permanently deleted. Confirm before toggling.
- **DMs not showing after enabling:** re-add the LinkedIn Company Page in Sprinklr; DMs only backfill the last 500 threads (max 500 messages).
- **Cannot DM a Company Page:** the page has DMs disabled on LinkedIn, or you're trying to initiate from the page (only replies are supported).
- **Reply / reaction / toggle option missing:** check the relevant Role Level Permission ("Manage messages to the Page" for DMs; "Toggle Comment" for comment control).

## Notes & gaps
- Prerequisites: a connected LinkedIn account (Profile / Company / Showcase) and the correct role-level permissions per account type.
- Showcase Pages are treated like Company Pages throughout.
- Reactions and comment-toggle are driven from the message's Options icon in [[engagement-dashboards]]; same entry point across all four workflows.
- Not specified in sources: exact location of "Manage messages to the Page" permission in the role editor; whether reactions can be removed/changed after the fact beyond the Unlike action; per-day rate limits on multi-account likes; sentiment/[[reporting]] impacts of these actions.

## Sources
- Create Engagement Column For LinkedIn — https://www.sprinklr.com/help/articles/engage-on-linkedin/create-engagement-column-for-linkedln/64536e750d27fc559bbe9315
- Use LinkedIn Reactions — https://www.sprinklr.com/help/articles/engage-on-linkedin/use-linkedin-reactions/63fef3fc32d12b63c5f55c54
- Direct Messages from LinkedIn Company Pages to Profiles — https://www.sprinklr.com/help/articles/engage-on-linkedin/direct-messages-from-linkedin-company-pages-to-profiles/65f98aeca7d38d01684336cb
- Disable/Enable Comments on LinkedIn Posts — https://www.sprinklr.com/help/articles/engage-on-linkedin/disableenable-comments-on-linkedin-posts/64819c8f723d925979db895e

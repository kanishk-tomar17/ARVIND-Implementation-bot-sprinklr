# YouTube — Engagement & Moderation (Sprinklr Social — YouTube)
**Source:** sprinklr.com/help — YouTube channel (multiple articles; see links below)

## What it is
- Lets consultants engage with and moderate native YouTube conversations from a Sprinklr [[engagement-dashboards]] column once a YouTube account is connected.
- Covers: building YouTube columns, approving/holding/rejecting comments, banning disruptive commenters, and pulling YouTube live-chat messages.
- All moderation actions push back to YouTube natively — no separate YouTube admin login needed once the account is integrated.
- Replies, sentiment, tagging, casing and rule automation work on YouTube messages like other channels (live-chat is read-only — see limits below).

## Key features & how to use

### Create a column for YouTube
- New Tab icon > **Sprinklr Social** > **Engage** > **Engagement Dashboards** > open the target dashboard > **+ Add Column** (top-right).
- In the **Add New Column** window, search and select the **YouTube** source tile.
- **Add New YouTube Column** then offers these column types: **Inbox**, **Search**, **Persistent Search**, **Videos**, **Video Comments**, **My Playlist**, **Video Comment Replies** (and **Chats** for live chat — see below).
  - Inbox = videos, comments, replies, playlists in one stream.
  - Search = posts by query; sortable by Relevance Rating, View Count, Published.
  - Persistent Search = saved query-based posts. Videos = your published videos. My Playlist = your created playlists.
- Fill **Basic Information**: **Name** (required), **Description**, **Account** (required), optional **Keywords** / **Exclude Keywords** (comma-separated; only/never-containing those words), **Default Date Range**, **Sort** (e.g. Descending), **Comment Type**, **Show** (e.g. All messages), **Campaign**, **Refresh Time**, **Column Color**. Live preview shows on the right.
- Optional: **Workflow Properties** (status, assignment, priority, spam, sentiment) and **Custom Properties** to include/exclude messages.
- Click **Create Column** (bottom-right).
- Data limits: video grabber fetches up to **500 videos**; comments pulled from the **previous 900 days** up to a **max of 20,000**; missing parent videos are auto-fetched to keep threads intact.

### YouTube comment moderation
- **Prerequisite (native YouTube):** the channel admin must set YouTube to **require approval for all comments** (Google support article 9482556) so comments arrive as "Held" for moderation in Sprinklr.
- Build a **Video Comments** or **Video Comment Replies** column (steps above).
- In Basic Information, set the **Moderation Status** multi-select. Options: **Select All**, **All**, **Published comments** (live on the video), **Held comments** (awaiting moderation), **Rejected Comments** (can be reversed).
- Once live, act on a message via its **Options (…)** menu: **Approve** (publishes to video) or **Reject** (removes; reversible). Other actions in the menu include Open Details, Reminders, Sentiment, Email, Suggest, Update Tags, Translate, Mark as Spam, Mark Secure, Preview on a Rule, Suggest/Request Approval as Post, and Create / Associate Cases.

### Ban YouTube users through Sprinklr
- Ban disruptive commenters without native YouTube admin access; keeps comment threads protected.
- Use a **Video Comments** or **Video Comment Replies** column, and set **Moderation Status = Held comments**.
  - **Hard requirement:** Ban Author is only available on comments/replies whose YouTube moderation status is **Held Comments**.
- Select the offending comment/reply, open the **Options (…)** menu, and choose **Ban Author** (sits just under Approve / Reject in the menu). This blocks that user from commenting on your videos.

### Grab YouTube live chat messages
- New **Chats** column type (last option in the Add New YouTube Column list) centralizes real-time live-chat messages from your streams.
- Pulls live-chat messages into the dashboard (shown as a "Live Chat" column) and tags them as a distinct **message type** for filtering, sentiment analysis and [[reporting]].
- **Read-only:** replying is **not supported** due to YouTube API limits. A Reply button shows on each message but is **disabled**, with a note: "We are working to bring the reply functionality to the livechat messages soon."

## Common issues & fixes
- **Ban Author missing / greyed out** → the comment is not in Held status. Ban only works on Held Comments; set the column's Moderation Status to Held comments and/or enable native YouTube comment approval.
- **No comments appear for moderation** → native YouTube isn't set to require approval, so comments publish directly instead of arriving as Held. Have the admin enable comment approval on the channel.
- **Can't reply to live-chat messages** → expected; live-chat is retrieval-only (API limitation). Use it for monitoring/sentiment/reporting only.
- **Older comments missing** → comments only go back 900 days and cap at 20,000; videos cap at 500.

## Notes & gaps
- Prerequisites: a connected YouTube account in Sprinklr; permission to add columns to an Engagement Dashboard; for moderation, native YouTube comment-approval enabled by the channel admin.
- Bans are managed from Sprinklr but enforced on YouTube; the article doesn't specify how to un-ban a user.
- Article doesn't state retention/refresh cadence for live-chat messages, nor whether bans sync if applied natively in YouTube.
- The Chats column preview in the help screenshot shows placeholder/loading content; exact in-message fields for live chat are not fully documented.

## Sources
- Create a Column for YouTube — https://www.sprinklr.com/help/articles/engage-with-messages-from-youtube/create-a-column-for-youtube/63ff4da87a695d65a1605947
- YouTube Comment Moderation — https://www.sprinklr.com/help/articles/engage-with-messages-from-youtube/youtube-comment-moderation/64113f4c2680c35a78bb4381
- Ban YouTube Users Through Sprinklr — https://www.sprinklr.com/help/articles/engage-with-messages-from-youtube/ban-youtube-users-through-sprinklr/6411417f2680c35a78bb43ab
- Grab YouTube Live Chat Messages — https://www.sprinklr.com/help/articles/engage-with-messages-from-youtube/grab-youtube-live-chat-messages/67973d3daa528e2b338fea06

Related: [[engagement-dashboards]] · [[rule-engine]] · [[reporting]] · [[publishing]]

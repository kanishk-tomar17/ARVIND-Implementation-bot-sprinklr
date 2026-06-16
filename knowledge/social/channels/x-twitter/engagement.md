# X — Engagement (Columns, Replies, DMs) (Sprinklr Social — X (formerly Twitter))
**Source:** sprinklr.com/help — X (formerly Twitter) channel (multiple articles; see links below)

## What it is
- How to monitor and respond to X (Twitter) activity inside Sprinklr [[engagement-dashboards]] — by building **columns** that pull specific X content (your posts, mentions, retweets, replies, DMs) and acting on it.
- Columns are added per dashboard; each column type maps to one kind of X content. Every column shares the same setup pattern (source → type → basic info → workflow/custom properties → create).
- Covers responding to comments (incl. converting a public reply into a private DM), sending/replying to DMs, automated welcome messages, previewing threads, following/blocking users, and auto-retweeting owned-account posts.
- Some automation (block, auto-retweet) is done in the [[rule-engine]], not in the dashboard itself.

## Key features & how to use

Common entry point for all columns: New Tab icon → **Sprinklr Social** → **Engagement Dashboards** (within Engage) → open the dashboard → **Add Column** (top-right) → search and select **X** as the source → pick the column **type**.

Column **type list** seen on the "Add New Twitter Column" screen: Inbox, Search, Persistent Search, Persistent Search With Filters, Received Direct Messages, Replies, Mentions, Retweets, My Tweets, Sent Direct Messages, Timeline, Filtered Timeline, Liked Tweets, Lists.

Common fields across column setup (right pane shows a **live Column Preview**): **Name**, **Description**, **Account(s)**, **Sponsored/Promoted Post** (All / Yes / No), **Default Date Range** (e.g. Lifetime), **Campaign**, **Sort** (Ascending/Descending), **Post Type**, **Minimum Likes / Replies / Retweets**, **Target Countries**, **Refresh Time**, plus **Workflow Properties** (Status, Assigned to, priority, Spam, sentiment) and **Custom Properties** (include/exclude rules). Finish with **Create Column** (bottom-right).

### My Tweets column (article 1)
- Add New X Column → select **My Tweets**.
- Enter Name, Description, Account(s). The **Promoted Post** filter: **Yes** (promoted only), **No** (non-promoted only), **All** (default).
- Configure Workflow Properties and Custom Properties → **Create Column**.
- To show full tweet text over 280 chars, enable the DP **TWITTER_SHOULD_CONSUME_TWEET_LONG_TEXT**.

### Mentions column (article 2)
- Add New X Column → select **Mentions**.
- Same basic fields, plus screenshot shows **Exclude Keywords** and **Keywords** fields, a **Show** filter (e.g. "All messages"), **Quoted Retweet** filter, and **View Conversation** link on each message.
- Long-text mentions over 280 chars require the same **TWITTER_SHOULD_CONSUME_TWEET_LONG_TEXT** DP.

### Retweets column (article 3)
- Add New X Column → select **Retweets**.
- Standard fields → Create Column.
- Permission note: **Repost (Retweet)** is its own permission (resharing). **Reply** is a separate permission. Editable retweets are classified as **reposts, not replies**.

### Replies column (article 4)
- Add New X Column → select **Replies**.
- Standard fields → Create Column. No special permissions/limits documented.

### Direct Messages columns (article 5)
- Two DM column types: **Received Direct Messages** (fans → your brand) and **Sent Direct Messages** (your brand → fans).
- Standard fields; preview pane shows DMs with **Read** ticks and media. Optional **Notify new Messages** checkbox and **Column Color**.
- Create Column to finish.

### Respond to X comments — public reply as private DM (article 6)
- Open a dashboard with X Comment columns → find the comment → click the **Reply** icon.
- In the reply window choose message type **Private Message** to respond privately instead of publicly.
- Add images, videos, links, text templates, custom links, content placeholders, emojis; set Campaign/properties; add notes.
- Optional **Schedule** icon → set date/time → **Apply**. Click **Send**.
- **"Enable Private Messaging"** checkbox controls whether you can receive DMs back from that account; respects the account's DM preference (followers only / everyone / none). Account switcher is disabled for DM replies.
- To view the private reply later: Engagement Dashboards → X Comment dashboard → find the profile → hover **Options** icon → **Open Details** → third pane → **Thread**.

### Send / reply to X Direct Messages (article 7)
- Build a **Received Direct Messages** column first.
- Reply: hover the private message → click the **Direct Message** icon → pop-up composer.
- Add images, videos, links, canned responses, custom links, content placeholders, feedback templates, emojis; select **Campaign** and message properties.
- Publish via **Post**, **Save as Draft**, or **Schedule** for later.
- Choose to respond from the **default brand handle** or the **handle that received the DM**.
- **Read** status = double ticks; live **Typing status** is shown when the user is replying.
- Requirement: target user must be a **follower of your brand's account**.
- Feature flags: **X_MESSAGE_READ_HANDLER_ENABLED**, **X_DM_PUBLISHING_ACCOUNT_SWITCHING_DISABLED**.

### X Welcome Messages (article 8)
- Auto-sends a message when a user starts a DM conversation with your account.
- Path: New Tab icon → Sprinklr Social → **Owned Social Accounts** (within Listen) → in Accounts (Settings), click **All Channels** to filter to X → find the X account → hover **Options** (three dots) → **Configure Your Messenger**.
- In Messenger Configuration: **Add Asset** (upload template via Media Uploader) → check **Enabled on X** (preview shows on right) → **Save**.

### Preview X Threads in Engagement Dashboards (article 9)
- Prerequisite: an **Outbound Column** of type **Sent**, **Scheduled**, or **Draft**.
- Only the latest message in a thread shows in the message cell.
- Find the draft/scheduled/published X Thread post → hover **Options** icon → **Preview** → click **Show This Thread** to open the **Third Pane** and see the full thread.

### Follow X users (article 10)
- Open an X Engagement Dashboard → click the user's **profile name** at the top of their message.
- Details pane shows tweet history, following count, and **followers** count.
- Click the number in **parentheses** above the Followers/Following label → opens **"Accounts Following [user]"** picker → select one or more of your linked accounts → click **Follow**.
- Reopen the same screen anytime to **unfollow** from specific accounts.

### Block X users (article 11)
- Done via the [[rule-engine]]: New Tab icon → Sprinklr Social → **Manage Rules** (within Triage).
- **Create New Rule** → set message conditions → add an action → scroll to **"Properties of the message sender"** → select **Block Profile** → **Save**.
- Blocked users cannot: add you to lists, follow you, see your profile picture, or tag you in photos.
- After blocking, Sprinklr stops fetching any further data from that profile; blocked profiles show a **diagonal watermark** in the platform.

### Auto-retweet posts from owned accounts (article 12)
- Done via the [[rule-engine]]: New Tab icon → **Governance Console → Rule Engine** (within Collaborate) → **Create New Rule**.
- Rule details: Rule Name (+ optional Description); **Rule Scope = Customer**; **Context = Case Update**; **Rule Type = On Demand**; set Activation Date / Rule Execution Batch → **Next**.
- Add Action (Addition icon → **Add Action**): Action Name; **Send Auto Respond To = X**; **Choose Account To Reply**; **Choose Campaign**; **Choose Preferred Reply = X Retweet**; choose Reply Template → **Save**.
- Screenshot confirms the Preferred Reply dropdown options: **Twitter Reply, Twitter Reply All, Twitter Quote, Twitter Retweet, Twitter Network**. A **Time Duration of Last Activity** condition (Greater than … Seconds) is also available, and an alternative **"Auto respond to a message using bot"** action exists.

## Common issues & fixes
- **Tweet/mention text cut off at 280 chars:** enable the **TWITTER_SHOULD_CONSUME_TWEET_LONG_TEXT** DP (My Tweets and Mentions columns).
- **Can't send/reply to a DM:** the recipient must be a **follower** of your brand's account; confirm **X_MESSAGE_READ_HANDLER_ENABLED** is on.
- **Account switcher greyed out on DM reply:** expected — switching is disabled (controlled by **X_DM_PUBLISHING_ACCOUNT_SWITCHING_DISABLED**); reply from the default or receiving handle.
- **No new data from a profile after blocking:** by design — blocking halts all further data fetch for that profile (shown with a diagonal watermark).
- **Thread shows only one tweet:** expected — open the post's third pane and click **Show This Thread**.

## Notes & gaps
- Prerequisites/permissions: **Reply** and **Repost (Retweet)** are distinct permissions; thread preview needs an outbound (Sent/Scheduled/Draft) column; block & auto-retweet require [[rule-engine]] access (Triage / Governance Console).
- DPs and feature flags (TWITTER_SHOULD_CONSUME_TWEET_LONG_TEXT, X_MESSAGE_READ_HANDLER_ENABLED, X_DM_PUBLISHING_ACCOUNT_SWITCHING_DISABLED) are partner/admin-controlled — raise with your Sprinklr contact if not enabled.
- Help text still uses legacy "Tweets / Retweets / Twitter Column" labels in UI even though the channel is branded **X**.
- Not specified in sources: exact rate limits on follows/DMs, max accounts selectable when following, and whether auto-retweet rules can be scheduled recurringly vs On Demand only.
- See also: [[publishing]] (composing/scheduling X posts), [[reporting]] (engagement metrics), [[asset-manager]] (templates/canned responses), [[engagement-dashboards]].

## Sources
- Create a Column for Tweets — https://www.sprinklr.com/help/articles/engage-with-your-fans/create-a-column-for-tweets/63f4ac6ee02459133724a68e
- Create a Column for X Mentions — https://www.sprinklr.com/help/articles/engage-with-your-fans/create-a-column-for-x-mentions/63f4afe59b334f7283b4d36c
- Create a Column for Retweets — https://www.sprinklr.com/help/articles/engage-with-your-fans/create-a-column-for-retweets/63f4aee5e02459133724a692
- Create a Column for X Replies — https://www.sprinklr.com/help/articles/engage-with-your-fans/create-a-column-for-x-replies/63f4aa279b334f7283b4d35c
- Create a Column for X Direct Messages — https://www.sprinklr.com/help/articles/engage-with-your-fans/create-a-column-for-x-direct-messages/63f4a8689b334f7283b4d355
- Respond to X Comments — https://www.sprinklr.com/help/articles/engage-with-your-fans/respond-to-x-comments/695e23fced1e4535a5fe44a6
- Send X Direct Messages — https://www.sprinklr.com/help/articles/engage-with-your-fans/send-x-direct-messages/63f4b4e1e02459133724a6a7
- X Welcome Messages — https://www.sprinklr.com/help/articles/engage-with-your-fans/x-welcome-messages/64008b5532d12b63c5f560a3
- Preview X Threads in Engagement Dashboards — https://www.sprinklr.com/help/articles/engage-with-your-fans/preview-x-threads-in-engagement-dashboards/64555dad0104980882a54951
- Follow X Users — https://www.sprinklr.com/help/articles/engage-with-your-fans/follow-x-users/64008d577a695d65a1605ca5
- Block X Users — https://www.sprinklr.com/help/articles/engage-with-your-fans/block-x-users/64008c3c7a695d65a1605c9b
- Auto-retweet X Posts from Desired Owned Accounts — https://www.sprinklr.com/help/articles/engage-with-your-fans/autoretweet-x-posts-from-desired-owned-accounts/64ec86435d8ee56e364cb426

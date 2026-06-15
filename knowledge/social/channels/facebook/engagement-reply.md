# Facebook — Replying & Engaging (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- How agents reply to and moderate Facebook from Sprinklr [[engagement-dashboards]] (and the Care/Agent Console): comments, Messenger DMs, edits, blocks.
- Covers the Facebook/Meta Messenger reply windows and message-tag policy that govern when you're allowed to send a DM.
- Includes requesting conversation control back from an external bot before you can reply, and using the [[rule-engine]] to flag external mentions of the brand.
- All actions are permission-gated at the account/channel and role level — agents need the right Channel Permissions and Publishing/role permissions.

## Key features & how to use

### Respond to Facebook comments (reply as a private message)
- Go to **Engagement Dashboards** (Sprinklr Social > **Engage**), find the Facebook comment, click the **Reply** icon.
- Set message type to **Private Message** (replies to a public comment as a DM to that user).
- Composer supports: **Image, Video, Link, Text Template, Custom Link, Content Placeholder, Emojis**. Optional: set **Campaign**, add **properties**, attach **notes**, or **Schedule** the message (Schedule icon).
- Click **Send** (bottom-right of the Private Message composer).
- To find the conversation later: in Engagement Dashboards, hover the customer profile > **Options** icon > **Open Details** > in the **Third Pane** select **Thread** to see the DM exchange.

### Send direct messages through Facebook Messenger
- **Via Engagement Dashboards:** Engage > Engagement Dashboards > **Add Column** (top right) > **Facebook** > **Messenger**. Hover a message to reveal action icons, click the **Private Message** icon, compose (attach media if needed), set **Campaign** and message properties, then **Send**, **Save as Draft**, or **Schedule Post**.
- **Via Agent Console:** Sprinklr Service > **Resolve** > **Agent Console**. Use the **Collapse Window** icon to add a new column, select the message, click **Write a Reply**, compose (media optional).
- **Delivery indicators (seen in UI):** a **double-tick** next to your reply — **gray** = sent, **blue** = delivered/seen.
- Limits: brands **cannot initiate** conversations (reply-only); photos/videos render inline only for users who started via the Messenger app; media sent after the 24-hour window appears as a **link**, not inline.

### Facebook platform policy for replying to DMs (Meta Messenger windows)
- Standard guidance: respond within **24 hours**. Promotional content allowed inside standard messaging / sponsored messages.
- **Message tags** let you send important, non-promotional 1:1 updates **outside** the 24-hour window. Tags **may not** be used for promotions (deals, offers, coupons, discounts).
- **HUMAN_AGENT tag:** lets a human agent reply up to **7 days** after the user's last message (for issues needing >24h, weekends, closures). No automated messages and nothing unrelated to the user's inquiry. Use only for genuine cases — Meta monitors for misuse.
- Enforcement: warning when you cross 24h; sending is **blocked after 7 days** (per Meta Data Policy). Each new user reply refreshes the window.
- **Dynamic Property (DP) behaviour:** DP **enabled** = upfront block notification before you can send past the window; DP **disabled** = two-stage warnings appear before delivery is blocked.

### Request control to reply to Messenger DMs
- When an external bot owns the thread, Facebook policy blocks your reply. The Facebook column shows a banner: **"Control is not with you. You can request for it."**
- Click the conversation's **Options** (•••) icon > **Request control** (the same menu also offers **Revoke control**, Open Details, Reminders, Sentiment, Email, Suggest, Update Tags, Translate).
- In the **Request Control** dialog, add a **Comment** (e.g. "Asking for access.") and click **Request**.
- The external bot decides. On approval a system message appears: **"[INTERNAL] Conversation control has been passed to you."** — only then can you reply.
- If you try to send without control, the publisher shows a warning that the message failed (no thread ownership).

### Edit published comments and replies (Engagement column)
- Engage > **Engagement Dashboards**, open a **Facebook Comments** or **Replies** column, find the brand's published comment/reply.
- Hover the action (•••) icon at lower-right > **Edit**. (The action menu also has Like, Like from multiple accounts, Delete, Open Details, Reminders, Sentiment, Email, Suggest, Create Canned Response, Update Tags, Translate, Mark as Spam, Preview on a Rule, Create Case.)
- The item opens in the **Publisher**; make changes and click **Post**. Edits sync to Sprinklr and **natively on Facebook** — no delete needed, engagement is preserved.
- **Edit appears only for the brand's own published messages** (not user content).

### Block / unblock Facebook users
- A blocked user **cannot post, comment, like, or share** on your Facebook page.
- Engage > **Engagement Dashboards** > pick the dashboard via the **Dashboard Menu** icon (top left).
- Hover the **Profile Name** > in the profile pop-up hover the **Options** (•••) icon (bottom-right) > **Block** (the pop-up also shows **View Details** and **Apply Macro / Refresh**).
- To reverse: same path > **Unblock**.
- You **cannot take action on a blocked user's messages**.

### Identify Facebook external mentions (Rule Engine)
- "External mentions" = brand mentions posted on other profiles/pages, not on the brand's own wall. Flag them with a [[rule-engine]] rule.
- Sprinklr Social > new tab > **Manage Rules** (under **Triage**) > **Create New Rule** (top right).
- Enter **Name** + **Description**, set context to **Inbound**, optionally adjust **Activation Date** / **Rule Execution Batch**, click **Next**.
- In **Rule Builder**: add icon > **Add Condition** > **Is Mention on External Source** = **Yes** (or No).
- On the Yes/No branch: add icon > **Add Action** (e.g. queue/user assignment, tagging).
- Click **Save** (or **Save as Draft**). Then surface results with a workflow column (see "WorkFlow Column Using Rule Engine").

## Common issues & fixes
- **Can't reply to a Messenger DM / message fails:** thread control is with an external bot — use **Request control** and wait for approval.
- **Send blocked / warned on a DM:** you're outside Meta's 24h window; needs **HUMAN_AGENT** tag (valid to 7 days). After 7 days sending is hard-blocked.
- **Media sent as a link, not inline:** message was sent after the 24-hour window, or the user didn't start via the Messenger app.
- **No Edit option on a comment:** Edit only shows for the brand's own published comments/replies and requires the permissions below.
- **Can't block / edit:** missing role permission (block permission, or "Edit Sent Post").

## Notes & gaps
- **Permissions:** commenting/DM engagement needs account-level **Channel Permissions** to the Facebook Page. Editing needs the **"Edit Sent Post"** role-level Publishing permission plus account-level publishing permission to the Page. Blocking needs **block permission** under Roles & Permissions.
- Reply-as-DM, edit, and block all act natively on Facebook via the connected account — they are not Sprinklr-only.
- Gaps: articles don't list exact supported media file types/sizes, or where the HUMAN_AGENT tag is toggled in the composer; sponsored-message setup is out of scope here. See [[publishing]] for composer details and [[asset-manager]] for media. Related: [[reporting]] for engagement metrics.

## Sources
- Respond to Facebook Comments — https://www.sprinklr.com/help/articles/reply-from-engagement-dashboards/respond-to-facebook-comments/63ec48a0f6e2cc7d18f9e905
- Send Direct Messages Through Facebook Messenger — https://www.sprinklr.com/help/articles/reply-from-engagement-dashboards/send-direct-messages-through-facebook-messenger/63ec4aacef1b447d6c6237f7
- Facebook Platform Policy for Replying to Direct Messages — https://www.sprinklr.com/help/articles/reply-from-engagement-dashboards/facebook-platform-policy-for-replying-to-direct-messages/63eb9947ef1b447d6c61e4b8
- Request Control to Reply to Messenger DMs — https://www.sprinklr.com/help/articles/reply-from-engagement-dashboards/request-control-to-reply-to-messenger-dms/63ecd51ff6e2cc7d18fabaa8
- Edit Published Comments and Replies using Engagement Column — https://www.sprinklr.com/help/articles/reply-from-engagement-dashboards/edit-published-comments-and-replies-using-engagement-column/63e9d1beef1b447d6c61b213
- Block/Unblock Facebook Users using Engagement Dashboards — https://www.sprinklr.com/help/articles/reply-from-engagement-dashboards/blockunblock-facebook-users-using-engagement-dashboards/63ea6a96ef1b447d6c61b35d
- Identify Facebook External Mentions using Rule Engine — https://www.sprinklr.com/help/articles/reply-from-engagement-dashboards/identify-facebook-external-mentions-using-rule-engine/63ecd6b7ef1b447d6c63072b

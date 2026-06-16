# Instagram — Replying & Comment Moderation (Sprinklr Social — Instagram)
**Source:** sprinklr.com/help — Instagram channel (multiple articles; see links below)

## What it is
- How to reply to and moderate Instagram comments inside Sprinklr's [[engagement-dashboards]].
- Two reply modes from a comment: a public **threaded reply** on the comment, or a private **Direct Message** to the commenter.
- Moderation actions on a comment: **Hide**, **Unhide**, **Disable Comments**, **Enable Comments** — all run as native channel actions on Instagram.
- A [[rule-engine]] recipe to capture and triage comments on Instagram **Live** videos.
- Meta's messaging-window policy (24-hour / 7-day rules, HUMAN_AGENT tag) that governs how and when you can DM users.

## Key features & how to use

### Reply to an Instagram comment as a Direct Message
Send a private DM to someone who commented publicly on a post.
- Open **New Tab icon → Sprinklr Social → Engage → Engagement Dashboards**.
- Top-left dropdown: pick a dashboard that has Instagram comment columns (column header reads e.g. "Instagram Comments (8)").
- Find the comment; click the **Reply icon** (left-arrow ↩ in the action bar below the message — tooltip "Reply").
- In the Reply window, change **Message Type** to **Direct Message**.
- Compose the reply. Composer supports images, videos, links, text templates, custom links, content placeholders, and emojis.
- Set campaign and other message properties; add notes if needed.
- Optional: click the **Schedule** icon (lower left) to schedule, then **Apply**.
- Click **Save as Draft** or **Send** (bottom right).
- Note: DMs are bound by Meta's messaging windows — see the policy section below.

### Reply to an Instagram comment as a threaded (public) response
Post a public reply that threads under the original comment.
- Same path: **Engagement Dashboards** → pick the dashboard with the Instagram comment/reply column.
- Find the comment; click the **Reply icon** at the bottom of the message card.
- In the Reply screen set **Message Type = Reply**, write your response.
- Click **Send** (bottom right of the composer) to publish.
- GIF limitation: GIF comments show **"This message has unsupported media type"** because Instagram's API doesn't capture GIF media. Click the message **date** to open the comment natively and act there.

### Hide / Unhide an Instagram comment
Hides spam or inappropriate comments from the post's native feed.
- In an Instagram comment column, hover over the comment's **options (…) menu** icon and select **Hide**.
- A hidden comment shows a **crossed-out eye symbol** (top-right of the card) confirming it's hidden from native.
- The same menu toggles back to **Unhide** to restore the comment.

### Disable / Enable comments on a post
Turns off (or back on) the ability to comment on a whole Instagram post.
- Prereq: a new or existing Engagement Dashboard with a **Media** column (you can name it "Instagram Comments" for clarity).
- Find the post in the column; open the **options (…) menu** at the bottom of the card.
- The menu's **Channel Actions** section (top of the list) shows **Disable Comments** — click it to disable commenting on that post.
- It's a toggle: once disabled, the same button reads **Enable Comments** to switch back.
- Distinct from Hide: Disable applies to the entire post's comment thread; Hide applies to one individual comment.
- (Release 26.4.)

### Capture comments on Instagram Live videos (Rule Engine)
View and triage all comments on an Instagram Live in the Engagement Dashboard via a [[rule-engine]] rule.
- Hard limit: **you can only reply to Live comments while the video is still live.**
- Open **New Tab icon → Sprinklr Social → Triage → Manage Rules**.
- Click **Create New Rule** (top right).
- Enter a name and description; set **Context = Inbound**. Optionally adjust Activation Date and Rule Execution Batch; proceed.
- Add four **conditions** (via the add-condition icon):
  - Channel = **Instagram**
  - Message Type = **Instagram Comments**
  - Message Subtype = **Live Comment**
  - Account = (the desired account)
- Add **actions** on the Yes/No branches as needed (e.g. route, tag, assign).
- Click **Save** (or **Save as Draft**).

### Meta platform policy for replying to Direct Messages
Governs the timing rules Sprinklr enforces when you DM Instagram users.
- **24-hour window:** respond within 24 hours of the user's message. After that, a warning shows: *"24 hours have passed since the last message from this social profile. As per messenger policy, your message should only be in response to customer enquiry."*
- **7-day block:** after 7 days the conversation is blocked per Meta's Data Policy.
- **HUMAN_AGENT tag:** lets a human agent respond up to **7 days** after the user's message. Sprinklr applies this tag automatically from the backend when a human agent replies outside the standard window.
- **Allowed with the tag:** human support for issues taking >24 hours to resolve; support when the business is closed.
- **Prohibited:** automated messages, content unrelated to the user's inquiry, and any promotional messaging (deals, offers, coupons, discounts) via message tags.

## Common issues & fixes
- **GIF comment shows "This message has unsupported media type":** Instagram API doesn't capture GIFs — click the message date to open and act natively.
- **Can't reply to a Live comment:** replies only work while the video is live; once the stream ends the window closes.
- **DM blocked / 24-hour warning:** you're outside Meta's messaging window. Within 7 days a human-agent reply is allowed (HUMAN_AGENT tag, auto-applied); after 7 days the conversation is blocked. Never send promo content via tags.

## Notes & gaps
- Prerequisites throughout: access to Sprinklr Social, an Engagement Dashboard with the appropriate Instagram comment/media column, and permission to manage comments and (for the Live workflow) to create rules in the [[rule-engine]].
- Hide vs Disable: Hide targets a single comment; Disable Comments targets the whole post. Both are native channel actions pushed to Instagram.
- Articles don't specify exact role/permission names required for moderation actions.
- The DM policy reflects Meta's platform rules and may change on Meta's side; Sprinklr enforces the current windows automatically.
- Related: [[publishing]], [[reporting]], [[facebook]] (similar Meta messaging-window rules apply).

## Sources
- Responding To Instagram Comments As Direct Messages — https://www.sprinklr.com/help/articles/reply-to-messages/responding-to-instagram-comments-as-direct-messages/63e4b67fa9d51179030176dd
- Replying to Instagram Comments as a Threaded Response — https://www.sprinklr.com/help/articles/reply-to-messages/replying-to-instagram-comments-as-a-threaded-response/63ec7289ef1b447d6c6272c9
- Hide Instagram Comments — https://www.sprinklr.com/help/articles/reply-to-messages/hide-instagram-comments/63e4b20da9d51179030176d3
- Disable Instagram Comments — https://www.sprinklr.com/help/articles/reply-to-messages/disable-instagram-comments/69c3de633d2bda6aa7478068
- Capture Comments On Instagram Live Videos Using Rule Engine — https://www.sprinklr.com/help/articles/reply-to-messages/capture-comments-on-instagram-live-videos-using-rule-engine/63ec733cf6e2cc7d18fa2518
- Meta Platform Policy for Replying to Direct Messages — https://www.sprinklr.com/help/articles/reply-to-messages/meta-platform-policy-for-replying-to-direct-messages/674557f592765f31c82d4c59

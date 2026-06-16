# X — Publishing Posts (Sprinklr Social — X (formerly Twitter))
**Source:** sprinklr.com/help — X (formerly Twitter) channel (multiple articles; see links below)

## What it is
- How to compose and publish to an X account from the Sprinklr Publisher: standard posts, video posts, threads, quote tweets, polls, and organic (website) cards.
- All X publishing happens in the **Create Post** window, opened from the **Publisher** / **Quick Publish** icon in the top navigation bar.
- Compliance rule across every flow: **only one X account can be selected at a time** in the Publisher (X policy). You cannot bulk-publish to multiple X handles in a single post.
- Right-hand pane gives a live mobile/desktop preview as you build the post.
- Common footer controls on every flow: **Schedule Post**, **Publish Another** (checkbox), **Save as Draft**, and **Post**.

## Key features & how to use

### Create an X (Twitter) post
- Open **Publisher** icon (top nav) > **Create Post**.
- **Select Accounts** field: search and pick one X account. Pin frequently-used accounts for speed. (Advanced Search link is top-right of the field.)
- **Message** box: type your text. Live **character counter** + circular fill indicator sits bottom-right of the box; an emoji picker is beside it.
  - Standard limit: **280 characters**.
  - **Long Tweet** support lets you exceed 280 (links auto-wrap). Extended limits: **10,000 characters** (needs a client property enabled) or **25,000 characters** (X Premium accounts). Exceeding the cap shows a red "Message exceeds the limit of N characters for X" banner and blocks posting.
- **@mention**: type "@" then the account name.
- **Insert** icon adds rich objects: **X Cards, Custom Links, Content Placeholders, YouTube Video, Link, Text Template**.
- **Photo / Video** radio toggle. Under Photo: **Select Photo** (from library/DAM) or **Upload Photo** from device; **Add Another Photo** for multi-image.
  - **Alt text**: "Write alt text here…" field per image, **max 1000 characters**. Not available for GIFs/videos.
  - **Tag Users**: type a handle (e.g. "shivam_sunday") and tick accounts from the suggestion list (only if the recipient has photo tagging enabled).
- Publishing options: **Who can reply** (reply restriction dropdown), **Dark Post** checkbox, **Enable Private Messaging** checkbox, **Campaign** (+ **Set as Default**) and **Sub-Campaign**, **Tags**, **Social Bars**, **URL Shortener**, **Generate Web Analytics Links**.
- **Approval Type** + approval notes where an approval workflow applies.
- Publish now (**Post**), **Save as Draft**, or **Schedule Post** (pick date/time). Tick **Publish Another** to keep composing after posting.

### Create an X video post
- Same Create Post entry; **Select Accounts** = single X account.
- Set **Type of Message** = **Message** (or Thread); toggle the **Video** radio under the content area.
- Add video via **Media Uploader / Digital Asset Manager** or upload from device.
- **Captions**: click **Add Caption** in the video preview > pick **language** from dropdown > upload in **SRT** format > keep **≤109 characters per subtitle group** > save.
- **Change Thumbnail** (requires the **Update Thumbnail** permission — found under Role Permissions > Publishing > Outbound Execution): works on **MP4 and MOV** files; choose from pre-populated images, DAM, device upload, or a frame of the video.
- **Video Title** (max **70 characters**) and **Description** (max **200 characters**); emoji picker available.
- Checkboxes: **Option to allow playback in embedded tweets**, **Monetize this Video**.
- **Geo-restrictions** (required): **None / Include / Exclude**.
- **Who can reply** dropdown (default "Everyone"; anyone mentioned can always reply). **Enable Private Messaging** adds a CTA button. **Publish this post as Dark Post** checkbox.
- Then Campaign/Sub-Campaign, Tags, Social Bars, URL Shortener, Approval Type/notes.
- **Post** / **Save as Draft** / **Schedule Post**; **Publish Another** to continue.
- Tip banner: "When your media is ready to go, you can **pre-upload** media to X to prevent a delay in posting."

### Publish a threaded tweet
- Create Post > single X account > set **Type of Message** = **Thread**.
- Compose **Tweet 1** (Message box + full functionality: text, **Photo/Video**, GIF, alt text, **Add Another Photo**).
- **Add Another Tweet** button appends the next tweet; default ceiling **25 tweets** (raising above default needs additional setup + success-manager / DP enablement).
- Each tweet has its own **Schedule** button (top-right of that tweet block) for staggered timing — later tweets must schedule after earlier ones. Or schedule the whole thread via the footer **Schedule Post**.
- Delete a tweet with its **Delete** icon. **Who can reply** applies to the thread.
- Video tweets inside a thread **cannot** use monetization, embedded-playback, or geo-restriction options.
- The **entire thread submits as one entity** for approval. You **cannot add tweets after publishing**. Completed threads can be **cloned** from the outbound column.
- Use for: linking a tutorial/article to business context, extending character limits (T&Cs, further reading), event reminders.

### Publish quote tweets
- Quote tweets start from an engagement column, not the blank Publisher.
- **New Tab** > **Sprinklr Social > Engagement Dashboards** (under Engage).
- Open the **Dashboard Menu** (top-left) and pick your engagement dashboard.
- **Add Column** > search/select **X** as source > choose column type (Inbox, Search, Persistence Search, Persistence Search with Filters, Replies, Mentions, Retweets, My Tweets, Timeline, Filtered Timeline, Liked Tweets).
- Fill **Name, Description, Accounts**; set **Workflow Properties** (status, assignment, priority, spam, sentiment); add **Custom Properties** to filter; **Create Column**.
- On a tweet in that column: hover the **Options** icon > **Quote Tweet**.
- Create Post opens with **Select Account** pre-populated; pick **Type of Message**; write your comment in the **Message** box; optionally add media; finish and **Post**.
- Single account only (X compliance).

### Create an X poll on Sprinklr
- Create Post > single X account > **Type of Message** = Message or Thread.
- Type the poll question in the **Message** box, then select the **Poll** radio (sits alongside **Photo** and **Video**).
- **Poll options**: enter answers, **max 25 characters each**; use the **Add** icon to add options up to a **maximum of 4**.
- **Poll Duration**: set **Days / Hours / Minutes** via dropdowns.
- **Who can reply** dropdown; **Dark Post** checkbox; **Enable Private Messaging** checkbox (adds CTA button).
- Campaign / Sub-Campaign, Social Bars, URL Shortener, Approval Type + notes.
- **Post** / **Save as Draft** / **Schedule Post**; **Publish Another** to continue.
- Votes are anonymous/private.

### Publish X organic cards
- **Prerequisites**: an **X Ad Account** enabled and added to Sprinklr with its handle connected, and a **Twitter/X Card** already created under **[[asset-manager]]**.
- **Quick Publish** icon > **Create Post** > select X account > write **Message** (@mention by typing "@"). Circular indicator fills blue toward the character limit.
- **Insert** icon > **Add X Cards** to attach the card. You **cannot add a photo or video at the same time** as a card.
- Engagement: **Who can reply** dropdown, **Dark Post** checkbox, **Enable Private Messaging** checkbox.
- **Enable Twitter Card Tracking** toggle: turning it on reveals a **Web Analytics** field (required) — pick a **Web Analytics Profile** (e.g. Webanalytics0511, Advocacy, joeyWebAnalytics) to track clicks.
- Campaign/Sub-Campaign, Tags, Social Bars, URL Shortener, Approval Type + notes.
- Publish now (**Post**), **Save as Draft**, or **Schedule Post** (month/date/time). **Publish Another** to continue.

## Common issues & fixes
- **"Message exceeds the limit of N characters for X"** (red banner) — over the cap. Trim text, or enable the 10,000-char client property / use an X Premium handle for higher limits.
- **Can't select a second X account** — by design (X compliance). Publish per handle.
- **Change Thumbnail greyed out / missing** — needs the **Update Thumbnail** permission (Role Permissions > Publishing > Outbound Execution) and an MP4/MOV file.
- **Can't add photo/video on an organic card post** — cards are mutually exclusive with photo/video media.
- **Can't add tweets after a thread publishes** — threads are immutable post-publish; clone instead.
- **Captions rejected** — must be SRT and ≤109 characters per subtitle group.

## Notes & gaps
- Prerequisites: a connected X account (and, for organic cards, an X Ad Account + a pre-built Card asset).
- Permissions referenced: **Update Thumbnail** for video thumbnails; approval-workflow permissions where approvals are configured. Other per-action permissions (e.g. Create Post, Publish, Create Draft) live in Outbound Execution but the articles don't map each flow to a specific permission.
- The 10,000-char Long Tweet limit depends on an unspecified **client property**; 25,000 requires **X Premium** — neither article names the exact property toggle.
- Raising the thread cap above 25 needs success-manager / DP-controlled enablement; exact request path unspecified.
- Articles don't detail GIF-specific limits, file-size caps, or supported video codecs beyond MP4/MOV for thumbnails.
- Related: [[publishing]], [[asset-manager]], [[engagement-dashboards]], [[rule-engine]], [[reporting]].

## Sources
- Create an X (formerly Twitter) post — https://www.sprinklr.com/help/articles/publish-to-an-x-account/create-an-x-formerly-twitter-post/63f8cf51e02459133724b19b
- Create an X video post — https://www.sprinklr.com/help/articles/publish-to-an-x-account/create-an-x-video-post/63f4b97ce02459133724a6b3
- Publish a threaded tweet — https://www.sprinklr.com/help/articles/publish-to-an-x-account/publish-a-threaded-tweet/63f8d1fd9b334f7283b4dd60
- Publish quote tweets — https://www.sprinklr.com/help/articles/publish-to-an-x-account/publish-quote-tweets/63f8d34ae02459133724b1a4
- Create an X poll on Sprinklr — https://www.sprinklr.com/help/articles/publish-to-an-x-account/create-an-x-poll-on-sprinklr/65d48f17fc36e1761199972b
- Publish X organic cards — https://www.sprinklr.com/help/articles/publish-to-an-x-account/publish-x-organic-cards/63f8d5059b334f7283b4dd68

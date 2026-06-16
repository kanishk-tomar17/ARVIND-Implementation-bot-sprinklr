# LINE (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — LINE channel (multiple articles; see links below)

## What it is
- LINE is a mobile-first messaging app (text, images, video, audio). Sprinklr integrates with it via the **LINE Business Connect API**, supporting **LINE Official Accounts** (with Business Connect enabled) and **LINE Business Connect Accounts**.
- Lets brands publish messages (text/photo/video/audio, image maps, broadcasts), engage inbound DMs through [[engagement-dashboards]] workflows, automate welcome messages and rich menus, and report on message/follower metrics.
- Supports message **templates** (Card, Confirm, Carousel, Image Carousel), **quick replies**, and **custom rich menus** as reusable assets.
- **API limitations — NOT supported:** publishing stickers, timeline photo updates, rich image / rich video publishing, image customization, and **editing a post after it is published**.

## Key features & how to use

### Setup — Welcome message
Automated greeting sent when a customer first DMs the LINE account; sets the tone and surfaces service options without manual effort.
- **Prerequisite:** first create a message template using **Asset Manager** (Asset Manager > create the welcome asset).
- Path: New Tab icon (Sprinklr Social) > **Listen > Owned Social Accounts**.
- In **Accounts (Settings)**, click the **All Channels** filter and select **LINE** to show only LINE accounts.
- On the target account, hover the **Options** (three-dot) icon and choose **Configure Your Messenger**.
- Click **Add Asset** to upload the prepared template via the **Media Uploader**; preview renders in the right pane.
- Click **Save** (bottom right) to activate. Reports as **LINE Welcome Message Count** (Greeting Messages).

### Setup — Custom rich menu
A customizable menu shown on the chat screen. Three parts: an **image**, **tappable areas** (up to **20**), and a **chat bar** to open/close it.
- Path: New Tab icon > **Listen > Owned Social Accounts** > Accounts (Settings) > filter **All Channels = LINE**.
- On the account, hover **Options** (three-dot) icon > **Custom Rich Menu**. (Same Options menu also has: Details, Edit, Web Analytics, Configure Your Messenger, Activity, Deactivate, Remove Account.)
- In the **LINE Rich Menu Library** window, click **Add Rich Menu**.
- In **LINE Rich Menu Configuration**, set:
  - **Rich Menu Name** (identifier), **Menu Bar Label** (`Menu` or custom text), **Default Behaviour** (`Shown` or `Collapsed`).
  - **Target Audience:** Gender, Language, Client Profile Lists, Partner Profile Lists.
  - **Rich Menu Content:** pick a **Menu Template** from the dropdown; **Upload Image** (JPEG or PNG only; recommended **2,500 x 1,686 px**); set an **Action Type** per tappable area = **No action**, **Link**, or **Text**.
- Click **Save**. (Max **20** tappable areas per menu.)

### Publishing
Publish text, photo, video, audio, and image maps; schedule, target audiences, attach campaigns. See [[publishing]].
- Path: **Engage > Quick Publish**.
- Select a **LINE account** and a **message type**, then fill its fields:
  - **Text:** message content; supports custom links, placeholders, templates, videos, and emoji picker.
  - **Photo:** title, photo (select/upload), description.
  - **Video:** video (select/upload), title, description.
  - **Audio:** audio file (select/upload).
  - **Image Map:** grid type, image, descriptions, section labels, section types, and per-section text/URLs.
- Optionally enable **Broadcast** messaging.
- **Target Audience:** choose **Select from Saved Target Audiences** (table shows Name, Audience Id, Reach, dates, Age, Gender, Country) or **Create new Audience**; new audiences filter by **Gender** (Male/Female), **Language**, **Client Profile Lists**, **Partner Profile Lists**. Confirm with **Add Selected**.
- Associate a **Campaign**, optionally apply a **URL shortener**, set **approval** requirements.
- **Preview**, then **Publish now**, **Save as draft**, or **Schedule**. Can queue additional posts.
- Note: posts **cannot be edited after publishing** (API limit).

### Publishing assets — Template messages
Predefined, customizable layouts. Four types: **Card, Confirm, Carousel, Image Carousel**.
- Path: New Tab icon > **Engage > Assets**. Top right: **Add Asset > Add Omni Chat Templates**.
- Enter **Name** + optional **Description**.
- Under **Asset Specific**, set **Template Type** (Card / Confirm / Carousel / Image Carousel) and **Channel = Line** (the channel dropdown also lists Google RBM, Sprinklr Live Chat, Google Business Messaging).
- Configure **Asset Details** (campaigns, sub-campaigns, status, Available/Visible/Expires dates, tags, brands, persona, etc.) and **Sharing** (Workspaces + Users/User Groups, or check **Visible in all workspaces**).
- Type-specific fields:
  - **Card:** image (aspect ratio/sizing), title, description, default action, and multiple action buttons.
  - **Confirm:** title, alt text, two action buttons.
  - **Carousel:** multiple card elements (image, title, description, action buttons).
  - **Image Carousel:** sequential images with one action button per image.
- Click **Save**.

### Publishing assets — Quick replies
Buttons shown at the bottom of the LINE chat screen so recipients tap instead of typing.
- **Actions available** — LINE-exclusive: **Open Camera**, **Open Camera Roll**, **Share Location**. Common: **Postback Event**, **Send Message**, **Open URL**, **Create Date Picker**.
- Path: New Tab icon > **Engage > Assets** > **Add Asset > Omni Chat Templates**.
- Set **Template Type = Quick Reply** and **Channel = Line** (under **Asset Specific**); a **Quick Replies** section appears.
- Per button: **Name** (button element title), optional **Upload Icon** (via DAM, Media Valet, or new upload), **Label** (button text), and **Action**:
  - **Create Date Picker:** Mode (Date or Date/Time), Start Time, End Time.
  - **Open URL:** URL field.
  - **Postback Event:** Display Text.
  - **Send Message:** Message text.
  - **Open Camera / Open Camera Roll / Share Location:** Label only.
- Configure Asset Details + Sharing, then **Save**.

### Engagement — create a LINE column
Manage inbound LINE messages in [[engagement-dashboards]] with workflow routing, prioritization, and replies.
- Path: New Tab icon > **Sprinklr Social > Engage > Engagement Dashboards**.
- Click **Add Column** (top right) > select **LINE** in the **Add New Column** window (searchable).
- In **Add New LINE Column**, choose a **Column Type** — **Inbox** is the available type. Preview renders in the right pane.
- Fill **Basic** info; set **Workflow Properties** (message workflow status, user assignment, priority, Spam, sentiment); add **Custom Properties** to filter messages by attributes.
- Click **Create Column**. Column is immediately usable.
- Engagement supports: text/photo/video/audio replies, quick-reply buttons + emoji, broadcast and reply messages, image maps, scheduled/targeted posts, ad-campaign and friend-acquisition tracking. (Same API limits apply — no stickers, timeline photos, rich image/video, image customization, or post editing.)

### Reporting — LINE metrics
Available in [[reporting]] dashboards. See [[reporting]].
- **Volume of LINE Brand Initiated Conversations** — conversations started by the brand.
- **Volume of LINE Brand Replies** — brand replies to a message.
- **LINE Message Broadcast** — number of Broadcast Messages sent.
- **LINE Account Blocked Count** — users who blocked the LINE Official Account.
- **LINE Account Followers** — total followers (users who added the account as a friend).
- **LINE Auto Response Messages Count** — auto-response messages sent via LINE Official Account Manager.
- **LINE Broadcast Message Count** — total broadcast messages sent on a given day.
- **LINE Broadcast Message Count via Sprinklr** — broadcasts sent through Sprinklr.
- **LINE Chat Screen Message Count** — messages sent from the LINE Official Account Manager Chat screen.
- **LINE Media Unique Played** — unique users who started playing any video/audio in the message.
- **LINE Media Unique Played 100%** — users who played the entirety of any video/audio.
- **LINE Message Delivered** — messages delivered.
- **LINE Message Unique Clicks** — unique users who opened any URL in the message.
- **LINE Message Unique Impressions** — users who opened the message (displayed at least 1 bubble).
- **LINE Multicast Messages Count via Sprinklr** — Multicast Messages sent through Sprinklr.
- **LINE Narrowcast Messages Count via Sprinklr** — Narrowcast Messages sent through Sprinklr.
- **LINE Push Messages Count via Sprinklr** — Push Messages sent through Sprinklr.
- **LINE Reachable Targets** — users the account can reach via targeted messages.
- **LINE Reply Message Count via Sprinklr** — replies sent through Sprinklr.
- **LINE Targeted Messages Count** — targeted messages sent.
- **LINE Welcome Message Count** — Greeting Messages sent.
- **LINE Message Multicast / Push / Reply** — counts of Multicast, Push, and Reply messages sent.

## Common issues & fixes
- **Can't edit a published post** — not possible; LINE API does not support post editing. Delete/republish instead.
- **Stickers / timeline photos / rich image / rich video won't publish** — unsupported by the LINE Business Connect API; use supported message types (text, photo, video, audio, image map, templates).
- **No image customization** — not available; prepare media before upload.
- **Welcome message not sending** — confirm the welcome template was created in Asset Manager first, then attached via **Configure Your Messenger > Add Asset** and saved.
- **Rich menu image rejected** — must be JPEG or PNG; recommended size 2,500 x 1,686 px; max 20 tappable areas.

## Notes & gaps
- **Account types:** LINE Official Account (with Business Connect) or LINE Business Connect Account; integration runs on the LINE Business Connect API.
- **Prerequisites:** templates/quick replies/welcome assets are built in **Asset Manager (Omni Chat Templates)** before use; welcome message and rich menu are configured per account under **Listen > Owned Social Accounts**.
- **Permissions:** asset visibility is controlled via Workspaces and User/User-Group sharing.
- **Gaps:** help articles do **not** specify character/size limits for text or media, image-map dimension specs, broadcast audience caps, or the full set of available rich-menu **Menu Template** layouts. Engagement column type observed = **Inbox** only. See [[rule-engine]] for routing/assignment of LINE cases.

## Sources
- LINE Capabilities and Limitations — https://www.sprinklr.com/help/articles/line/line-capabilities-and-limitations/64561e410104980882a56c29
- LINE Publishing — https://www.sprinklr.com/help/articles/line/line-publishing/64561ceee66f2e36b4514bd9
- How to Create an Engagement Column for LINE — https://www.sprinklr.com/help/articles/line/how-to-create-an-engagement-column-for-line/6456222ce66f2e36b4514bfb
- LINE Engagement and Limitations — https://www.sprinklr.com/help/articles/line/line-engagement-and-limitations/64561d6f0104980882a56c19
- LINE Welcome Message — https://www.sprinklr.com/help/articles/line/line-welcome-message/64561d9be66f2e36b4514bea
- Create Quick Replies for LINE — https://www.sprinklr.com/help/articles/line/create-quick-replies-for-line/645621c60104980882a56c2c
- Create Template Messages for LINE — https://www.sprinklr.com/help/articles/line/create-template-messages-for-line/6456214f0104980882a56c2b
- Create Custom Rich Menus for LINE — https://www.sprinklr.com/help/articles/line/create-custom-rich-menus-for-line/64561fdd0104980882a56c2a
- LINE Reporting Metrics — https://www.sprinklr.com/help/articles/line/line-reporting-metrics/64561d2b0104980882a56c0f

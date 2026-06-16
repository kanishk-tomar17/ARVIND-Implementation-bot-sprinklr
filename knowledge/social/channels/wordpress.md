# WordPress (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — WordPress channel (multiple articles; see links below)

## What it is
- WordPress is a content-management system, integrated into Sprinklr as a Social channel so teams can **engage, publish, report, and monitor** their WordPress blog from one place.
- Publish blog posts directly from Sprinklr (immediate, scheduled, or draft), with title, body, excerpt, categories, tags, featured image, and author selection.
- Engage with blog activity: comment on posts, reply to comments/replies, approve/unapprove (hold) comments and replies, and mark them as spam.
- Supported post (message) types: **Text, Photo, Video, Quote, Link**.
- Requires WordPress to be enabled in your environment (coordinate with your Success Manager) and the WordPress account credentials/access tokens in hand before you start. See [[publishing]], [[engagement-dashboards]], [[reporting]].

## Key features & how to use

### Setup — Add a WordPress account
Path: **New Tab icon → Sprinklr Social → Owned Social Accounts within Listen → Add Account** (top-right of the Accounts/Settings window).
- In **Add Account** ("Choose a channel you would like to add an account for"), search **wordpress** and select the **Wordpress** tile.
- The **Add Wordpress account** form (Basic Details) opens with a **Select Authentication Type** toggle: **Basic Auth** or **RPC**.
  - **Basic Auth** fields: **Wordpress Domain Url** (required), **Username** (required), **Password** (required), **Default Language**, **Linked Languages**.
  - **RPC** fields: **URL** (required), **Username** (required), **Password** (required), **API Key**.
  - Required fields are marked with a red dot. Username is the WordPress login (WP Admin → Users → All Users); Password should be a WordPress **Application Password** generated for API use, not the login password.
- Click **Save** to proceed to account configuration, then set:
  - Display account name in Sprinklr; assign the Sprinklr **User** owner.
  - Optional **custom character count**; optional default **URL shortener**.
  - **Publish post as draft** checkbox (forces posts to draft state).
  - **Account Groups**, **Permissions** for Users/User Groups, **Workspaces** (visibility), **Subscribers** (notifications), and **Timezone**.
- Click **Save** (bottom-right) to finish.
- Prereqs: WordPress channel enabled in the environment; all access tokens/credentials ready.

### Publishing — Publish to a WordPress account
Path: **New Tab icon → Sprinklr Social → Quick Publish within Engage** (opens the **Create Post** window).
- **Select Accounts**: search and add the WordPress account(s); **Advanced Search** is available to refine.
- **Type of Message** dropdown: **Photo, Link, Quote, Video, Text**.
  - Note: a single video publishes as a URL; for embedding, previewing, or multiple videos, contact your Success Manager.
- **Author**: choose from the **Select an Author** dropdown.
- **Title** and **Excerpt** fields for the blog post.
- **Description** (required): rich-text editor (Paragraph styles, bold/underline/alignment, lists, image insert). Use the **Insert** menu to add Custom Links, Content Placeholders, Text Templates, or YouTube videos; **Sprinklr AI+** is available inline for content help.
- **Category**: select from dropdown, or **Create New Category** (name + parent category → **Create**).
- **Tags**: select from dropdown, or **Create New Tag** (name → **Create**).
- **Featured Image**: click **Select Photo** to add from the Media Uploader or upload from device.
- Optional: associate a **campaign**/**sub-campaign**, add **Tags** and **Social Bars**, apply a **URL Shortener**, apply **Properties**, and set an **Approval Type** (with optional Approval Note).
- Live **preview** renders in the right pane (mobile/web toggle; note: mobile preview is not available for WordPress — use **View Web preview**).
- Publish options (bottom of window):
  - **Post** — publish immediately.
  - **Save as Draft** — keep for later.
  - **Schedule Post** — pick month/date/time → **Apply**.
  - **Publish Another** checkbox — keep creating posts after this one.
- Field set varies by message type (Photo adds **Photo** + **See More Url**; Video adds **Video**; Quote replaces Title with **Quote**; Link adds **Url**). See [[publishing]].

### Engagement — Create a column for WordPress
Path: **New Tab icon → Sprinklr Social → Engagement Dashboards within Engage** → open a dashboard → **Add Column** (top-right).
- Search and select **WordPress** as the source.
- Choose **column type**: **Inbox**, **Blogs**, **Comments**, or **Replies**.
- Enter **Name**, **Description**, **Accounts**, and Basic Information.
- **Workflow Properties**: filter by message workflow status, user assignment, priority, spam, and sentiment.
- **Custom Properties**: include/exclude messages by applied properties.
- Click **Create Column**.
- Supported engagement actions in-column: comment on posts, reply to comments, reply to replies, approve/unapprove (hold) comments and replies, mark comments/replies as spam. See [[engagement-dashboards]].

### Editing a published WordPress post
- In an Engagement Dashboard, find the WordPress blog post.
- Hover the **Options** icon → **Edit**.
- Update fields in the Edit Post window → click **Post** to publish the changes.

## Common issues & fixes
- **Mobile preview unavailable for WordPress** in Create Post — use **View Web preview** instead.
- **Video limits**: single videos render as URLs; embedding/previewing/multiple videos need Success Manager involvement.
- **Posts going to draft unexpectedly**: check the **Publish post as draft** account setting.
- **Auth failures**: confirm the right auth type (Basic Auth vs RPC); for Basic Auth use a WordPress **Application Password**, not the account login password.

## Notes & gaps
- Channel must be enabled per environment via the Success Manager before the WordPress tile appears.
- Permissions follow the account's configured User/User-Group permissions and Workspace visibility.
- **Media specs** (file sizes/dimensions) are not in these articles — see Sprinklr's "WordPress Media Recommendations".
- The capabilities article lists supported actions only; it does **not** state character limits or detail dedicated reporting metrics. Reporting is implied via the channel integration but not documented in these four articles — confirm available metrics in the reporting module. See [[reporting]].
- RPC auth uses an **API Key** field (per the UI); the Authorization URL / Client ID / Client Secret / API Identifier sometimes cited elsewhere were not present in the current Add-account form.

## Sources
- Add a WordPress account to Sprinklr — https://www.sprinklr.com/help/articles/wordpress/add-a-wordpress-account-to-sprinklr/645267450d27fc559bbe5503
- WordPress capabilities & limitations — https://www.sprinklr.com/help/articles/wordpress/wordpress-capabilities-limitations/64557ca10104980882a54eba
- Publish to WordPress account — https://www.sprinklr.com/help/articles/wordpress/publish-to-wordpress-account/64557c7a0104980882a54e5b
- Create a column for WordPress — https://www.sprinklr.com/help/articles/wordpress/create-a-column-for-wordpress/64557cc60104980882a54f0a

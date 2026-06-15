# Advanced Publishing — Workflow & Compliance (Sprinklr Social — Publishing)
**Source:** sprinklr.com/help — Publishing sub-area (multiple articles; see links below)

## What it is
- Advanced publishing controls that sit on top of the core Publisher (Quick Publisher / Advanced Publisher) to improve accuracy, compliance, and reliability of posts.
- Covers content optimisation (A/B testing, content placeholders, spelling/grammar, custom dictionary), link handling (URL shortening, invalid-link detection, TRAI SMS compliance), special post types (organic dark posts, broadcast announcements), account hygiene in the publisher (deactivated/disabled accounts, Facebook DM account locking), and reliable scheduling (media pre-upload).
- Reference for consultants configuring client environments — many features are gated by a **Dynamic Property** that a Success Manager / tickets@sprinklr.com must enable.
- Related GROOT topics: [[ai-in-publishing]], [[editorial-calendar]], [[approval-workflows]], [[rule-engine]], [[asset-manager]], [[web-analytics]].

## Key features & how to use

### Organic Split (A/B) Testing
- Tests up to **4 variants** of the same post and surfaces the best performer by a chosen metric.
- **Scope:** currently only **Organic Facebook video posts and Reels**.
- Path: Sprinklr Social > Engage > **A/B Testing** > **Create A/B Test** (top right).
- Select **Channel** and **Account** from dropdowns.
- Under **Variant**, set **Format** (post type); click **Add Variant** to add more (max 4). Variants can differ by media file, thumbnail, title, description.
- **Test Details** tab: enter **Test Name**, select the **Key Metric** (e.g. number of plays, impressions, link clicks, average time watched) — the winning metric.
- See also [[web-analytics]] for performance reporting.

### Publish with Content Placeholders
- One post auto-fills account-specific values (e.g. per-store link) instead of creating separate messages per account.
- **Step 1 — create an Account custom field:** New Tab > Platform Modules > All Settings (Listen). Field type **Pick-list**, Asset Type **Account**, values **Manual**, and tick **Enable for Content Replacement**. Best practice: set a sensible default value for accounts with no specific value.
- **Step 2 — apply to accounts:** New Tab > Platform Modules > Accounts > select account > Options > Edit > set the custom field value > Save.
- **Publish:** Publish > Create Post > select accounts > in the Message box click the **Insert (+)** icon > **Content Placeholder** > pick the placeholder (named after the custom field) > Post.
- Permission-gated (may require System Admin). See [[asset-manager]].

### Character Count Limits for Publishing
- Publisher shows remaining characters in the bottom-right; switch between global and channel editors by clicking the channel icon.
- Stated limits: **Global 10,000** | **Facebook Page 5,000** | **LinkedIn Company 1,300** | **Instagram 2,200** | **Twitter/X 280** (JP/KO/ZH retain 140) | **Twitter DM 10,000** | **VK 3,923** | **Yelp Location 5,000**.
- Twitter/X: links always count as **23 characters** regardless of length; media (images/videos) count as **0**. Replies subtract the recipient handle.

### Spelling and Grammar Check
- Inline check while composing posts/responses. **Red underline = spelling**, **green underline = grammar**. Right-click an error for suggestions; choose **Add to Dictionary** to stop future flagging.
- **Spell Check Language** field (user-level) selects the dialect variant — 30+ languages incl. English (US/GB/AU/CA/NZ/ZA), Spanish, French, German, Portuguese variants, Japanese, Chinese (Simplified), Persian, Ukrainian.
- **Dynamic Property:** `GRAMMAR_CHECK_WITH_VARIANT_LANGUAGES_ENABLED` (via Success Manager / tickets@sprinklr.com).
- **Permissions:** Edit User permission to change Spell Check Language; Add to Dictionary can be disabled per user; macro support for bulk field updates.
- Works in Quick Publisher, Advanced Publisher, Reply Window, Agent, and Care console. Uses the LanguageTool API.
- Can drive pre-publishing [[rule-engine]] conditions (**Grammatical Errors**, **Is Grammar Correct**) and reports (Grammar Violations Count, Spell Check Violations Count).

### Manage Custom Dictionary
- Org-wide store of approved words (industry/proprietary terms) that won't be flagged; tracks who added each word; multi-language.
- **Permissions:** View, Add to Dictionary, Remove from Dictionary, Edit.
- **Add (manual):** New Tab > Platform Modules > All Settings (Listen) > Manage Customer > **Dictionary** > **Add Word** (top right) > enter word + language > Add.
- **Add (from Publisher):** right-click a red-underlined word > **Add to Dictionary**.
- **Add (bulk):** Dictionary > **Import Words** > drag Excel file or Choose file.
- **Edit/Remove:** hover a word > Options icon > Edit (Update) or Remove (confirm).

### Use a Shortened URL in Publisher
- Compresses long links (Instagram, Facebook, YouTube, Twitter, LinkedIn) to **19 characters**. Requires a pre-configured URL shortener.
- Open **Custom Links** window: `Ctrl + Shift + K` (Win) / `control + shift + K` (Mac).
- Enter the link > select a **URL shortener** from the dropdown > **Shorten** (bottom right) > copy via the copy icon > **Done**.
- Then publish via Quick Publish: select account in **Select Accounts**, paste the shortened URL into the **Content box**, finish details, **Post**.

### Detect Invalid Links within Quick Publisher
- Validates URLs before publishing and shows an error if a link is broken (page removed/deleted, bad redirect/server error, access-restricted).
- Activates at scheduling and at publish time, in both Create Post and Response Publisher windows; works across channels that support link posts.
- **Dynamic Property:** `VALIDATE_URL_ENABLED` (enable via Success Manager).

### Publish Organic Dark Posts
- Unpublished organic content for **Facebook and Twitter** — reaches targeted audiences without appearing on the main page feed.
- **Create:** Quick Publish > Create Post > select account(s) > compose > scroll down and select **"Publish this page as a Dark Post for Facebook pages"** or **"Publish this post as a Dark post for Twitter"** > Post.
- **View in [[editorial-calendar]]:** shows the Dark Post icon; hover + click the timestamp for the dark post permalink.
- **View in Engagement Dashboards:** Add Column > source Outbound or Facebook. Outbound: use **Exclude Dark Post**. Facebook: set **Published Status** = **Only Unpublished**.
- **Delete:** hover the three-dot icon (bottom-right of message) > Delete.

### Broadcast an Announcement
- System admins send platform-wide announcements (e.g. risk-mitigation guidance during incidents); show once or until an expiry date.
- **Permission:** **Broadcast** under the Setup section. Assign via All Settings (Listen > Platform Modules) > Workspace Roles > Create Role > assign to users/groups > Save.
- **Create:** Notifications bell icon (top right) > announcement icon > **Broadcast an Announcement** > choose **Text** or **Media & Text** > enter Message > **Select Media** (optional) > add Title and Description (emoji picker optional) > set **Confirmation Text** and **Expiry Date** > under **Share the announcement with** pick User / User group / Workspace / Workspace group (or combinations) > set **Approval Type** + optional Approval Note > **Post**.
- Rejected approvals block publication. See [[approval-workflows]].

### TRAI India SMS Link-Structure Compliance
- India's TRAI requires shortened SMS URLs to show the sender relationship: format changes from `https://spr.ly/{UniqueID}` to **`https://spr.ly/{SenderID}/{UniqueID}`** (sender ID as prefix).
- **Setup:** Launch Pad > All Settings > Manage Workspace > **URL Shortener** > **+ Add URL Shortener** (or edit existing via the vertical ellipses).
  - **Primary Details:** URL Provider (dropdown), URL Name, Source Protocol (HTTP/HTTPS).
  - **Provider Settings:** URL Domain, **Path Prefix** = your DLT-verified sender ID. Optionally tick "Set as default shortener for publishing" / "...for vanity url" > Save.
- **Prerequisite:** register the sender ID on the **DLT portal** and paste the verified ID into **Path Prefix**.

### Disabled Account Switching in Facebook DM Replies
- Prevents publishing failures by locking the account switcher when replying privately to a Facebook fan — Meta requires DMs to come from the account the fan originally engaged with.
- Path: Sprinklr Social > Engagement Dashboards > Engage > open Facebook Dashboard > select a post with a fan comment > **Reply**.
- In the reply window choose the message type: **Reply** (public), **Comment on Post** (threaded public), or **Message** (private DM). When **Message** is selected, the **account switcher is disabled** and a tooltip explains the Meta restriction.
- Send options: Schedule Post, Save draft, Send; Preview available.

### Show Deactivated Accounts in Publisher
- Deactivated accounts become visible (with an inactive indicator) when selecting accounts in the publisher and in Advanced Search — for transparency; they cannot be selected to publish.
- **Setup:** environment-specific — enable via Success Manager.
- Path: Quick Publish > Create Post > account selection / Advanced Search.

### Manage Deactivated Accounts from Quick Publisher (Add / Re-add / Notify Admin)
- Manage account hygiene without leaving Quick Publisher.
- **Add Account:** new **Add Account** button in the Selected Accounts field opens the standard add-account window.
- **Deactivated account actions:** click the **red triangle** icon next to the account (pop-up shows the deactivation reason) > **Re-add Account** (standard reactivation flow) or **Notify Admin** (requests reactivation).
- **Permissions:** `ADMIN_ASSETS_PERMISSIONS_ENABLED` dynamic property **+** Create Account permission.
- **Channels:** Facebook Page, Google My Business, Instagram, LinkedIn, LinkedIn Company, Pinterest, TikTok Business, X (Twitter), YouTube (more to follow).

### Pre-upload Media for Publishing at Exact Schedule
- Uploads media to the channel ahead of time so a scheduled post fires at the exact moment (no upload-delay slippage).
- **Channels:** Twitter, LinkedIn, Instagram only. Enable via Success Manager.
- **Timing rules:** Pre-upload option appears only when scheduling **30+ minutes** ahead; if the scheduled time is **23 hours or later**, the system auto-pre-uploads.
- **Steps:** New Tab > Publisher icon > select account(s) > add media > add Message + channel details (LinkedIn: Message; Twitter: message type + Alt Text; Instagram: Caption) > click **Pre-upload** > then choose **Post**, **Save as Draft**, or **Schedule Post**.
- **Status indicators** (top-right of Create Post): initialization, in-progress, success, or failure (with re-initiate option).
- **Editing:** edits allowed after pre-upload, but re-run pre-upload before scheduling/publishing.

## Common issues & fixes
- **Post truncated / rejected for length:** check the per-channel character limit (above). On Twitter/X remember links = 23 chars, media = 0, replies subtract the handle.
- **Facebook DM fails to send:** you tried to switch accounts — DMs must come from the account the fan engaged with; the switcher is intentionally disabled when **Message** is selected.
- **Publish fails on a deactivated account:** deactivated accounts are visible but cannot publish; use **Re-add Account** or **Notify Admin** from Quick Publisher (needs `ADMIN_ASSETS_PERMISSIONS_ENABLED` + Create Account permission).
- **Broken link blocks publishing:** invalid-link detection requires `VALIDATE_URL_ENABLED`; fix the URL flagged in the error.
- **Scheduled post publishes late / media missing:** use Pre-upload (Twitter/LinkedIn/Instagram). On failure the system retries; if it still fails, media uploads at actual publish time.
- **Dark posts not pulled into Sprinklr:** dark posts published natively on Facebook are not pulled in unless a comment is made on the post.
- **Valid term flagged as misspelled:** add it to the Custom Dictionary (Add to Dictionary from Publisher, or bulk Import Words).
- **SMS short links rejected in India:** ensure the DLT-verified sender ID is set in **Path Prefix** so links use `spr.ly/{SenderID}/{UniqueID}`.

## Notes & gaps
- **Success-Manager / Dynamic-Property gated:** Spelling-grammar variants (`GRAMMAR_CHECK_WITH_VARIANT_LANGUAGES_ENABLED`), invalid-link detection (`VALIDATE_URL_ENABLED`), show deactivated accounts, manage deactivated accounts (`ADMIN_ASSETS_PERMISSIONS_ENABLED` + Create Account), and media pre-upload. Confirm enablement before promising these in a client env.
- **Permission-gated:** Content Placeholders (custom-field creation, may need System Admin); Broadcast announcements (Broadcast permission); Custom Dictionary (View/Add/Remove/Edit).
- **Scope limits stated:** A/B testing = Organic Facebook video/Reels only; Dark Posts = Facebook + Twitter; Pre-upload = Twitter/LinkedIn/Instagram only.
- **Not specified by the articles:** exact custom-dictionary size limits; precise visual styling of deactivated-account indicators; URL-shortener provider list / setup steps for the shortener itself; full list of A/B testing key-metric options beyond the examples; retry counts/backoff for pre-upload; whether character limits update with future native channel changes.
- Article URLs reflect the "advanced-capabilities" help path; UI labels may shift across Sprinklr releases — verify live and prefer sprinklr.com/help if sources conflict.

## Sources
- Organic Split (A/B) Testing on Sprinklr — https://www.sprinklr.com/help/articles/advanced-capabilities/organic-split-ab-testing-on-sprinklr/66a1192200331679bfd4c578
- Publish with Content Placeholders — https://www.sprinklr.com/help/articles/advanced-capabilities/publish-with-content-placeholders/6437831cb7f3625d288e742f
- Character Count Limits for Publishing — https://www.sprinklr.com/help/articles/advanced-capabilities/character-count-limits-for-publishing/63fede497a695d65a160587a
- Spelling and Grammar Check — https://www.sprinklr.com/help/articles/advanced-capabilities/spelling-and-grammar-check/63fee0be32d12b63c5f55c3c
- Manage Custom Dictionary in Sprinklr — https://www.sprinklr.com/help/articles/advanced-capabilities/manage-custom-dictionary-in-sprinklr/6569a3fa44f32b4163d5734a
- How to Use a Shortened URL in Publisher — https://www.sprinklr.com/help/articles/advanced-capabilities/how-to-use-a-shortened-url-in-publisher/6453905cf65d86626c829e7f
- Detect Invalid Links within Quick Publisher — https://www.sprinklr.com/help/articles/advanced-capabilities/detect-invalid-links-within-quick-publisher/63fee1cf7a695d65a160587e
- Publish Organic Dark Posts — https://www.sprinklr.com/help/articles/advanced-capabilities/publish-organic-dark-posts/64378911b7f3625d288e7432
- Broadcast an Announcement — https://www.sprinklr.com/help/articles/advanced-capabilities/broadcast-an-announcement/6436b577c7dea832a77e11a8
- TRAI India Government Regulation on SMS Link Structure — https://www.sprinklr.com/help/articles/advanced-capabilities/trai-india-government-regulation-on-sms-link-structure/6718d310d4ec357fe5d73ed3
- Disabled Account Switching in Facebook DM Replies to Prevent Publishing Failure — https://www.sprinklr.com/help/articles/advanced-capabilities/disabled-account-switching-in-facebook-dm-replies-to-prevent-publishing-failure/6799ead6b8b98177d0489de8
- Show Deactivated Accounts in Publisher — https://www.sprinklr.com/help/articles/advanced-capabilities/show-deactivated-accounts-in-publisher/6641ac271bca4f6f747fc834
- Manage Deactivated Accounts from Quick Publisher (Add, Re-add, and Admin Notifications) — https://www.sprinklr.com/help/articles/advanced-capabilities/manage-deactivated-accounts-from-quick-publisher-add-readd-and-admin-notifications/6799e5817a3dda2a871da159
- Pre-upload Media for Publishing at Exact Schedule — https://www.sprinklr.com/help/articles/advanced-capabilities/preupload-media-for-publishing-at-exact-schedule/645491aa0d27fc559bbeb46b

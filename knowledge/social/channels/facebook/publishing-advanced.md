# Facebook — Advanced Publishing (Sprinklr Social — Facebook)
**Source:** sprinklr.com/help — Facebook channel (multiple articles; see links below)

## What it is
- Advanced Facebook publishing capabilities in Sprinklr beyond a plain page post: Workplace group posts, audience targeting/gating, dark→published conversion, editing natively scheduled posts, video monetisation, mobile-app publishing, and domain verification for link previews.
- All flows run from the Sprinklr [[publishing]] Publisher (Create Post / Quick Publisher) or from [[engagement-dashboards]] columns.
- Some features depend on Facebook-side setup (Rights Manager access, Business Manager domain verification) that must be completed before the option appears or works in Sprinklr.
- Targeting, monetisation, and dark posts apply to **Facebook Pages**; Workplace posting applies to a **Workplace Bot** account.

## Key features & how to use

### Publish content to Facebook Workplace
- Post messages, images, and videos to a Facebook **Workplace** group from the Publisher.
- Steps:
  1. Open the Publisher and select **Create Post**.
  2. Choose a **Facebook Workplace Bot** account, then pick the specific Workplace **group**.
  3. Enter text in the **Message** box; use **@mention** to tag people/groups.
  4. Use the **Insert** icon to add custom links, placeholders, templates, or YouTube videos; use the **Emoji Picker** icon for emojis.
  5. Add **Photo** or **Video** via Media Uploader (Digital Asset Manager) or device upload. Photos support an **alt text** field ("Write alt text here…"); videos do not.
  6. Set **Campaign** (primary + sub-campaign), **Tags**, and **Social Bars** / custom properties; optionally apply the **URL Shortener**.
  7. Set **Approval Type** with optional approval note.
  8. **Publish** now, **Save as Draft**, or **Schedule Post** (date/time). A minimisable **Preview** pane shows the rendered post.

### Targeting & Gating Facebook Posts
- Restrict or prefer who sees a Page post by demographics/location. Applies when publishing from a **Facebook Page** account.
- In Create Post, below the post body two links appear: **Add Preferred Audience to this post** (Targeting) and **Add Audience Restrictions to this post** (Gating).
- For each, choose **Select from Saved Target Audiences** (reuses a saved [[asset-manager]] audience) or **Add New Audience** to build one.
- **Select Target Audiences** screen lists saved audiences in a table — columns: Name, Audience Id, Reach, Modified Date, Creation Date, Age, Gender, Country, Additional Targeting Values; has **Add Filter**, search, and **Add Selected** / **Add New Audience**.
- **Preferred Audience (Targeting)** fields on the Add New Audience screen: **Min Age** (e.g. 13), **Interests** (searchable, multi-select), **Gender** (Male/Female), **Locations** (Country/Region/City), **Relationship Status** (Single, In a Relationship, Married, Engaged), **Interested In** (Male/Female), **Language**, **Education Status / Level** (In High School, In College, College Grad). A live summary panel previews the chosen audience; tick **Save this Target Audience for Future**, then **Set Target Audience**.
- **Audience Restrictions (Gating)** fields are limited to: **Locations**, **Language**, plus the save checkbox.
- **Limit:** Facebook supports a maximum of **25 countries, 200 cities, 200 regions, or 50 locales** when geo-targeting a single post.

### Convert Facebook Dark Posts into Published Posts
- A **dark post** (unpublished/page-unlisted post) can later be published organically.
- Create a dark post: in Quick Publisher, tick **"Publish this post as Dark Post for Facebook Pages."** (Adjacent options: "Publish this post as Draft Post for Facebook Pages" and "Schedule this post on Facebook Page.")
- Dark posts appear in the **outbound/sent** column but **cannot be published from there** — they only surface for publishing in an **inbound** column type (e.g. Facebook Post). Perform some engagement on the post to fetch it inbound.
- To convert via an [[engagement-dashboards]] column:
  1. New Tab → **Sprinklr Social > Engage > Engagement Dashboards**.
  2. **Add Column** (top right) → select **Facebook** → column type **Post**.
  3. Fill **Basic Information** (preview renders on the right pane).
  4. Under **Published Status**, select **Only Unpublished** from the dropdown.
  5. Set **Workflow Properties** and **Custom Properties** as needed → **Create Column**.
  6. Find the message, hover the **Options** (three-dot) icon → **Publish**. To change it first, choose **Edit** to reopen Quick Publisher. (The Options menu also offers Like, Delete, Share, Open Details, Reminders, Sentiment, Update Tags, Translate, Mark as Spam, Mark Secure.)

### Edit Natively Scheduled Facebook Posts
- Edit/reschedule posts scheduled **natively on Facebook** from inside Sprinklr — no native page access needed.
- Steps:
  1. New Tab → **Sprinklr Social > Engage > Engagement Dashboards**.
  2. **Add Column** → category **Outbound** → column type **Scheduled**.
  3. Configure: **Name**, **Channel = Facebook**, **Account** (the Facebook Page), **Status = "Scheduled on Facebook."**
  4. Review preview → **Create Column**.
  5. On the post, click the **Edit** icon to open Quick Publisher, make changes, then **Schedule**.
  6. To only move the time, click the **reschedule** icon and pick a new date/time on the calendar.

### Monetise Videos from Sprinklr
- Enable monetisation on video posts for Facebook, Twitter (X), and YouTube. Requires platform-side rights/ads setup first.
- **Account prerequisite (Facebook):** the Page must have Rights Manager access. In **All Settings > Accounts**, find the Facebook Page → **Edit** → enable the checkbox **"Page is Authorised with Rights Manager Access to Monetise Facebook Videos."** (Twitter needs a linked Twitter Ads account; YouTube channel needs rights-management access added via the authorised content owner's Google account.)
- **Facebook video** in Create Post: after uploading, tick **"Monetise this video"** to reveal **Monetisation Options**:
  - **Copyright Rule** (required) — select from dropdown.
  - **Content Category** (required) — TV Episode / Film / Web.
  - **Monitoring Type** (required) — Video only / Video & audio / Audio only.
  - **Include Territories** and **Exclude Territories** (multi-select country chips).
  - **Allowlist** — search and add Facebook Pages.
- **Twitter video:** enable checkbox → optional **Exclude Tags**, optional **Exclude advertiser @handles**, select **countries**, tag **Video Category** (multi-select).
- **YouTube video:** enable checkbox → **Upload Policy** (Monetise/Block/Track), optional **Content ID matching**, claim ownership (Globally or by territory), **Asset Type** (TV Episode/Film/Web), and ad placement: **Pre-roll**, **Post-roll**, **Mid-roll** (videos ≥8 min) with custom mid-roll breaks.
- **Limits:**
  - Once a video is published with monetisation enabled, **monetisation cannot be disabled.**
  - Facebook: cannot select Ownership Link, cannot enable In-stream Ads, cannot use Facebook Profiles/Instagram in the allowlist.
  - YouTube: Ads Suitability cannot be set (defaults to "None of the above").

### Publish via Sprinklr Mobile App
- Create posts on the go via the Sprinklr Mobile App Publisher; save as draft or schedule.
- Steps:
  1. Tap the **Menu** icon (bottom right) → **Publishing** under Sprinklr Social.
  2. In the **Select Account** popup, search and tick one or more accounts (Facebook Page, Twitter, Instagram, etc.) → **Done**.
  3. Enter the **caption**.
  4. Tap the **Image** icon to upload media from device or **Digital Asset Manager**.
  5. Tap **Customise** or **Next** to reach the **Optimize** screen — note you **cannot revert** to the basic editor after customising.
  6. Complete required per-channel fields on **Optimize** (each channel shown as its own block, e.g. "Twitter (Message)", "Instagram (Post)", with per-channel Advanced Settings).
  7. **Save as Draft** or **Publish**.
- **Multi-channel:** simple posts (media + text) can go to Twitter, Facebook, Instagram, and LinkedIn **simultaneously**. Advanced types (Carousel, Album, etc.) must be posted **one channel at a time**.
- If **Publish** is set as a **personalised shortcut**, you can start a post directly from the bottom navigation bar.

### Facebook Domain Verification
- Verify domain ownership in **Facebook Business Manager** so you can edit/customise link previews shared on Facebook (done on Facebook's side, not in Sprinklr).
- **Prerequisites:** be a Facebook Page admin with Business Manager access, and have access to the domain's DNS records.
- Steps:
  1. In Business Manager left menu, open **Domains** → **Add** / **Add New Domains**.
  2. Enter the domain to verify.
  3. Log into the domain registrar and add the provided **TXT record** to DNS.
  4. Back in Business Manager, click **Verify** → confirmation shows on success.
- **Grant access to others:**
  - **Assign Partner** — copy the generated **single-use** link and share with another business for link-editing rights.
  - **Assign Pages** — give access to other Facebook Pages you own.

## Common issues & fixes
- **Dark post won't publish from the sent column** — it can't; fetch it into an inbound column (engage on it first) and publish from there, or use an Engagement Dashboard column with Published Status = Only Unpublished.
- **No "Monetise this video" option** — the Page lacks Rights Manager access; enable the Rights Manager checkbox under All Settings > Accounts > Edit for that Page.
- **Monetisation greyed out / can't turn off** — once published with monetisation on, it cannot be disabled.
- **Geo-targeting rejected** — you exceeded Facebook's caps: 25 countries / 200 cities / 200 regions / 50 locales per post.
- **Customised link preview won't save / publish** — the domain isn't verified in Business Manager; complete TXT-record domain verification first.
- **Mobile: can't go back to basic editor** — expected; once you tap Customise/Next you stay in the Optimize editor.

## Notes & gaps
- Workplace posting needs a connected **Facebook Workplace Bot** account; targeting, gating, dark posts, and monetisation apply to **Facebook Page** accounts.
- Targeting/gating audiences can be saved and reused as assets (see [[asset-manager]]); approval routing follows the standard [[publishing]] approval flow (Approval Type field).
- Domain verification is entirely a Facebook Business Manager task; Sprinklr only consumes the verified domain when customising link previews.
- Article text did not state hard counts on Workplace media limits, exact required user permissions/roles inside Sprinklr for each action, or whether scheduled-post editing has a cut-off window before publish time — confirm in-platform.
- Some article images were Google-CDN hosted and time-limited; UI detail above was confirmed from the durable Sprinklr-CDN screenshots that were viewed.

## Sources
- Publish Content to Facebook Workplace — https://www.sprinklr.com/help/articles/create-a-post-on-facebook/publish-content-to-facebook-workplace/63ec532eef1b447d6c6242da
- Targeting & Gating Facebook Posts — https://www.sprinklr.com/help/articles/other-publishing-capabilities/targeting-gating-facebook-posts/63ec58dbf6e2cc7d18f9f604
- Convert Facebook Dark Posts into Published Posts — https://www.sprinklr.com/help/articles/other-publishing-capabilities/convert-facebook-dark-posts-into-published-posts/63ecd956f6e2cc7d18fabb25
- Edit Natively Scheduled Facebook Posts — https://www.sprinklr.com/help/articles/other-publishing-capabilities/edit-natively-scheduled-facebook-posts/63ec5411ef1b447d6c624332
- Monetise Videos from Sprinklr — https://www.sprinklr.com/help/articles/other-publishing-capabilities/monetise-videos-from-sprinklr/63ece06df6e2cc7d18fabc6d
- Publish via Sprinklr Mobile App — https://www.sprinklr.com/help/articles/other-publishing-capabilities/publish-via-sprinklr-mobile-app/63ea29adef1b447d6c61b291
- Facebook Domain Verification — https://www.sprinklr.com/help/articles/other-publishing-capabilities/facebook-domain-verification/63ec5bb5ef1b447d6c624593

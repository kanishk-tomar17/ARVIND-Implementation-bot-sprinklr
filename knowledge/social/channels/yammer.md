# Yammer (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Yammer channel (multiple articles; see links below)

## What it is
- Yammer (now rebranded by Microsoft to **Viva Engage**) is an internal enterprise collaboration channel. Sprinklr lets your team **engage, publish, report, and monitor** a brand's Yammer Groups from inside the platform.
- Channel name shown in Sprinklr is **YammerGroup**. Sprinklr supports both **Public and Private** Yammer Groups — but you can only add groups **you are already a member of**.
- Engagement: view and reply to Yammer Group posts and comments (public and private). Publishing: create text posts plus image/video media, hashtags and emojis.
- Hard limits: **cannot delete** posts/comments, **cannot @mention** another Yammer user, **cannot edit** a published post. Reporting is **inbound + SLA only**. No mobile preview.
- See [[publishing]], [[engagement-dashboards]], [[reporting]].

## Key features & how to use

### Capabilities & limitations (read first)
- **Engagement (supported):** view Yammer Group posts and comments; reply on Yammer Group posts and comments. Works for both public and private group content.
- **Publishing (supported):** publish a Yammer Group post; add media attachment (image & video); use hashtags and emojis.
- **Reporting (supported):** **inbound and SLA reporting only** for Yammer Group — no engagement/outbound metrics.
- **Not supported:** deleting posts or comments; @mentioning another Yammer user; editing a published post.
- **Media constraint:** if the Yammer network has **no Azure Directory connection**, video upload via Sprinklr Quick Publish is capped at **4 MB**.
- **Microsoft 365 Groups constraint:** if the Yammer network is connected to **Microsoft 365 Groups**, you can publish **text only** (posts/comments/replies) — media posts are not possible.

### Setup — prerequisites
- Enable the channel via the dynamic property (DP): **`YAMMER_CHANNEL_ENABLED`** (`yammer.channel.enabled`, BOOLEAN, PARTNER level).
- For **Private** Yammer Groups, contact Sprinklr Support — it requires additional setup.

### Setup — add a YammerGroup account
1. Click the **New Tab** icon → under **Sprinklr Social**, select **Owned Social Accounts** (within Listen).
2. In the **Accounts (Settings)** window, click **Add Account** (top right).
3. In the **Add Account** window, search and select **YammerGroup** from the channel list.
4. Enter the **Email Address** and **Password** for the account to add.
5. Follow the authentication prompts to grant Sprinklr permission.
6. Edit **Account Details** — account display name, owning Sprinklr User, custom character count for replies, default URL shortener, auto-populated reply signature, Groups to include the account in, User/User Group permissions, workspace visibility, subscriber notifications, timezone, and account properties.
7. Click **Save** (bottom right).

### Setup — add (white-label) your own Yammer App on Sprinklr
- Use this to run Yammer on your own Azure app credentials instead of Sprinklr's default app.
1. **New Tab** icon → **Sprinklr Social** → **Owned Social Accounts** (within Listen).
2. In **Accounts**, filter the channels for **Yammer**.
3. Click the **Options** (three-dot) icon next to the target Yammer account → select **White Label**.
4. The **"Whitelist Yammer Group App"** dialog opens with two input fields and a read-only callback:
   - **Yammer Group Consumer Key** — paste the Azure Application (client) ID.
   - **Yammer Group Consumer Secret** — paste the Azure client secret **Value**.
   - **Callback URL for Yammer Group** — non-editable; use the **Copy** button to grab it for the Azure redirect URI.
5. Click **Save** to register the app via the authentication flow.

### Setup — create the Azure app for Yammer
- **Create the app registration:**
  1. Go to `https://portal.azure.com/#home`.
  2. **More Services** (under Azure Services) → **App Registration** (under Others) → **New Registration**.
  3. Fill the form: app **name**, supported account/server type, and the **Redirect URI** — use the Callback URL copied from Sprinklr's White Label dialog (form e.g. `https://prod3.sprinklr.com/ui/oAuth2EntityCallBackHandlerV2?accountType=Yammer_GROUP`; the exact host/domain varies by Sprinklr environment — always copy your own from the platform).
- **Get credentials for Sprinklr:**
  1. Open the registered app; note the **Application (client) ID** → this is the **Yammer Group Consumer Key**.
  2. Go to **Client Credentials / Certificates & secrets** → add a new client secret with a description and expiry.
  3. Copy the generated secret **Value** immediately → this is the **Yammer Group Consumer Secret**. (Manage owned apps under **App registrations → Owned applications**, which lists Display name, Application (client) ID, Created date, and certificate/secret status.)
- **Admin consent:**
  1. Open **API Permissions**.
  2. Click **Grant admin consent / Grant Permission** so an admin approves the permissions for all accounts.
  3. Admin consent is a **one-time** action — individual users do not need to re-approve.

### Engagement — create a Yammer column
- Two column types: **Group Posts** and **Group Comments**.
1. **Sprinklr Social** → **Engagement Dashboards** (within Engage). See [[engagement-dashboards]].
2. From the Engagement Home window, open the target **Folder or Dashboard**.
3. Click **Add Column** (top right of the dashboard).
4. Search and select **YammerGroup** as the source.
5. Choose the column type: **Group Posts** or **Group Comments**.
6. Enter **Name**, **Description**, and **Accounts** — a live preview renders on the right.
7. Set **Workflow Properties** (message workflow status, user assignment, priority, Spam flag, sentiment).
8. Set **Custom Properties** to include/exclude messages by criteria.
9. Click **Create Column** (bottom right).

### Publishing — publish to a Yammer Group
1. **Sprinklr Social** tab → **Quick Publish** (within Engage). See [[publishing]].
2. In **Select Accounts**, search and pick the Yammer account(s); **Advanced Search** available for filtering. (The composer is titled **Create Post**; the channel toggle/button reads **Post**.)
3. Type into the **Message** box. The **Insert** menu adds custom links, content placeholders, text templates, or YouTube videos; the **emoji picker** adds emojis; hashtags supported.
4. Add media via **Select Media** (Media Uploader) or **Upload Media** (from device). (Respect the M365-Groups text-only and 4 MB no-Azure-Directory limits above.)
5. Choose **Campaign** and **Sub-Campaign**; tick **Set as Default** if wanted.
6. Configure **URL Shortener**, **Tags**, and **Social Bars**.
7. Apply any post **Properties** (the composer shows a large Properties set, e.g. "Properties (227)").
8. Set **approval type** and add **approval notes** if your workflow requires it.
9. Click **Post** to publish now, or **Save as Draft**. Use **Schedule Post** to set a future date/time. **Publish Another** keeps the composer open for the next post.
- A right-pane preview shows how the post renders (e.g. "All Company" group with Like / Comment / Share). **No mobile preview** is available for Yammer.

### Use a Yammer account as your Social Avatar
- Lets a consultant engage with Yammer **Public Groups** using their own Yammer profile identity.
1. Click the **profile icon** (top-right of the nav bar) → select your profile image / name / email from the dropdown.
2. In the **User** window, open the **Social Avatar** tab (in the dashboard bar, alongside Overview, Permissions, Manage Signatures, Notification Preferences, Security Settings).
3. Click **Add Social Avatar** (center of the tab; shown when "No social avatar added").
4. In the **Add Social Avatar** pop-up, choose **Yammer User**.
5. Sign in to your Yammer account if prompted, then click **Allow** to let Yammer grant Sprinklr access.
6. Your Yammer profile is now linked as your Social Avatar.

## Common issues & fixes
- **Can't add a group:** you must already be a member of the group. Private groups also require Support to enable the additional setup.
- **Channel not visible / can't add account:** confirm the `YAMMER_CHANNEL_ENABLED` partner DP is on.
- **Media post fails or only text goes through:** the network is connected to Microsoft 365 Groups (text-only) — media is not supported in that configuration.
- **Video upload rejected over 4 MB:** the Yammer network lacks an Azure Directory connection; under that setup Quick Publish caps video at 4 MB.
- **Delete / edit / @mention options missing:** these actions are not supported on Yammer in Sprinklr by design.
- **White Label save fails:** verify the Azure Redirect URI exactly matches the Copied Callback URL, the secret **Value** (not the secret ID) was pasted, and admin consent was granted in Azure.

## Notes & gaps
- **Rebrand:** Yammer is now Microsoft **Viva Engage**; Sprinklr UI and these articles still label the channel **YammerGroup / Yammer**.
- **Permissions:** adding accounts and white-labeling require Owned Social Accounts access; Azure admin consent requires an Azure AD admin.
- **Reporting scope is narrow** — only inbound and SLA reporting; no outbound/engagement analytics documented. See [[reporting]].
- **Unspecified in sources:** image/file size limits beyond the 4 MB video case; exact Azure API permission scopes to request; whether the [[rule-engine]] can act on Yammer messages; supported image/video formats; account-level rate limits.
- The "Add Yammer App on Sprinklr" article included several `blob:`/local screenshots that could not be downloaded; UI detail was taken from the downloadable White Label and Azure screenshots instead.

## Sources
- Add a Yammer Account in Sprinklr — https://www.sprinklr.com/help/articles/yammer/add-a-yammer-account-in-sprinklr/645649c7e66f2e36b4514d70
- Add Yammer App on Sprinklr — https://www.sprinklr.com/help/articles/yammer/add-yammer-app-on-sprinklr/660d6e742820514daf8782bb
- Create Azure App for Yammer — https://www.sprinklr.com/help/articles/yammer/create-azure-app-for-yammer/660d662f259c2c03bb8f65e0
- Yammer Capabilities and Limitations — https://www.sprinklr.com/help/articles/yammer/yammer-capabilities-and-limitations/645649830104980882a56d96
- How to Create a Yammer Column in Sprinklr — https://www.sprinklr.com/help/articles/yammer/how-to-create-a-yammer-column-in-sprinklr/64564193e66f2e36b4514d23
- Publish to Yammer Group — https://www.sprinklr.com/help/articles/yammer/publish-to-yammer-group/645648f00104980882a56d8f
- Use Yammer Account for Social Avatar — https://www.sprinklr.com/help/articles/yammer/use-yammer-account-for-social-avatar/6456494ae66f2e36b4514d6d

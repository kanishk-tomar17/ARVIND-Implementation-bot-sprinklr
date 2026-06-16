# VKontakte (VK) (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — VKontakte (VK) channel (multiple articles; see links below)

## What it is
- VKontakte (VK) integration for Sprinklr Social. Lets brands publish to, engage on, and report on VK Communities (VK Pages and VK Groups).
- Two account types are supported: **VK Group** and **VK Page**. Personal VK profiles are **not** supported as channels — but a personal VK profile must be identified by Sprinklr as a member (Admin/Editor) of the VK Community in order to authorize the account.
- Adding a VK account requires going through your **Account Manager** (it is not fully self-serve from the Add Account list alone — the AM provisions VK access).
- Terminology: anywhere the platform says "Group", it means a **VK Community**.
- Once added, VK accounts can be provisioned to users/user groups, used in the [[rule-engine]], and engaged via [[engagement-dashboards]].

## Key features & how to use

### Setup — add & manage a VK account
- **VK roles & who can publish:** VK Communities have four roles — Administrator, Community Editor, Moderator, Member. Only **Administrators** and **Community Editors** can publish Community Posts, so Sprinklr only adds/authorizes those two roles for publishing (via Quick Publisher or Engagement Dashboards).
  - If an authorized user is later demoted to Moderator/Member on VK, their outbound posts stop pushing live — the post just **saves as a draft on the Global Editorial Calendar**. Sprinklr gives **no notification** of the demotion.
- **Add a VK account:**
  1. Click the **New Tab** icon and select **Settings** under Sprinklr Social.
  2. In Settings, select **Accounts** (or use the search bar) to open Accounts Settings.
  3. Top-right of the Accounts (Settings) window, click **Add Account**.
  4. In the Add Account window, select **VK Page** from the channel list.
  - Note: per the capabilities article you must also coordinate with your Account Manager to get VK provisioned.
- **Manage an existing VK account:**
  1. New Tab icon → **Settings** under Sprinklr Social.
  2. Select **Manage Workspace** (left side) → **Accounts**.
  3. Click **All Channels** in the top-left of the section bar to filter accounts by **VK Page** (the Account Type column reads "VK Page").
  4. Hover the account's **Options** (three-dot) icon to act on it. (Screenshot confirms the Options menu items: **Details / Curate, Edit, Web Analytics, Enable Business Messaging, Push Notification Activation Steps, Deactivate, Remove Account**.)

### Setup — activate push notifications
- Path: New Tab → Settings → **Manage Workspace** → **Accounts** → filter to **VK Page** → hover the account's **Options** icon → select **Push Notification Activation Steps**.
- A **"VK Page Account Activation Steps"** pop-up opens. Follow its in-window steps to activate push notifications. (Screenshot of the pop-up shows the activation flow includes: log in at vk.com as Admin of the VK Page/Group; navigate to the Community; under Manage → API Usage → **Callback API**; under Settings copy the **"String to be returned"** value into the field on the VK page; in Sprinklr go to **Administration → Settings → Accounts → VK Page/VK Group**; enable PageGroup so push notification is received and confirm.) Exact field values come from the live pop-up — read it in the environment.

### Publishing
- See [[publishing]]. For media specs, see Vkontakte Media Recommendations (link in Sources).
- **Supported post content:**
  - **Text** — default character limit **3923**.
  - **Photo**, **Video**, **GIF**.
  - **Custom Link**, **Emoji**, **YouTube Video** insert.
  - **Content Placeholder** insert; **Text Template** insert.
  - **Direct Message** publishing.
  - **Discussion Topics** with Custom Link, Text Template, and Content Placeholder.
- **Not supported in publishing:**
  - **Editing a published post** (no edit-after-publish).
  - Publishing **audio files, maps, or documents**.
  - **Suggesting a post.**
  - **Synchronization with other social networks.**
  - **Mentions, emoticons, and hashtags** are not supported.
  - Controlling the availability of content within the network / on the internet.

### Engagement
- See [[engagement-dashboards]]. Post-level actions you can take:
  - **On posts:** Delete, Comment, Like/Unlike.
  - **On comments:** Reply, Like/Unlike, Delete.
  - **On replies:** Delete.
  - **Direct Messages:** Reply, Mark as important, Delete, Archive.
- **Filter messages** by **Brand**, **Fan**, or **All Messages**.
- **Supported column types:**
  - **VK Group:** Wall Post, Wall Comment.
  - **VK Page:** Wall Post, **Suggested Post**, Wall Comment.
  - **Both Group & Page:** Topic, Topic Comment, Search, Persistent Search, Direct Message.

### Reporting
- See [[reporting]]. VK reporting glossary defines the available metrics and dimensions.
- **Account-level metrics:** VK Albums, VK Followers, VK Photos, VK Posts, VK Reach (total people reached), VK Subscribers Reach (total subscribers to the Group), VK Topics, VK Videos, VK Video Views, VK Views (total views for the community), VK Visitors. Visitor breakdowns: **VK Group Visitors by Age Range / by City / by Country / by Demographics (age+gender) / by Gender**.
- **Post-level metrics:** VK Group Post Reach (total people reached by the post); Post Reach **By City / By City Trend / By Country / By Demographics**; **Post Reach Subscribers** and **Subscribers Trend**. Plus VK MeasurementGroup **Comments / Likes / Reposts** (each with a **Trend** variant over engagement dates). **Volume of VK Sent Direct Messages** = total VK sent DMs.
- **Dimensions:** **Age range and gender** (VK insights split by age+gender); **Is VK Poll** (flags whether an item is a poll).

## Common issues & fixes
- **Posts won't go live / silently save as drafts:** the publishing user was likely demoted on VK from Admin/Community Editor to Moderator/Member. Sprinklr does not warn about this. Restore the user's Admin or Community Editor role in the VK Community, then re-publish from the Global Editorial Calendar / Quick Publisher.
- **Can't edit a post after publishing:** not supported on VK — delete and re-publish if a change is needed.
- **Trying to publish audio/maps/documents, suggest a post, or sync to another network:** unsupported (API limitation). These functions are not available for Sprinklr to build on VK.
- **Mentions / hashtags / emoticons not working:** not supported on the VK channel.

## Notes & gaps
- **Prerequisites/permissions:** publishing user must hold **Administrator** or **Community Editor** in the VK Community; VK account provisioning requires the **Account Manager** (personal profiles can't be added as channels).
- "API Limitation" in the source = functionality VK's API doesn't expose for Sprinklr to build.
- **Push notification activation:** the exact callback/confirmation values live inside the in-platform "VK Page Account Activation Steps" pop-up; read them in the live environment rather than relying on the screenshot summary above.
- The reporting glossary lists metrics/dimensions only — it does not specify which standard dashboards/widgets ship with them; build custom widgets in [[reporting]] using these field names.
- Screenshots viewed (article 1) confirmed the Accounts Options menu and the activation pop-up; articles 2 and 3 contained no UI screenshots (only navigation/marketing imagery).

## Sources
- Add and Manage VKontakte Page Account — https://www.sprinklr.com/help/articles/vk/add-and-manage-vkontakte-page-account/645654ec0104980882a56e48
- Vkontakte Capabilities and Limitations — https://www.sprinklr.com/help/articles/vk/vkontakte-capabilities-and-limitations/64565313e66f2e36b4514dfb
- Vkontakte Reporting Glossary — https://www.sprinklr.com/help/articles/vk/vkontakte-reporting-glossary/64565586e66f2e36b4514e25
- (Referenced) Vkontakte Media Recommendations — https://www.sprinklr.com/help/articles/channels/media-recommendations-by-social-channel/64564f350104980882a56db5

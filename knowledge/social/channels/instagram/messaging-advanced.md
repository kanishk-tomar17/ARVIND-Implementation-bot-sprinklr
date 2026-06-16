# Instagram — DM Automation & Handover (Sprinklr Social — Instagram)
**Source:** sprinklr.com/help — Instagram channel (multiple articles; see links below)

## What it is
- Advanced Instagram Direct Message (DM) tooling in Sprinklr Social: structured entry points (Persistent Menu, Ice Breakers), reusable reply assets (Quick Replies, Carousel templates), and the Handover Protocol for moving a conversation between bots/apps and human agents.
- Persistent Menu and Ice Breakers are configured **per Instagram account** from Owned/Social Accounts settings.
- Quick Replies and Carousel templates are built as **Omni Chat Template assets** in Asset Manager, then surfaced in DMs (manually or via a rule).
- Handover Protocol lets a Primary and Secondary app (e.g. a bot and Sprinklr's agent app) pass thread control back and forth — driven manually from the engagement column or automatically via [[rule-engine]].

## Key features & how to use

### Persistent Menu for Instagram Messaging
- A fixed menu shown in the DM thread (links to FAQs, highlights, website, etc.).
- Path: New Tab icon → **Social Accounts** (under Listen / Platform Setup) → open the **Accounts** view → set the **All Channels** dropdown to Instagram.
- Find your account, click the **Options** (3-dot) icon → **Configure Your Messenger**.
- In the **Messenger Configuration** window, under **Configure Persistent Menu**, tick the **Enabled on Instagram** checkbox.
- For **Menu Item 1**, fill in:
  - **Label** — visible button text. A live character counter shows remaining of a **30-character max** (e.g. "Visit our website" showed 13).
  - **Action** dropdown — e.g. **Add URL** (then a **URL** field appears, e.g. www.sprinklr.com) or an Asset Manager reply.
- Click **Add Another Menu Item** to add more (up to **20 menu items**).
- A live mobile preview on the right shows the menu button in the DM thread.
- Click **Save** (bottom-right; Cancel beside it to discard).

### Instagram Ice Breakers
- Prompts shown to a customer on **first-time DM contact** to start the conversation; tapping one fires an automatic reply.
- Path: Sprinklr Social → **Owned Social Accounts** (under Listen) → **All Channels** filter set to Instagram → account's **Options** icon → **Configure Ice Breakers**.
- In the **Ice Breakers Configuration** window, for each **Menu Item**:
  - **Label** — the prompt text (e.g. "Hi", "Please check our menu"); has a character counter.
  - **Action** dropdown — e.g. **Select Reply from Asset Manager** (the chosen reply/asset, e.g. a menu image, shows as a thumbnail under the item).
  - Use **Add Asset** / Media Uploader to attach the reply asset where applicable.
- Click **Add Another Menu Item** for more prompts; live mobile preview on the right shows the ice-breaker chips in the thread.
- Click **Save** (bottom-right).

### Instagram Quick Replies (Omni Chat Template asset)
- Pre-set responses with action buttons for FAQs in DMs. Built as an asset, then used in the thread.
- **Limitation:** Instagram Quick Replies are **not supported on desktop** — a channel-side limitation.
- Path: Sprinklr Social → **Assets** (under Engage) → in **Asset Manager** click the **Create Asset** icon (top-right) → **Add Omni Chat Templates**.
- **Create New Asset** window:
  - **Basic Details:** Name (required) + optional Description.
  - **Asset Specific:** **Channel** = Instagram; **Template Type** = **Quick Reply**.
  - **Quick Replies** block: enter the **Message** text (required); for **Button 1** set **Label** (e.g. "Happy Halloween") and **Action** (e.g. **Send Message**). Click **Add New Button** for more buttons.
  - **Asset Details:** Campaigns (required), Sub-Campaigns, **Status** (e.g. Approved, required), Available From, Visible from, Expires on, Tags, Restricted, Brands, Persona, Customer Journey Stage, Automated Tags, Information.
  - **Asset Sharing:** pick Workspaces and Users/User Groups; tick **Visible in all workspaces** for org-wide use.
  - Set any **Properties**, then **Save** (bottom-right).
- Live mobile preview shows the message bubble with the button(s) below it.

### Create a Carousel Template for Instagram DMs (Omni Chat Template asset)
- A swipeable card template (image + title + buttons) sent in DMs; reusable like other [[asset-manager]] assets.
- Path is the same as Quick Replies: **Assets** → **Create Asset** icon → **Add Omni Chat Templates**.
- **Create New Asset** window:
  - **Basic Details:** Name (required, e.g. "Instagram Generic Template") + optional Description.
  - **Asset Specific:** **Channel** = Instagram; **Template Type** = **Carousel**.
  - **Carousel Element 1:**
    - **Upload Image** (from DAM, MediaValet, or a new upload).
    - **Title** (required, e.g. "Holiday Season") and **Subtitle**.
    - **Default Action** → **URL** (required) — where the card links when tapped.
    - **Action Button 1** — Label + Action; **Add New Button** for more.
    - Add more carousel elements as needed.
  - Complete **Asset Details**, **Asset Sharing** (Workspaces, Users/User Groups, optional "Visible in all workspaces"), and **Properties** as above.
  - **Save** (bottom-right).
- Deploy the template into an Instagram DM manually or via an automated response in [[rule-engine]]. Live preview shows the card in the thread.

### Enabling Handover Protocol for Instagram Messages
- Prerequisite for any handover (manual or rule-based). Requires config on **both** Facebook (Meta) and Sprinklr; the Instagram account must be linked to a Facebook Page.
- **On Facebook / Meta (Page admin):**
  1. Open the Facebook Page linked to the Instagram account.
  2. **Settings → Page setup → Advanced messaging → View**.
  3. Under App settings find **Messenger receiver (within Handover protocol)** → **Configure**.
  4. In the App Settings popup, click **Select** to open the **Primary Receiver** dropdown.
  5. Choose the relevant **Sprinklr App** as the primary receiver.
- **In Sprinklr** (requires access to the account-addition window):
  1. New Tab icon → **Owned Social Accounts** (under Sprinklr Social / Listen).
  2. In **Accounts (Settings)**, filter to **Instagram**, find the account.
  3. Click the row's **Options** (3-dot) icon → **Enable Handover Protocol** (sits in the menu alongside Details, Edit, Web Analytics, Link Business Account, Activity, Deactivate, Remove Account).
  - Once both sides are set, the change reflects in Sprinklr.

### Apply Handover Protocol using Rule Engine (automated)
- Path: New Tab icon → Sprinklr Social → **Manage Rules** (under Triage) → **Create New Rule**.
- In the **Rule Builder**, click the **+ (Addition)** icon → **Add Condition**.
  - Condition on **The properties of the Message** → **Has Conversation Control** — checks whether Sprinklr currently holds thread control.
- Click **+** again → **Add Action**.
  - Action changing **properties of Message** → **Conversation Thread Control**, then pick one:
    - **Request Thread Control**
    - **Take Thread Control**
    - **Pass Thread Control (As Primary to Secondary)**
    - **Pass Thread Control (As Secondary to Primary/Secondary)**
    - **Pass Thread Metadata**
    - **Release Thread Control**
    - **Extend Thread Control**
- **Save** (bottom-right).
- **Pass control on case actions (pattern):**
  - Create a custom field "Initiate Handover" (Yes/No) on **message and case**.
  - On the **Case Close macro**, set "Initiate Handover (Case CF)" = Yes and run an **On Demand Case Update** rule that copies the field from case onto the last associated fan message.
  - A **Queue rule** triggered by that custom field then performs the handover.

### Apply Handover Protocol using Engagement Column (manual)
- Prerequisite: Handover Protocol enabled (see "Enabling Handover Protocol" above).
- Path: New Tab icon → **Engagement Dashboards** (under Engage) → open your dashboard from **Engagement Home** → **Add Column** to create an Instagram DM column. See [[engagement-dashboards]].
- On a DM, open the message **Options (…)** menu (bottom-right of the message). Two handover actions appear in the action list:
  - **Pass on Control** — transfers thread control to a non-primary app. A popup opens; add notes in the **Comment** field → click **Pass** (passes to the primary receiver).
  - **Request Control** — requests control when your app does not currently hold it. Popup opens; optional **Comment** → click **Request** (requests from the primary receiver).
- (Other items in the same menu include Like, Send Heart, Open Details, Reminders, Sentiment, Email, Suggest, Update Tags, Translate, Mark as Spam, Create Case, Associate/Disassociate Cases.)

## Common issues & fixes
- **Quick Replies not appearing on desktop:** expected — Instagram Quick Replies are unsupported on desktop (channel limitation). Test on mobile.
- **Persistent Menu Label rejected/truncated:** keep labels ≤ 30 characters; the inline counter shows remaining length. Max 20 menu items per account.
- **Handover actions missing or failing:** confirm Handover Protocol is enabled on both Meta (Sprinklr App set as Primary Receiver under Advanced messaging) and in Sprinklr (Enable Handover Protocol on the account). "Request Control" only applies when your app does not already hold control.

## Notes & gaps
- Persistent Menu & Ice Breakers are per-account settings reached via the account's Options menu in Owned/Social Accounts; menu wording varies slightly ("Social Accounts" vs "Owned Social Accounts") across articles.
- Requires the relevant Instagram account already added/connected, and (for handover) linked to its Facebook Page with admin access to Meta settings.
- Handover Primary/Secondary roles are defined by the Meta-side configuration; Sprinklr acts as the receiver app set there.
- Articles do not specify exact Sprinklr permission/role names beyond needing access to the account-addition window for handover enablement.
- Carousel element count, image size/aspect limits, and Quick Reply button-count limits are not stated in the source articles.

## Sources
- Persistent Menu For Instagram Messaging — https://www.sprinklr.com/help/articles/advanced-capabilities/persistent-menu-for-instagram-messaging/6583ce31c99bc66ce07bff2f
- Instagram Ice Breakers — https://www.sprinklr.com/help/articles/advanced-capabilities/instagram-ice-breakers/640818097517d84a3aaf2fab
- Instagram Quick Replies — https://www.sprinklr.com/help/articles/advanced-capabilities/instagram-quick-replies/63e3913aa9d5117903016673
- Create a Template for Instagram Direct Messages — https://www.sprinklr.com/help/articles/advanced-capabilities/create-a-template-for-instagram-direct-messages/63ee63f4f6e2cc7d18facbbb
- Enabling Handover Protocol for Instagram Messages — https://www.sprinklr.com/help/articles/advanced-capabilities/enabling-handover-protocol-for-instagram-messages/63ee628df6e2cc7d18facbb3
- Apply Handover Protocol using Rule Engine — https://www.sprinklr.com/help/articles/advanced-capabilities/apply-handover-protocol-using-rule-engine/63eef419f6e2cc7d18facdfe
- Apply Handover Protocol using Engagement Column — https://www.sprinklr.com/help/articles/advanced-capabilities/apply-handover-protocol-using-engagement-column/63ee5ed4ef1b447d6c6318b0

Related: [[rule-engine]] · [[engagement-dashboards]] · [[asset-manager]] · [[publishing]] · [[reporting]] · [[facebook]]

# Telegram (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Telegram channel (multiple articles; see links below)

## What it is
- Telegram integration in Sprinklr Social lets brands run **bot-based** Telegram accounts to broadcast to and engage with **Channels** and **Groups** plus handle 1:1 **Direct Messages**.
- The account type is **Telegram Bot** — you connect a bot you create in Telegram (via @BotFather) using its **Bot Token**, not a personal user account.
- Use it to foster a community of fans/followers, broadcast messages directly to followers, monitor discussions, run sentiment analysis, reply to messages, and publish (with scheduling, drafts, editorial calendar, preview).
- Personas: Publishing & Engagement Agents, Community Managers, Social Media Managers.
- Reporting: SLA and Inbound reporting are available for direct messages; brand vs. fan messages are distinguished. See [[reporting]].
- Must be enabled in the environment first — work with your Sprinklr Success Manager. Listening is for **owned accounts only** (no earned/mentions).

## Key features & how to use

### Setup — Add a Telegram (Bot) account
- Prereq: Telegram must be enabled in your environment (Success Manager).
- First create a bot in Telegram to get the token:
  1. Open Telegram and message **@BotFather**.
  2. Send `/help` to see commands; send `/newbot`.
  3. Follow prompts to name the bot; **copy the API token** it generates (the Bot Token).
- In Sprinklr:
  1. New Tab icon → under **Sprinklr Social**, open **Owned Social Accounts** (within Listen).
  2. In the **Accounts (Settings)** window, click **Add Account**.
  3. In the channel picker, search/select the **Telegram Bot** tile.
  4. On the **Add Telegram Bot account** form fill the required fields:
     - **Display Name*** — the account name shown in Sprinklr.
     - **Bot Token*** — paste the @BotFather API token (format `<id>:<token>`).
     - **Upload image** (optional) — account avatar via Media Uploader.
  5. Click **Save** → continue to the **Update Account** window to configure: owner, character count, URL shortener, signature, Account Groups, User/User-Group permissions, Workspace visibility, notification subscribers, timezone, and custom properties. Save to finish.

### Channels vs. Groups
- **Channels** — one-way broadcast to followers (announcements/community reach).
- **Groups** — many-to-many conversations; inbound group messages can be filtered separately (see "Filter group messages").
- Both are brand-managed via the connected bot. Publishing targets **one channel or group per post**.

### Publishing — Publish to Telegram
- Path: top-nav **Quick Publish** icon → **Create Post**. See [[publishing]].
- Steps / fields:
  1. **Select Accounts** — pick your Telegram account (Advanced Search available to filter).
  2. **Telegram Channel/Group** — select a single channel or group (one at a time per post).
  3. **Message** — enter post text.
  4. Media (optional): choose **Photo** or **Video**; add from **DAM** or upload.
  5. **Campaign** — choose from dropdown; can set as default.
  6. **Submit for Approval** — sends for admin review before going live.
- Supported media: Photo, Video.

### Engagement — Create a Telegram column
- Prereq: the Telegram Bot account must already be added.
- Path: New Tab → **Engagement Dashboards** (Sprinklr Social → Engage) → open a dashboard → **Add Column** (top right). See [[engagement-dashboards]].
- Steps:
  1. In **Add New Column**, select **Telegram** as the source.
  2. Choose column type: **Direct Messages**.
  3. **Add New Telegram Column** dialog — enter **Name**, **Description**, **Accounts**, plus optional **Campaign**, **Sort** (e.g. Descending), **Refresh Time**, **Column Color**. A live **Column Preview** renders on the right.
  4. **Workflow Properties** — set (auto or manual): **Status**, **Assigned to**, **Priority**, **Sentiment** (also spam designation).
  5. **Custom Properties** — include/exclude messages based on applied properties.
  6. Click **Create Column**.

### Engagement — Filter group messages
Two ways to separate group messages from DMs:

- **Method 1 — Engagement Column filter (in-column):**
  1–6. Same as creating a Telegram Direct Messages column above.
  7. In the column dialog use the **Group Message** dropdown — pick **Yes** (group messages only), **No** (exclude group messages / DMs only), or **All**.
  8. Set Workflow Properties and Custom Properties as needed → **Create Column**.

- **Method 2 — Rule Engine (account-wide):** See [[rule-engine]].
  1. **Manage Rules** under **Triage** (Sprinklr Social).
  2. **Create New Rule** → enter **Rule Name** and **Description**.
  3. **Rule Scope** = Customer/Workspace; **Context** = **Inbound**.
  4. Set Activation Date and Rule Execution Batch (or defaults).
  5. **Add Condition** — under "properties of the Message" pick **Is Group Message** (set to Yes/No). The condition builder also supports **Channel is Telegram** to scope to this channel.
  6. **Add Action** on the **Yes**/**No** branches (route, assign, tag, etc.).
  7. **Save** or **Save as Draft**.

### Reporting & engagement capabilities
- Supported: view Telegram DMs, reply to Telegram DMs, distinguish **Brand Message vs. Fan Message**, SLA + Inbound reporting on DMs. See [[reporting]].

## Common issues & fixes
- **Telegram tile / option missing:** channel not enabled in the environment — contact your Success Manager.
- **No earned mentions appear:** expected — listening is **owned accounts only**; earned/mention listening is not supported.
- **Can't edit or delete a published message / manage polls:** not supported in Sprinklr. Editing DMs, deleting messages, editing a published message, and Telegram polls are all unsupported.
- **Bot won't connect:** verify the **Bot Token** is the exact `<id>:<token>` string from @BotFather and that the bot is added/admin on the target channel or group.

## Notes & gaps
- Prereqs: environment enablement (Success Manager); a Telegram bot created via @BotFather; required fields are **Display Name** and **Bot Token**.
- Account is a **bot**, not a personal account — broadcast/community style, not personal DMs at scale beyond bot rules.
- Publishing is one channel/group per post; only Photo/Video media documented.
- Limitations explicitly stated: no edit/delete of messages, no edit of published posts, no poll management, no earned-mention listening.
- Gaps (not specified in source): exact media size/format limits, scheduling/approval workflow specifics for Telegram, character limits, and supported attachment types beyond Photo/Video.

## Sources
- Add a Telegram Account — https://www.sprinklr.com/help/articles/telegram/add-a-telegram-account/658d625fc99bc66ce07c3745
- Telegram Capabilities and Limitations — https://www.sprinklr.com/help/articles/telegram/telegram-capabilities-and-limitations/658d60d1f34cb207e48be337
- Telegram Channels and Groups — https://www.sprinklr.com/help/articles/telegram/telegram-channels-and-groups/658d6049c99bc66ce07c373c
- Publish to Telegram — https://www.sprinklr.com/help/articles/telegram/publish-to-telegram/64575be90104980882a57933
- Create a Telegram Column — https://www.sprinklr.com/help/articles/telegram/create-a-telegram-column/658d6191f34cb207e48be340
- Filter Group Message for Telegram — https://www.sprinklr.com/help/articles/telegram/filter-group-message-for-telegram/658d61f8c99bc66ce07c3742

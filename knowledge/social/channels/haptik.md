# Haptik (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Haptik channel (multiple articles; see links below)

## What it is
- Haptik is a conversational-AI / chat channel you connect to Sprinklr Social as an Owned Social Account, then engage from an Engagement Dashboard column.
- It is an inbound/engagement channel: agents view conversations and reply with text or image messages, and can hand the chat back to the bot.
- Identified in the Sprinklr UI by a blue tile with a white "hand" icon, listed under both Add Account and Add Column source grids.
- Conversation flow: messages land in Sprinklr, an agent can take over and reply, or pass control back to the Haptik bot ("Assign to bot").

## Key features & how to use

### Setup — Add a Haptik account
- Prerequisite: obtain the **Client Name** and **Client ID** of a supported Haptik account before starting.
- Open the **New Tab (+) icon** under Sprinklr Social, then go to **Listen → Owned Social Accounts**.
- In the **Accounts (Settings)** window, click **Add Account** (top right).
- In the channel grid, search/select **Haptik** (blue tile, white hand icon — sits alphabetically near Google / Instagram).
- In the **Add Haptik Account** dialog, enter **Client Name** and **Client ID**, then click **Save**.
- The **Update Account** window then opens ("Update <name> Haptik Account — add important details to this Account here"). Configure:
  - **Account Details** — Account Name; **UserId** (auto-populated, read-only, e.g. 1000069229); **Owner** (required); **Custom Character Count**; **Autopopulate signature**; **Default URL Shortener** (Select…).
  - **Groups to include Account in** — Account Groups membership.
  - **Permissions** — grant channel actions to Users and User Groups.
  - **Workspace** visibility / sharing settings.
  - **Subscriber notifications**.
  - **Timezone** association.
  - **Custom properties**.
- Click **Save** to finish. See [[owned-social-accounts]], [[account-setup]].

### Engagement — Create a Haptik column
- Open an **Engagement Dashboard** from the Sprinklr Social tab.
- Click **Add Column** and select **Haptik** as the source (blue hand-icon tile in the Add New Column grid, near Trustpilot / WhatsApp Business / Sprinklr Live Chat).
- Choose a column type:
  - **Inbox** — brand and user messages.
  - **Direct Messages** — account-specific messages.
- Provide **Name**, **Description**, and select **Accounts**.
- Optional filters/config:
  - **Workflow Properties** — filter by status, assignment, priority, spam, sentiment.
  - **Custom Properties** — filter messages by applied custom properties.
- **Chat control / hand back to bot:** hover over a message and choose **Assign to bot** from the options menu to reassign the conversation to the Haptik bot. See [[engagement-dashboards]], [[engagement]].

### Engagement — Capabilities & limitations (what agents can/can't do)
Supported:
- View all conversations.
- Reply to a message.
- Reply with a text message.
- Reply with an image message.
- Pass chat control to the bot.

Not supported:
- Delete a message in a conversation.
- Edit a published post / message.

## Common issues & fixes
- **Can't find Haptik in the Add Account or Add Column grid** — use the Search box at the top of the grid; the tile is the blue square with a white hand icon.
- **Need the Client ID/Name** — these come from the Haptik side; the account cannot be added without them.
- **Trying to edit or delete a sent message** — not supported on this channel; correct by sending a new reply instead.

## Notes & gaps
- Prerequisite: a **supported Haptik account** plus its Client Name and Client ID.
- Owner is a required field on the account; permissions are granted to Users/User Groups during account setup.
- Articles do not specify character limits, attachment/file-size limits, supported media types beyond image replies, rate limits, or publishing (outbound/scheduled posting) — Haptik is documented as an engagement channel only.
- No troubleshooting/error catalogue is published; the limitations above are the only documented constraints.

## Sources
- Add a Haptik Account — https://www.sprinklr.com/help/articles/haptik/add-a-haptik-account/6909e36bb005fa4a1f133837
- Haptik Capabilities and Limitations — https://www.sprinklr.com/help/articles/haptik/haptik-capabilities-and-limitations/6909e3754bf1347217420633
- Create a Haptik Column — https://www.sprinklr.com/help/articles/haptik/create-a-haptik-column/6909e371a83b233e58bb6799

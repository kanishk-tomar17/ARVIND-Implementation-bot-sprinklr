# WhatsApp Supported Templates (Messaging 057)
**Source:** Product Foundation Courses → Messaging / 057 WhatsApp Supported Templates (video transcript + HSM template builder screenshot) · **Help:** search `site:sprinklr.com/help WhatsApp message templates HSM freeform omnichannel template builder`

## What they are
**WhatsApp message templates** are predefined message formats specified by WhatsApp, used to send notifications / customer-care messages to users who opted in. Two kinds:

### 1. HSM (Highly Structured Messages)
- **Pre-approved** templates for specific use cases — required for **business-initiated** conversations (to start a conversation on WhatsApp you can **only** use HSM templates).
- Can include text, media, and interactive elements.
- **Must be reviewed and approved by WhatsApp** before use.
- **Three categories** (different guidelines + pricing): **Utility, Marketing, Authentication.**

### 2. AMP / Freeform messages
- Used to respond to a **customer-initiated** conversation (a **service conversation**) — more flexible.
- **No pre-approval** required; businesses have full freedom in composition.

## Build an HSM template (demo)
**Path:** Digital Asset Management → **Assets** → **Create Asset** → **Omnichannel Templates** → in the **Omnichannel Template Builder**, enter asset **name + description** → **Asset Specific:** Channel = **WhatsApp Business**, Template Type = **HSM**. The Message Details window then shows **4 components**:

1. **Header Type** — **Text** (enter the text) or **Media** (image/video/document). Media input is **static** (upload) or **dynamic** (custom field).
2. **Message (body)** — body text; add **variable placeholders** with curly braces `{{1}}`, populated by **custom fields**; you're then prompted to add **sample content** (e.g. a name).
3. **Buttons** (interactive) — two kinds:
   - **Quick Reply** — multiple buttons; user picks one to send back as a response.
   - **Call to Action** — **Call** (phone number + country code → opens dialer) or **Open URL** (static or dynamic via custom field).
4. **Footer** — text appended at the end of the body.

A live **WhatsApp preview** renders on the right.

## Template Details (before saving)
- **Element name** / asset name.
- **Account Name** — the **WhatsApp Business account** to send from.
- **Language Code.**
- **Category** of the HSM template (Utility / Marketing / Authentication).
- **Save** → goes to **WhatsApp for approval**.

## Notes / gaps
- Mirrors the HSM flow in [[channels-supported]] (Journey Facilitator); requires a WhatsApp account added via [[whatsapp-account-addition]]. Placeholders use [[custom-fields]].
- Part of Messaging: [[channels-overview]], [[facebook-templates]], [[apple-messages-templates]], [[google-business-messaging-templates]].

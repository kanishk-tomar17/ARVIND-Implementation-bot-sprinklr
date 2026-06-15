# Channels Supported (Journey Facilitator 144)
**Source:** Product Foundation Courses → Journey Facilitator / 144 Channels Supported (video transcript + demo; HSM template builder screenshot) · **Help:** search `site:sprinklr.com/help journey facilitator channels HSM template create`

## Channels supported
Journey Facilitator can reach customers across multiple touchpoints. Major channels:
- **Email** — widely used, ROI-generating; personalised messages + full KPI/metric tracking.
- **SMS** — instant, real-time text even when customers are offline; promotions, discounts, updates.
- **WhatsApp** — high engagement & click-through; promotions, order lifecycle management, conversational commerce.
- **Facebook Messenger** — conversational marketing; product recommendations, audience insights, discounts, interactive quizzes — one-to-one at scale.

## HSM templates (WhatsApp)
To **initiate** a conversation as a business on WhatsApp you must use **pre-approved HSM templates** — WhatsApp only allows free-form text **within 24 hours** of a customer reaching out. Sprinklr lets you create, manage, and submit these for approval.

### Create an HSM template (demo)
1. New tab icon → **Sprinklr Marketing** tab → **Digital Asset Management** (within **Plan**).
2. In the **DAM** window → **Create Asset** (top-right) → **Omnichannel Templates**.
3. From the dropdown: **Template Type = HSM**, **Channel = WhatsApp Business**.
4. Give a **name** (this appears in the platform) + optional description.
5. **Message Details:** choose **Header Type** (None / text / image / document), add **body/content**.
   - Formatting: emojis, **bold**, *italics*, strikethrough, code.
   - **Dynamic content** via variables/custom fields: `{{1}}` (open double-curly, number, close), then below select the **custom field** whose value replaces the placeholder.
   - The **rendering window** (right) shows a real-time WhatsApp preview.
6. **Buttons** (optional) — quick replies or call-to-action. Enter a label; postback message not required.
7. **Footer** text (optional).
8. **Template Details:**
   - **Element name** — saved in Meta. **Lowercase alphabets only, no spaces, underscores allowed.**
   - **Account name** — the verbatim name of the account the template will be used with.
   - **Language code** — unrelated to actual content language but recommended to match (48+ options).
   - **Category** — if Meta classifies it differently per their norms, enabling **Automatic Category Change** auto-updates it.
9. **Save** (bottom-right) → automatically submitted to **Facebook Business Manager** for approval; track status in **Digital Asset Manager**.

(An **email marketing template** can also be created for the email channel.)

## Notes / gaps
- Templates here feed the **Send Message** node in [[journey-nodes]]; channels tie to message delivery in [[journey-builder-basics]].
- Part of Journey Facilitator: [[audience-profile-import]], [[segment-manager]], [[campaigns]], [[journey-builder-basics]], [[journey-nodes]], [[journey-reporting]].

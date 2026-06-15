# Google Business Messaging Supported Templates (Messaging 060)
**Source:** Product Foundation Courses → Messaging / 060 Google Business Messaging Supported Templates (video transcript + GBM Rich Card builder + template-type dropdown screenshot) · **Help:** search `site:sprinklr.com/help Google Business Messaging templates rich card carousel quick reply`

## What they are
**GBM message templates** add enhanced, structured content rendered in the **Android Messages app**. Four types covered: **Quick Reply, Rich Card, Rich Card Carousel, Rich Text.**

## Common build path
Open a new page → **Digital Asset Management** → **Create Asset** → **Omnichannel Templates** → basic details (name) + **Channel = Google Business Messaging** → choose **Template Type** (Card / Carousel / Quick Reply / Rich Text).

## 1. Quick Reply template
Predefined response options — customers select instead of typing. Includes **suggested replies** and **suggested actions**. Use cases: FAQs, order-status updates, appointment confirmations, feedback collection.
- **Body:** plain text only.
- **Quick reply buttons:** types include **Open URL** and **Call**; also a **suggested reply** (not an action).
- Add a **postback message**; **min 2, max 10** quick replies; each has a **label** + postback message.
- Asset details (campaigns, expiry) → **Save**.

## 2. Rich Card template
Send multiple units of info in one card — structured, interactive. Use cases: product showcase, travel/accommodation, appointment bookings, updates/reminders.
- **3 main components:** **Title**, **Image**, **Buttons**.
- **Fallback text** — sent if the card doesn't render properly.
- Upload the **image** (per desired look/feel); set **image height**.
- **Buttons (max 4):** **Action button** (currently only **Open URL** — add a link + postback message) or **Simple button** (sent back as a response on click).
- Asset details → **Save**.

## 3. Rich Card Carousel
A series of cards swiped **horizontally**; each card is self-contained (images, text, buttons) — lets users compare items and interact individually. Use cases: product showcase, inventory lookups, step-by-step guides, subscription plans.
- **Min 2, max 10** rich cards; each can contain buttons.
- **Build:** name/description + Channel = GBM + Template Type = **Carousel** → select **card width** (e.g. Medium) → enter **fallback text** → configure each card.

## 4. Rich Text
Rich-text asset type (also available in the template-type list).

## Notes / gaps
- Requires a GBM account added via [[google-business-messaging-account-addition]]; built in the same Omnichannel Template Builder as the other channels.
- Part of Messaging: [[channels-overview]], [[whatsapp-templates]], [[facebook-templates]], [[apple-messages-templates]].

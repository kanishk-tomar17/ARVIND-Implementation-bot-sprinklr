# Apple Messages for Business (Sprinklr Social — Channel)
**Source:** sprinklr.com/help — Apple Messages for Business channel (multiple articles; see links below)

## What it is
- Apple Messages for Business (AMB) lets brands talk to customers inside Apple's native Messages app on iPhone, iPad, Mac, and Apple Watch — handled in Sprinklr as a [[social]] messaging channel.
- Two-way conversational messaging: customers reach out from Maps, Safari, Spotlight, Siri, or a brand's website/app, and agents reply from the Sprinklr [[care-console]] / [[engagement-dashboards]].
- Rich, native experience: text/rich text, images, documents, audio, video, GIFs, emojis, link/rich-link previews, plus delivery and typing indicators.
- Supports an authentication flow so customers can verify identity in-thread.
- Built for assisted service — not for outbound broadcast/[[publishing]]; conversations are customer-initiated.

## Key features & how to use

### Capabilities and limitations
Supported message types (what can flow in each direction):

- **Sent and received (both ways):**
  - Text / Rich Text messaging
  - Link / Rich Link — a rich link renders an inline preview card instead of a bare URL (see screenshot behavior below)
  - Images
  - Documents
  - Emojis
  - Audio files
  - Videos
  - GIFs
  - Delivery Indicator (shows message delivered)
  - Typing Indicator (shows the other party is typing)
- **Received only (customer can send, agent cannot send back):**
  - Location sharing
  - Stickers

Other capabilities:

- **Authentication** — supported as an in-conversation capability for verifying the customer.
- **Auto-close reply box on conversation deletion** — there is an option to "automatically close the reply box when the customer deletes the conversation from their end." This is **not self-serve**: coordinate with your Sprinklr Success Manager to enable it.

Limitations (call these out to clients up front):

- **No editing a published/sent post** — once a message is sent it cannot be edited.
- **No consumer name** — the customer's name is not exposed on the profile.
- **No consumer image** — the customer's profile picture is not available.
- Location sharing and stickers are **inbound-only** — agents cannot send them.

### Rich link behavior (URL handling)
- When a message contains a URL embedded in longer text, Sprinklr automatically **splits it into 3 separate messages** and generates a rich-link preview card, instead of sending one long block with a raw URL.
- Confirmed by the article screenshot:
  - **Before:** one bubble — "Please find the link to the product page: https://www.apple.com/ipad. Let me know if you have any questions." (plain inline URL).
  - **After:** three bubbles — (1) "Please find the link to the product page", (2) a rich-link card showing the page image with title "iPad" and source "apple.com", (3) "Let me know if you have any questions."
- Net effect: cleaner threads and a native link-preview card rather than an unbroken paragraph with a URL in the middle.

## Common issues & fixes
- **"Why can't I edit a message I just sent?"** — AMB does not support editing sent messages. Send a correction/follow-up message instead.
- **"Customer's name/photo isn't showing."** — Expected: AMB does not provide consumer name or consumer image. Identify the customer via the conversation/authentication flow, not the profile fields.
- **"My single message turned into 3 bubbles."** — Expected behavior when a URL sits inside longer text; Sprinklr splits it to render a rich-link preview. Not a bug.
- **"I can't send a sticker / share location back."** — These are receive-only on AMB; there is no agent-side send for them.
- **Reply box not auto-closing when a customer deletes a conversation** — that toggle isn't self-serve; raise it with your Success Manager to enable.

## Notes & gaps
- **Prerequisites/permissions:** Standard Sprinklr Social channel onboarding applies (brand must be registered for Apple Messages for Business and the account connected in Sprinklr); the source article does not detail the registration/connection steps — confirm with the channel-setup docs / Success Manager.
- The auto-close-reply-box option requires Success Manager involvement (not in-product self-serve).
- **Not covered by this source article (gaps):** no specific character limits, file-size limits, or media format/codec constraints are stated; reporting/analytics metrics for AMB are not detailed; routing/assignment, bot/[[ai-studio]] handoff, and SLA setup are out of scope here — see the general [[engagement-dashboards]], [[rule-engine]], and [[reporting]] KB. Treat any specific limit numbers as unverified until confirmed against the live channel.
- Only one source article was available for this channel; the file should be expanded if Sprinklr publishes setup/reporting articles for AMB.

## Sources
- Apple Messages for Business — Capabilities and Limitations: https://www.sprinklr.com/help/articles/apple-messages-for-business/apple-messages-for-business-capabilities-and-limitations/64525dcef65d86626c825590

# Live Chat Customisation (Live Chat 087)
**Source:** Product Foundation Courses → Live Chat / 087 Live chat customisation (video transcript) · **Help:** search `site:sprinklr.com/help live chat builder personalize customization WCAG`

## Scope
UI customisation via the **Live Chat Builder**, what needs a **support ticket** instead, and **WCAG** compliance.

## Live Chat Builder — "Personalize your live chat"
Open Launchpad → Live Chat Care → edit the application → **Personalize your live chat**.

### Trigger icon
- **Theme colour** — colour picker or standard colours.
- **Icon / logo** — choose from 6 preset logos or upload a **custom image**.
- **Chat icon text** — text on the trigger icon (**hidden on mobile**, icon only, to save space).
- **Collapse icon** — X or Chevron.
- **Background** — custom pattern or a colour.
- **Positioning** — left/right, plus **padding** from bottom/left (or bottom/right).
- **Availability/visibility** of the trigger icon (e.g. always show).

### Home screen
- Brand **logo**, custom **title + description**.
- **New conversation card** — an **HTML component**, highly customisable; edit verbiage on the starter/new-conversation tab; add custom images.
- **History position** toggle — show history at the **bottom** (toggle on) vs the default **top**.
- **Home-screen actions** (under three dots): e.g. maximise, clear session.

### Conversation screen
- Header **title + description** (logo auto-inherited from home page).
- **Welcome messages** and **conditional welcome messages**.
- **Assets** supported: card asset, **carousel** asset, **contact forms** (via the Asset Builder).
- **Chat actions** (three-dot) — configured here; appear **after the first message** is sent.
- **Reply box** text placeholder; **character limit** (shown in UI).
- **Disclaimer banner** — your disclaimers; can be **dismissible or persistent**.
- **Dynamic wait time / queue position** placeholders — based on the work queue + assignment logic, so customers see expected wait.
- **Contact form** — capture customer details before chat starts (asset from Asset Builder).
- **Persistent menu** (three dots) — options like main menu, video call; the exact match is **sent as a message** to the brand, then a **Conversational AI bot** configures the next steps.
- **Restrict attachment types** the user can send.
- **Agent/bot persona image** — show **initials** or the agent's Sprinklr profile picture; bot persona configurable separately.
- **Update application**, then verify on the **UAT URL**.

## Beyond the Builder → raise a support ticket
For customisations the Builder can't do, raise a support ticket with partner/application/environment details and any specific **hex codes / pixel sizes**:
- Self-help apps (Status / KB / Guided Workflow cards) configured from the **back end**.
- **Custom fonts** for the whole chat.
- Trigger-icon **attention effects / borders**.
- App **height/width**, **chat bubble colour**, **persona image** updates.

## WCAG compliance
**WCAG** (Web Content Accessibility Guidelines, by W3C) is the accessibility benchmark.
- Example: font colour is auto-chosen **white or charcoal** based on the background colour to meet WCAG **contrast ratios**.
- Online tools let you check whether a foreground/background pairing complies with the required contrast ratio.

## Notes / gaps
- Builder covers most branding; anything outside it (fonts, exact dimensions, home-screen self-help cards) is a **back-end/support-ticket** task — set client expectations accordingly.
- Persistent-menu options route into a [[../conversational-ai/dialogue-tree-basics]] bot flow.
- Always validate changes on the **UAT URL** before production.

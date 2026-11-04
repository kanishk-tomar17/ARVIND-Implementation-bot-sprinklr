# Custom Fonts — Live Chat & Surveys (Typography)

**Self-serve. Does NOT require a support ticket.** Custom fonts are uploaded once as a
**Font Family asset** in Digital Asset Manager, then selected from a font dropdown in the
Live Chat Builder and/or the Survey Builder.

Sources:
- https://www.sprinklr.com/help/articles/typography/configure-custom-fonts-in-live-chat/6757f183dcbeed48d002a82f
- https://www.sprinklr.com/help/articles/survey-styling/leverage-custom-fonts-to-brand-the-surveys/695d44562727657ea2626647

## Step 1 — Upload the font (Digital Asset Manager)
Universal Search → **Digital Asset Manager** (or Assets in Sprinklr Social) → **Create Asset**
→ **Advanced Options → Font Family**.
- Enter **Name** + **Description**.
- **Asset Specific** section: set **font style** (`normal`) and **weight**
  (`400` = regular, `700` = bold).
- Upload the font file, or **submit a URL** if the font is hosted online.
- **Save.**

**Supported formats:** `.WOFF`, `.WOFF2`, `.ttf`, `.otf` — or a hosted URL.

**Key limitation:** *one Font Family asset = one font.* Each weight/style (regular, bold,
italic) must be uploaded as its **own** asset. Budget one upload per weight you actually use.

**Licensing:** confirm you hold the licence before uploading a proprietary font. Open-source
faces (Google Fonts / SIL OFL — e.g. **Figtree**) are safe to upload directly.

## Step 2a — Apply in Live Chat
Sprinklr Service → **Live Chat Care** (under Brand Care) → **Live Chat Builder** →
**Personalize Your Live Chat** → **Typography** → select the custom font family.
- You can list **2–3 fonts in order of preference** (fallback chain).

## Step 2b — Apply in a Survey
Open the **Survey Builder** → select the text element → **font selection dropdown** →
pick the font (custom uploads carry a **"custom"** label).
- **Preview** to verify rendering across devices before publishing.

## What *does* need a ticket
Configuring **system fonts as a fallback** — raise at `tickets@sprinklr.com`.
Custom font upload/selection itself does not.

## Gotchas
- Font not in the dropdown → the asset didn't save, or it was created in a **different
  environment/partner**. Font Family assets are per-environment: uploading in prod does not
  make the font available in a testing partner. Upload it in the environment you're styling.
- A survey embedded in a Live Chat app is styled in the **Survey Builder**, not the Live Chat
  Typography panel — the two are configured separately.

Related: [[customisation]] · [[builder]] · [[basics]]

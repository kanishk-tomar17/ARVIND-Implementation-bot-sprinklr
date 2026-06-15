# HTML Email Templates (Email Care 138)
**Source:** Product Foundation Courses → Email Care / 138 Email templates (video transcript + demo) · **Help:** search `site:sprinklr.com/help HTML email templates platform email templates`

## What it is
**HTML email templates** = pre-designed structures/layouts (coded in **HTML + CSS** within Sprinklr) for visually consistent, branded emails — can include images, buttons, links, formatting. Because the code is HTML/CSS, **involve the development team** for any changes.

## Enablement (two DPs)
- **HTML email templates are NOT enabled by default** — raise a **support ticket** to enable them for the partner. Without it, emails go as **plain text body** (no template).
- To **access/edit** templates from the UI, also enable the DP **"Customized Sprinklr email templates"** → then **All Settings → Manage Customer → Platform Email Templates** appears.

## The two templates to customize
There are many templates, but only **two** matter for branding:
1. **Email Message Forward Event** — when forwarding an email / proactively sending the first brand message.
2. **Email Message Reply Event** — when replying to a customer's email.
Each has a **default** HTML template (preview shows email body, account name, etc.); edit to add brand logo, colors, etc.

## CRITICAL safety process
- **Bad HTML/CSS breaks the email flow** — no emails will send (grabbing & publishing break) for the partner. Be extremely careful.
- **Process:**
  1. Get the customer's **sample HTML file** to replace the template with.
  2. **Make changes in the DEV environment first** (enable the DP in dev) — edit the two events (Forward, Reply).
  3. **Test exhaustively** — send and grab emails in dev; confirm templates don't break grabbing/publishing.
  4. Only then **replace the templates in production**.
  5. Make the production change during the **brand's off-business hours** (ask the brand for these).

## Notes / gaps
- Heavily gated by DPs + support tickets; dev-first + off-hours deployment is the key safety guidance. Relates to Sandbox dev/staging best practices ([[alm-best-practices]]).
- Completes Email Care: [[account-types]], [[webforms-external-gw]], [[email-signature]], [[email-collaboration]], [[manual-case-merge]], [[ignore-duplicate-autoresponse]].

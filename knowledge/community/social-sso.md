# Social / Single Sign-Ons (Community 187)
**Source:** Product Foundation Courses → Community / 187 SocialSingle Sign Ons (video transcript + demo) · **Help:** search `site:sprinklr.com/help community login providers SSO social sign on`

## Login methods for a community
1. **Email ID + password** (native)
2. **Single Sign-On (SSO)** — SAML-based, brand's existing login across portals
3. **Social Sign-On** — login with Google / Facebook / Twitter / LinkedIn
4. **OAuth login** — fully custom client implementation

All are enabled in **Community Builder → Edit → Content Settings → Login Providers**, then **Save → Full Page Preview → Publish**.

## 1. Email ID + password
Content Settings → Login Providers → enable the **Email ID & password** toggle → Save → publish.

## 2. Single Sign-On (SAML)
1. Follow the **SSO checklist** (from the project repository docs). Sprinklr provides: **Sprinklr entity ID, Sprinklr public key certificate**; the customer provides the rest.
2. **All Settings → Manage Customer → search "Single Sign-On" → Add Single Sign On** → for SAML: name it, fill **Entity ID, Issuer name, Identity Provider Login URL**, and the other checklist details → **Save**.
3. **Community Builder → Content Settings → Login Providers** → enable the SSO toggle, select the configured SSO app → Save → Full Page Preview → Publish.

## 3. Social Sign-On (Google/Facebook/Twitter/LinkedIn)
1. **Client sets up the app** on the respective platform (e.g. a Google Developers account + social sign-on app) and shares the **App Key** and **App Secret**.
2. **All Settings → Social Sign-Ons → Create Social Sign On** → pick profile type (e.g. Google), give an **App title**, enter **App key** + **App secret** → Save.
3. **Community Builder → Content Settings** → enable **Social** → select the Facebook/Google/Twitter/LinkedIn app → Save → Full Page Preview → Publish.

## 4. OAuth login
- Custom client implementation; client shares **documentation, API key/secret, and domain whitelisting**. **Requires back-end development → onboard the Product team.**
- After back-end config: Community Builder → Content Settings → enable **OAuth** → select the OAuth app created in back-end → Save → Full Page Preview → Publish.

## Notes / gaps
- All login providers are toggled in Community Builder Content Settings ([[community-builder]]); SSO/social-sign-on apps are configured under All Settings (customer level — see [[customer-vs-workspace]]).
- Part of Community: [[community-builder]], [[global-workspace-roles]], [[message-level-rules]], [[live-chat-on-community]], [[guided-workflow-on-community]], [[spam-model]], [[case-management-for-community]], [[survey-on-community]], [[support-ticket]], [[community-reporting]].

# Chat Deflection — Social → Live Chat (Live Chat 088)
**Source:** Product Foundation Courses → Live Chat / 088 Chat deflection (video transcript) · **Help:** search `site:sprinklr.com/help social to live chat deflection one-time URL dynamic link asset`

## What it is
**Social → Live Chat deflection** moves a customer from **any social channel** to the **more secure Sprinklr Live Chat**. The deflected case stays **associated to the original social case** (one case across channels).

## Why deflect
- Customers share **PII** (account number, credit card, address, phone) on social, but **legal mandates restrict soliciting personal info on social channels** → a secure chat is necessary.
- Also to start a **video call / co-browsing** session or use other live-chat-specific features.

## UX journey
1. During a social interaction, the agent realises they need **sensitive info**.
2. Agent sends a **unique link** via the social channel.
3. Customer clicks → redirected to a **live chat window**, resumes with the agent.
4. The agent retains **full context** of the prior social conversation.
- *Demo:* social case "block my credit card" → can't ask PII on social → agent sends the deflected live-chat URL as a **canned response** → customer opens it → now in Live Chat, conversation **associated to the original social case**.

### With authentication (optional)
Brands can add an **auth step** between social and live chat (to verify identity or pull **CRM data**): customer is redirected to the **brand login page**; after login, Sprinklr gets an alert and the brand can share additional user info to Sprinklr.

## URL types (two)
- **One-time URL** — **device+browser restricted** (first click locks it to that device-browser combo) and has an **expiration time**. Note: once opened within expiration on a combo, it stays accessible on **that same combo** afterward regardless of expiry.
- **Generic URL** — **no** device/browser or time restriction; open any device/browser anytime.

## Enablement — two implementation scenarios
- **Sprinklr-hosted page:** brand/IC creates & configures the live chat app in Sprinklr; field team raises a support request to create a **live chat custom page**; support creates it and shares a **sprinklr.com URL**. Optionally use the brand's **own domain** via **CNAME mapping** + sharing the subdomain's **SSL certificate**. Support then creates a **dynamic link asset** to send to customers.
- **Brand-hosted live chat:** brand configures the app in Sprinklr; Sprinklr shares the **embed (JavaScript) code**; brand builds a custom page and embeds the JS to host live chat; brand passes the **token** (received in the query parameter, carrying case info) **back to Sprinklr** to identify the associated case. Support then creates the dynamic link asset.

## Landing-page customisations (via support)
Provide to support: **favicon**, **brand logo**, **background colour/text**, **page background**, and the **live chat** (Builder customisations carry through). The **chat header is not shown** on the hosted page (redundant — covered by the page header).

## Creating/publishing the deflection asset
Sent either via a **dialogue-tree macro** or an **agent canned response** — choose first, since steps differ:
- **Via macro** — when the deflection verbiage is **standard** and you also want extra actions (run rules, update custom fields): the agent runs the rule via macro, the asset is sent via Conversational AI, plus the additional steps run.
- **Via canned response** — when you want to **personalise the verbiage** and need no extra actions (the demo used this).
- **Asset creation:** make a **simple text** asset with the **deflection link placeholder**; create a **deflection node** in the Conversational AI application and use a **macro** to send it (or send via canned response). **Only the back-end team creates the link asset** — provide the verbiage to support.

## Notes / gaps
- Distinct from the bot [[../conversational-ai/dialogue-nodes-advanced]] deflect node (general multi-channel); this is the **security-driven social→live-chat** pattern with case association preserved.
- One-time vs generic URL is the key security decision — one-time for sensitive PII flows.
- Dynamic link assets are **back-end/support-created**; consultants supply verbiage + branding details.

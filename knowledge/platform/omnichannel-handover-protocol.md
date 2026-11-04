# Omnichannel Handover Protocol

**Source:** [Sprinklr Help — Omnichannel Handover Protocol](https://www.sprinklr.com/help/articles/api/omnichannel-handover-protocol/64832193723d925979db8cd4) (Platform > Integrations > API)

## What it is
Lets any **external 3rd-party bot** participate in a conversation with a customer on Modern Messaging channels, and hand the conversation off between the bot and a live agent (or vice versa). Used when a brand runs its own/external bot for automated responses and wants to pass control to Sprinklr for live-agent servicing when needed.

## Prerequisites to implement
1. **Bot integrated into Sprinklr** — the external bot must be integrated via Sprinklr's APIs before this works (this is dev work on the bot/RaptorCX side, not a platform toggle).
2. **Sprinklr Developer Portal access** — required to get the API access needed for integration.

## Core capabilities / what "implemented" looks like
1. **Pass Control API** — transfer conversation control from bot → Sprinklr (or vice versa).
2. **Acquire Control API** — a participant takes over conversation management.
3. **Release Control API** — bot returns control to the primary participant.
4. **Rule Engine configuration** to automate control handoff:
   - Queue setup
   - Rules with Pass / Acquire / Release actions
   - Macros configured for on-demand execution
   - Case macros applied within Engagement Dashboards

## Supported channels
Facebook, WhatsApp, Twitter/X, Instagram, Line, Kakao Talk, Apple Business Chat, Google RCS, WeChat, Sina Weibo, Viber, Sprinklr LiveChat.

## Readiness checklist (for verifying a client's environment)
- [ ] Target channel (from list above) is connected/enabled for the partner.
- [ ] Developer Portal access exists for the partner/team doing the integration.
- [ ] External bot is registered/integrated against Sprinklr's Pass/Acquire/Release Control APIs.
- [ ] Queue exists for handled conversations.
- [ ] Rule Engine rules exist with Pass/Acquire/Release actions wired to that queue.
- [ ] Macros for on-demand control actions are configured and applied in Engagement Dashboards (case macros).

## Notes / gaps
- Distinct from the **Handover Function Tool** (Sprinklr AI Agent > Route Tools) — that's an *internal* AI Agent task-router (Router / Customer Profile Overview / Summarizer), not for external bot handoff. Don't confuse the two.
- Article doesn't detail Developer Portal onboarding steps themselves — if that's the blocker, likely needs a Sprinklr support ticket.

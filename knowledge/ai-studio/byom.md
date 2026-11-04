# BYOM — Bring Your Own Model (AI+ Studio)
**Source:** https://www.sprinklr.com/help/articles/add-support-for-byom/get-started-with-byom-in-ai-studio/6717c5932e64c74e571fe316 · also `.../implementation-steps-for-byom-in-ai-studio/68ac3393a2245b36104906fe`

## What it is
Point Sprinklr's AI+ Studio at **your own hosted LLM endpoint** instead of a Sprinklr-provided model. Sprinklr is LLM-agnostic; BYOM is how a customer plugs in an internally developed/hosted model.

## Prerequisites
- A **working API endpoint** for the model, compatible with Sprinklr's backend (Sprinklr can supply an adapter if the format differs).
- Documentation of input format, response structure, and a sample request/response.
- **The endpoint must support function/tool calling** — otherwise Sprinklr's Agentic AI capabilities can't use it.

## Limits / gotchas
- **It's for LLM endpoints, not for arbitrary APIs or finished chatbots.** A packaged bot API (message in → reply out) is NOT a BYOM candidate.
- **You cannot mix Sprinklr AI and BYOM/BYOK in the same deployment** — it's a deployment-wide choice.
- Model selection is at **use-case / agent / copilot level**; no dynamic runtime switching.
- The customer owns hosting, maintenance, compute cost, latency and model accuracy.

## When NOT to use it
If the requirement is "route a customer message to an external bot and return its reply", BYOM is the wrong tool — use a **Conversational AI app with an [[../conversational-ai/api-node]]**, or middleware in front of the **Omnichannel Handover Protocol** (https://www.sprinklr.com/help/articles/api/omnichannel-handover-protocol/64832193723d925979db8cd4). See `documents/hayya-external-bot-on-sprinklr-whatsapp-options.md`.

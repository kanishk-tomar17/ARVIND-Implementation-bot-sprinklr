# Sprinklr Specialised AI Service Features (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-service-specialized-ai-use-cases/sprinklr-specialised-ai-service-features/69415868041df6338a0317fa

## What it is
- A catalog of Sprinklr's purpose-built (specialised) AI features for Sprinklr Service, combining generative AI with enterprise governance and security.
- Spans five domains: **Agent Assist**, **Conversational AI**, **Conversational Analytics**, **Outbound Voice**, **Workforce Management**.
- Most features are "On Request" — they must be enabled by Sprinklr (Support/Success) rather than self-served; a few are on by Default.

## When to use
- You need a quick reference for which Service AI feature exists, where it lives in the UI, and what's needed to turn it on.
- Scoping an implementation: deciding whether a capability is Default vs needs a Sprinklr request, and what permission gates agent access.
- Confirming whether a feature is configured via **AI+ Studio** (only AI Autofill is) vs standard Service settings.

## Configuration steps
This article is a feature/enablement matrix, not a step-by-step setup guide. Per feature, "Configuration" means: confirm enablement path, grant the access control, then find it at the stated location.

1. **Agent Assist** (augments agents in the Care Console)
   - Smart Compose — On Request; user-level toggle; Care Console reply box.
   - Similar Cases — On Request; needs All & View permission; Smart Assist tab.
   - Smart Paraphraser — On Request; needs Outbound Execution permission; Care Console reply box.
   - Agent Nudges — On Request; needs View & Edit permission; Care Console.
   - Predictive CSAT — Default (no permission needed); shown in side-pane properties.
   - Response Compliance — On Request; enabled via checkbox settings; Care Console reply box.

2. **Conversational AI** (NLP to understand and engage customers)
   - ASR (speech recognition) — On Request; shared across IVR, Voice Bot, AQM.
   - Text to Speech — On Request; shared with IVR, Voice Bot.
   - Intent Detection — Default; needs Conversational AI permission; Persona App Intent Models.
   - Entity Detection — Default; needs Conversational AI permission; Persona App Intent Models.
   - Discovery Run — Default; needs Conversational AI permission; Persona App Intent Models.

3. **Conversational Analytics** (insight from conversations)
   - Predictive CSAT — On Request; no permission needed; Reporting & Case Analytics.
   - Voice Acoustics — On Request; no permission needed; Reporting & Case Analytics.

4. **Outbound Voice** (planned outbound campaigns)
   - Answering Machine Detection (AMD) — On Request; enable via AMD checkbox; Service > Voice > Campaign.
   - Predictive Dialer — On Request; no permission needed; Service > Voice > Dialer.
   - AI Autofill — On Request; configured in ACW settings; Service > Voice > ACW. **Only feature built in AI+ Studio.**

5. **Workforce Management** (scheduling and forecasting)
   - Scheduling — On Request; Persona App.
   - Forecasting — On Request; Persona App.

## Notes & gaps
- This is a **reference matrix**, not a procedure guide — it does not give field-by-field setup. For actual build steps, drill into each feature's own KB article.
- "On Request" = raise with Sprinklr to provision; you cannot self-enable.
- Access controls are permission names you must grant on the relevant role (e.g. Conversational AI, Outbound Execution, All & View, View & Edit) before agents see the feature.
- Only **AI Autofill** uses AI+ Studio; the rest are configured in standard Service/Persona settings.
- Built on a secure, compliant framework; key benefits cited: real-time insights, faster resolutions, consistent brand voice, automated content generation, smart routing, predictive analytics.
- Related GROOT topics: [[intents]], [[entity-detection]], [[care-console]], [[predictive-csat]], [[voice-bot]], [[ivr]], [[ai-studio]], [[rule-engine]], [[persona-app]].

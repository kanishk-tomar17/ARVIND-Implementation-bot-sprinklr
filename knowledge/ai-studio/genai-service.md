# Sprinklr Service Generative AI Use Cases (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/sprinklr-service-generative-ai-use-cases/sprinklr-service-generative-ai-use-cases/697b7208c0c0b637f94b208f

## What it is
- A catalog of the generative-AI features inside Sprinklr Service, grouped by module.
- Purpose: help agents work faster, respond quicker, and handle cases more accurately.
- Each feature has its own enablement path — usually module enablement plus one or more Dynamic Properties (DP).

## When to use
- Boosting live agent productivity (draft replies, summarize cases, auto-fill after-call work).
- Building or upgrading bots with GPT-driven workflows, intent/entity detection, or Smart FAQ.
- Generating analytics/insights from conversations (contact drivers, topics, interaction phases).
- Auto-generating or gap-checking knowledge base content.
- Automating QA scoring across interactions.

## Generative AI features by module

### Agent Assist (real-time agent productivity)
- **Smart Comprehend** — understands conversation context. Requires DP + extra config.
- **Smart Responses** — drafts customer replies. Requires DP + extra config.
- **Case Summarization** — generates interaction summaries. Requires DP + extra config.
- **ACW Prefill** — auto-populates after-call work forms. DP: `_SCREEN_AI_PREFILL_ENABLED=True`.

### Conversational AI (bot building)
- Dynamic Workflow nodes
- Processing Node (single-shot dynamic workflows)
- Zero Shot Intent and Entity Detection
- Smart FAQ models
- Voice Bot Speech to Speech
- All require DP: `_CONVERSATIONAL_AI_GPT_FEATURES_ENABLED=True`.

### Conversational Analytics (insights)
- Interaction Summary & Topics
- Top Contact Drivers
- Contact Driver Discovery
- Interaction Phase Analysis
- Insights Hub: statistical trends, product/service insights, agent quality, contact drivers.

### Knowledge Base (content generation)
- KB Gap Analysis — auto-enabled.
- Brainstorm Ideas
- Community Post Nomination — auto-enabled.

### Quality Management
- Automated Quality Management — requires DP + extra config.

## Configuration steps
1. **Enable the parent module** for the feature you want (the feature won't work until its module is on).
2. **Set the required Dynamic Property (DP).** Common ones:
   - Conversational AI features → `_CONVERSATIONAL_AI_GPT_FEATURES_ENABLED=True`
   - ACW Prefill → `_SCREEN_AI_PREFILL_ENABLED=True`
   - Agent Assist (Smart Comprehend / Smart Responses / Case Summarization) and Automated QM → DP plus additional config (contact Sprinklr Support).
3. **Complete any additional setup** the feature needs (prompts, model selection, guardrails) where supported.
4. **Set access via Feature Access Management:**
   - Most features: enable/disable + RBAC.
   - Select features: enable/disable only (no RBAC).
   - Some capabilities sit outside Feature Access Management entirely.
5. **Auto-enabled features** (KB Gap Analysis, Community Post Nomination) need no DP — available once the module is on.

## Notes & gaps
- Article is a feature index, not a deep how-to — exact DP/config detail per feature is light; Sprinklr directs you to **contact Sprinklr Support** for setup help.
- **AI Configuration Support varies:** some features allow prompt editing, model selection, and guardrails; others don't.
- DP-gated features only work if their parent module is enabled first.
- RBAC is not supported on every feature — check before relying on role-based gating.
- Related ARVIND topics: [[intents]], [[faq-bots]], [[bot-rule-setup]], [[custom-fields]], [[rule-engine]], [[case-summarization]], [[knowledge-base]], [[quality-management]].

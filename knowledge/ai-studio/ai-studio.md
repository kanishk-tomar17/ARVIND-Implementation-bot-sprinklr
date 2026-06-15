# AI+ Studio (Sprinklr AI — AI+ Studio)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/ai-studio/ai-studio/696794a5779326190325a833

## What it is
- Centralized workspace in Sprinklr for building, managing, and monitoring AI across the platform.
- A single environment to integrate, govern, and scale AI operations securely and responsibly.

## When to use
- You need one place to set up and govern AI providers/models (Sprinklr-provided LLMs, your own provider keys, external APIs, or in-house models).
- You're deploying an AI feature and want to test and audit it before/while it runs.
- You need PII masking and safety guardrails (harmful-content detection, prompt protection, protected-material filters) on AI prompts.
- You want to customize Copilots (AI assistants) for agent/workflow productivity.
- An admin needs to control which generative-AI features are available, toggle them on/off, and manage user access.

## Configuration steps
The article is an overview only — it does not document step-by-step setup. It describes five capability areas inside AI+ Studio:

1. **Providers and Models** — set up/manage AI providers. Options:
   - Use Sprinklr-provided language models.
   - Bring your own provider keys.
   - Integrate external APIs.
   - Use proprietary in-house models.
2. **AI Use Cases** — deploy AI features with built-in testing and audit to keep outputs accurate.
3. **Security and Compliance** — apply PII masking templates and safety guardrails (harmful-content detection, prompt protection, protected-material filters) that attach to prompt nodes.
4. **Copilots** — customize AI assistants to streamline workflows and decision-making.
5. **Feature Access Management** — admin control center to view feature availability, enable/disable specific generative-AI features, and manage user access with custom configurations.

## Notes & gaps
- This KB article is thin: it lists capabilities but gives no prerequisites, no field-level detail, no ordered setup steps, and no stated limitations. For actual configuration, drill into each sub-area's own help article.
- Feature Access Management is admin-gated — managing availability and user access requires admin permissions.
- Guardrails and PII masking attach at the prompt-node level, so they apply per AI use case rather than globally.
- Related GROOT topics: [[intents]], [[faq-bots]], [[bot-rule-setup]], [[custom-fields]], [[rule-engine]]

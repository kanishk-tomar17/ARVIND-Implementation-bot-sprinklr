# Sprinklr AI Agent (Sprinklr AI — AI Agents)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/manage-ai-agents/sprinklr-ai-agent/6978b125c836550ff8e79418

## What it is
- A unified builder for designing, configuring, and deploying AI-powered virtual agents that automate tasks and respond to users across digital channels.
- One interface to manage the agent's behavior, workflows, knowledge sources, and system settings.

## When to use
- Automate customer interactions across digital channels (text and voice).
- Deflect repetitive tasks/queries and improve operational efficiency.
- Deliver consistent, on-brand responses driven by your own knowledge content.

## Configuration steps
The article describes the agent's configurable components, not a click-by-click UI walkthrough. The components you set up:

1. **Manage Persona** — define how the agent communicates: tone, communication style, and behavioral traits.
2. **Discover Tasks and Tools** — analyze historical conversation data to surface automation opportunities (which tasks the agent should handle).
3. **Add Knowledge Content** — upload the sources the agent answers from (RAG):
   - FAQs
   - Documents
   - Websites
   - Knowledge articles
4. **Configure Content Instructions** — set rules governing how the agent uses that content:
   - Language and response behavior
   - Tone
   - Sensitivity / handling protocols
5. **Define Tasks and Tools** — build structured workflows:
   - **Tasks** = structured workflows combining prompts and logic.
   - **Tools** = individual actions the agent can trigger (including integrations).
6. **Admin Panel** — system-level settings:
   - Timeout behavior when users don't respond
   - Voice settings (speech output, voice prompts, interruption handling, intent detection)
   - Trigger applications directly (launch without separate rule setup)
   - Industry selection
   - AI version selection
   - LLM configuration
- **Audit Logs** record every significant system and user action, for compliance and troubleshooting.

## Notes & gaps
- This help article is capability-focused — it lists what each section does but does NOT give exact navigation paths, field-level toggles/dropdown values, or explicit deploy/publish and testing steps. For a click-by-click build, see the category page (sprinklr.com/help/categories/sprinklr-ai-agent/) or RaptorCX training; do not invent the missing UI steps.
- No prerequisites, permissions, or technical limits are stated in the article.
- Knowledge content drives answers via RAG — quality/coverage of uploaded sources directly affects accuracy. Relates to [[faq-bots]] and [[intents]].
- "Define Tasks and Tools" overlaps conceptually with bot flow/dialogue design — see [[bot-rule-setup]]; tool integrations may pull/push to record data, relating to [[custom-fields]].
- "Trigger applications directly" lets the agent launch without separate rule setup; compare with classic routing via the [[rule-engine]].

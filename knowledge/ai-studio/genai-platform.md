# Platform Generative AI Use Cases (Sprinklr AI — AI Use Cases)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/platform-generative-ai-use-cases/platform-generative-ai-use-cases/697b71d09a795458207842d2

## What it is
- Built-in generative AI capabilities across the Sprinklr Platform that cut manual effort on content, code, and text tasks.
- Grouped into four modules: Coding Assistance, Text Generation, Text Enhancement, and Sandbox Testing.
- Access is governed through AI+ Studio with enable/disable and RBAC controls.

## When to use
- Generate, debug, or summarize Groovy code without writing it by hand.
- Quickly produce hashtags, product descriptions, or multiple content variations for social/marketing.
- Improve existing copy — shorten/lengthen, fix grammar, reword, simplify, change tone, translate, draft emails.
- Validate config/changeset updates safely in a sandbox before pushing to production.

## Configuration steps
1. **Enable the module in AI+ Studio.**
   - Most features show "Enable/disable and RBAC supported" — control access by role here.
   - Text Generation and Text Enhancement features are "Auto-enabled with module" — they turn on automatically once the module is enabled.
2. **Configure Dynamic Properties (DPs) for coding features.**
   - "Generate Groovy Code" and "Debug Groovy Code" need "DP and additional configuration required."
   - Other coding features need "DP configuration required."
   - Contact Sprinklr Support to set these up.
3. **Use Text Generation features** (auto-enabled):
   - Generate Hashtags
   - Generate Product Descriptions
   - Generate Content Variations
4. **Use Text Enhancement features** (auto-enabled, for existing content):
   - Make it Longer / Make it Shorter
   - Fix Spelling and Grammar
   - Reword
   - Simplify Language
   - Modify Tone
   - Translate
   - Draft Email
5. **Use Sandbox Testing** before production:
   - "Summarize Changeset Updates" to validate changes prior to deployment.

## Notes & gaps
- Coding Assistance (Generate / Debug / Summarize Groovy) requires DP setup — not self-serve; route through Sprinklr Support.
- Debug and Summarize coding features lack "AI Configuration Support" (no advanced customization).
- Some features are "Not available in Feature Access Management" — you cannot toggle them per role.
- The article is a capability catalog, not a step-by-step setup guide; exact DP values and per-feature config screens are not documented here — confirm in AI+ Studio or with Support.
- Related GROOT topics: [[ai-studio]], [[rule-engine]], [[custom-fields]], [[intents]], [[bot-rule-setup]].

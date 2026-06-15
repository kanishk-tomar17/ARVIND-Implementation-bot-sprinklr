# AI Scoring / Automated QM (Quality Management 176)
**Source:** Product Foundation Courses → Quality Management / 176 AI Scoring (video transcript + "New Rule: AI Scoring" case-update rule screenshot) · **Help:** search `site:sprinklr.com/help automated quality management AI scoring case update rule parameters`

## What it is
**Automated Quality Management (Auto QM)** automatically evaluates an **entire case conversation** and assigns scores to each interaction across parameters — leveraging **AI** (models trained and deployed to predict on new data). QM itself is evaluating agent performance to find strengths/weaknesses and coach agents toward better CX.

## Why it matters
- Contact centres see huge case volumes (1k–20k+/day). Manual evaluation is time/resource-heavy.
- Manual QM samples only **1–2%** of cases and extrapolates → misleading results.
- Auto QM evaluates **100%** of cases quickly → targeted coaching, and removes human **bias/inconsistency**.

## Three parameter types
1. **Sprinklr AI** — ML models trained on historical **human-labelled data** to learn patterns and predict scores on new data. Uses **NLP / contextual recognition** (tone, sentiment, relationship between words); models improve over time with fresh data + feedback.
   - *Example — empathy detection:* "I understand there's a problem with the machine" = mere acknowledgment (not empathetic); "I understand the inconvenience caused due to the water-drain issue of the washing machine" = genuinely **empathetic** → the AI marks it empathetic because it understands context.
2. **Rule-based parameters** — no context/AI needed; simple logic (e.g. **average hold time** = how long the customer was on hold). Governed purely by rules.
3. **Generative AI parameters** — use genAI models (e.g. ChatGPT); users define **prompts** for very **subjective/specific** use cases.

## Set up AI scoring (demo)
1. **Enable the audit checklist** — once parameters are finalized/deployed, add the parameter to an **audit checklist**; the checklist triggers AI scoring. (See [[audit-checklist]].)
2. **Create a Case Update rule** (Rule Engine):
   - **New Rule** → Name (e.g. "AI Scoring"), Description.
   - **Rule Scope** = **Customer**; **Context** = **Case Update**.
   - Set **Activation Date** and **Rule Execution Batch**.
   - **Rule Type** = **Standard** (triggered automatically per config) or **On Demand** (manual trigger).
   - (See [[case-update-creation]] in Rule Engine for case-update rule mechanics.)
- Scores surface in the **AI Score Breakdown** widget in the Case Analytics view.

## Notes / gaps
- Built on [[audit-checklist]] (parameters/categories) and the Rule Engine ([[case-update-creation]]); complements [[case-sampling-rule-engine]] for which cases to evaluate.
- Part of Quality Management: [[audit-checklist]], [[agent-appeals-process]], [[calibration]], [[case-sampling-rule-engine]].

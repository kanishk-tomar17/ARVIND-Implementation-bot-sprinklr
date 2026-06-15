# Quality Monitoring / Audit Checklist (Quality Management 175)
**Source:** Product Foundation Courses → Quality Management / 175 Quality Monitoring – Audit Checklist (video transcript + Audit Checklist builder screenshot) · **Help:** search `site:sprinklr.com/help audit checklist builder quality management scoring`

## What it is
**Audit checklists** (a.k.a. **audit forms**) are flexible forms used in quality management for **manual evaluations** of processes/systems/products. They give auditors a structured framework to assess compliance with standards, regulations, or internal policies.

## Use cases
1. **Manual case evaluation** — quality managers select an audit form in the **Case Analytics view** (Quality Manager persona) to evaluate an agent across parameters (e.g. opening, closing); review and submit the evaluation.
2. **Calibration** — audit checklists are the main tool; admins calibrate quality managers' audits to establish common understanding of quality standards. (See [[calibration]].)
3. **AI Quality Scoring** — audit forms create customizable checklists that serve as a reference for AI scoring; the **AI Score Breakdown** widget (Case Analytics) leverages them to build categories/subcategories for quality parameters. (See [[ai-scoring]].)

## Configuration steps (demo)
1. Need the relevant **permissions**. In the **Launchpad** → **Platform Modules** → **Audit Checklist** (LUB shows all previously created forms; with permissions you can edit/clone/delete).
2. Click **Audit Checklist** (button) to create a form.
3. Provide **Checklist Name + Description**, and select the **Asset Type** (mandatory) — for QM case evaluations, choose **Case** level.
4. Optionally set **visibility conditions** and **Asset Sharing** (all workspaces or specific workspaces / users / user groups).
5. **Build the checklist:** create multiple **categories** and **subcategories** (called **items**). Per item: provide **description + help text**, select **input type** (pick list, multi pick list, checkbox, radio button, rating scale, audio feedback, etc.).
   - Example: a **pick list** with options **Yes / No**.
   - Per question: disable comments, mark as **mandatory**, set question-level **visibility conditions**.

## Enable scoring
- Scoring can be enabled only on **pick list, multi pick list, checkbox, radio button, rating scale**.
- Click **Enable Scoring** → provide **weightages** for categories and items.
- Options: **Disable scoring**, **enable Not Applicable**, mark an item as **Critical**.
- **Overall audit score** = **weighted average** of item and category scores. (A **Critical** item marked 0 makes the entire score zero.)

## Advanced use cases
- **Agent approval (dispute) flow** — configure agent acknowledgment: number of disputes allowed + time interval to acknowledge, at checklist level; only send for approval if score < a threshold. (Detail in [[agent-appeals-process]].)
- **Auditor approval (calibration acknowledgment)** — similar config; detail in [[calibration]].
- **Snooze intervals** — pause the evaluation going to the agent for acknowledgment up to a max snooze time.
- **Conditional visibility** — show a question based on the response to another question.

## Customer example
A leading brand runs **100+ manual evaluations/day**; multiple categories + mandatory Yes/No/NA questions; **conditional visibility** to capture reasons only when the answer is "No"; **criticality** so a 0 on a critical question zeroes the whole score.

## Notes / gaps
- Foundation for [[ai-scoring]], [[agent-appeals-process]], [[calibration]], and [[case-sampling-rule-engine]]. Additional resources in the KB Quality Management Audit Checklist articles.
- Part of Quality Management: [[ai-scoring]], [[agent-appeals-process]], [[calibration]], [[case-sampling-rule-engine]].

# Calibration (Quality Management 178)
**Source:** Product Foundation Courses → Quality Management / 178 What is Calibration and how to enable it for a partner (video transcript + Audit Calibration Form in Case Analytics screenshot) · **Help:** search `site:sprinklr.com/help quality management calibration auditor approval evaluation type`

## What it is
**Calibration** aligns the evaluation criteria/standards used by a quality manager with those set by the admin/supervisor. It may involve reviewing sample evaluations, comparing scores, discussing cases, and giving feedback to the QM.

## Why it matters
- **Consistency & accuracy** — a uniform approach to evaluating agents, avoiding discrepancies.
- **Standardization** — admins ensure QMs adhere to org standards.
- **Performance improvement** — identify where QMs need training/support.

## Access
Requires the **Calibrate permission** (under the audit checklist).

## Calibration levels
Calibration can occur at multiple org levels (number of levels + evaluation-type names are configurable). Example with 3 levels:
- **Level 1** — quality executives evaluate agents → **default evaluations**.
- **Level 2** — quality managers re-evaluate the executives' audits → **calibrated evaluations**.
- **Level 3** — supervisors evaluate the QMs' calibrated evaluations → **supervisor reviews**.

### Restricting who does which level
Controlled by the standard custom field **Quality Evaluation Type**:
1. Edit the field → toggle on **Custom Field Value Visibility Control**.
2. Select the **evaluation type** → map to specific **user groups / users** → Save.

## How to calibrate (demo)
1. Open a previously audited case (audited by another QM) in **Case Analytics**.
2. Users with calibrate permission **hover on the audit card** → **Calibrate** option.
3. See the audit checklist + auditor details; fill the **Audit Calibration Form** (select evaluation, score each parameter — opening quality, closing quality, resolution quality, etc.).
4. **Submit** → calibrators see the **variance in scores**. (The case view also shows the **AI Score Breakdown** + **CSAT Trend** widgets.)

## Calibration acknowledgment flow
Like the agent appeal process ([[agent-appeals-process]]), QMs can **acknowledge** the calibrated evaluation done by supervisors/admins.
- Pending cases appear on the QM homepage widget **"Calibrated Evaluations Pending Acknowledgement"** → **Open** → see variance → **Agree / Disagree**.
- Controlled at **audit-checklist level:** Edit checklist → **Enable Auditor Approval** → specify **dispute number**, **time before auditor must acknowledge**, and optional condition (send only if score < threshold).

## Reporting
- **Alignment report** — how closely a calibrator and auditor align.
- **Variance report** — parameter-level analysis of score variance between auditor and calibrator.

## Customer example
A leading brand: disputes = **1**, auditor acknowledgment interval = **7 days** (auto-acknowledged if missed); ~**19,000 calibrations** over 8 months across teams.

## Notes / gaps
- Built on [[audit-checklist]] (Calibrate permission + Enable Auditor Approval); parallels [[agent-appeals-process]]. KB articles: "Quality Management Calibration".
- Part of Quality Management: [[audit-checklist]], [[ai-scoring]], [[agent-appeals-process]], [[case-sampling-rule-engine]].

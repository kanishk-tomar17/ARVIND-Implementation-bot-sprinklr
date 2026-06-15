# Agent Appeals Process (Quality Management 177)
**Source:** Product Foundation Courses → Quality Management / 177 Agent Appeals Process (video transcript + checklist "Enable Agent Approval" options screenshot) · **Help:** search `site:sprinklr.com/help agent appeal dispute flow audit checklist quality management`

## What it is
The **agent appeal process** lets agents **access and review** evaluations done on them by quality managers. Agents can **acknowledge** an evaluation or **raise a dispute** if they believe they were assessed inaccurately.

## Why it matters
- **Empowers agents** — gives them a voice in their own evaluations.
- **Transparency & trust** — shows the evaluation system is open to scrutiny.
- **Resolves discrepancies** — agents flag specific areas; auditors re-evaluate.

## Set up (audit-checklist level)
Control which evaluations are sent for agent acknowledgment **per audit checklist**:
1. **Edit** an existing checklist → at the bottom, the options are **Enable Agent Approval**, **Enable Auditor Approval**, **Enable Snooze Interval**.
2. Select **Enable Agent Approval** → configure:
   - **Number of times** an evaluation can be sent for agent appeal (disputes allowed).
   - **Duration** before which the agent must acknowledge.
   - Optional condition: only send evaluations with **score less than** a specific score.

(See [[audit-checklist]] for the full builder.)

## How it works (agent side)
1. Quality Manager completes the evaluation → audit flows to the agent in the **Agent Persona app**.
2. Agent sees evaluations in the **Case Evaluation widget** → **Show** (also views previously acknowledged cases).
3. **Open** an evaluation → detailed per-question scores → **Agree** or **Disagree**.
4. To dispute: click **Dispute**, select the disputed questions, add a **comment**.

## Post-acknowledgment
- **Agent agrees** → case moves to **Total Evaluated** for the quality manager.
- **Agent disagrees** → comes back to the QM. They click **Reevaluation** in the widget, see agent **comments** and disputed questions (yellow flags), and re-evaluate.
- If disputes allowed = 1, after reevaluation it goes directly to **Total Evaluations**.

## Reporting
Plot how scores changed after reevaluation using agent-appeal dimensions/metrics.

## Customer example
A leading brand: disputes = **1**, acknowledgment interval = **3 days**; if the agent doesn't acknowledge in 3 days the audit is **auto-acknowledged**. ~30,000 audits over a year used this flow.

## Notes / gaps
- Configured on [[audit-checklist]]; the auditor-approval counterpart is used in [[calibration]]. KB articles: "Quality Management Audit Dispute Flow".
- Part of Quality Management: [[audit-checklist]], [[ai-scoring]], [[calibration]], [[case-sampling-rule-engine]].

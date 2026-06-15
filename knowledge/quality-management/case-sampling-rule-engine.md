# Case Sampling via Rule Engine (Quality Management 179)
**Source:** Product Foundation Courses → Quality Management / 179 Case Sampling via Rule Engine (video transcript + "Assign to User" rule action screenshot) · **Help:** search `site:sprinklr.com/help quality management automated sampling rule engine case update`

## What it is
**Automated sampling** systematically selects cases and assigns them to quality managers — instead of randomly picking cases, the org shares **criteria** for which cases to audit. Saves QM time and focuses attention where it's needed.

## Sampling criteria (examples)
Per business requirements, pick selected cases. Example:
- **Voice** channel → only if **call duration > 2 minutes**.
- **Live Chat** channel → only if case **sentiment = negative**.

## Set up sampling (two ways)
Configured in **Case Update rules** (Rule Engine — see [[case-update-creation]]):
1. **Via condition in case update rule** — set fields: **Sample By** (with state), **frequency** of sampling, **number of assets/cases** to sample, **sampling category**, and user custom field (typically **per user** and **last engaged user**).
2. **Via sampling action in case update rule** — set: **Add sample data to queue** (stores the sample cases), **number of samples**, **sampling duration** (frequency), **sampling start time**, **sample for each** (= last engaged user).

## Assign sampled cases to users (two ways)
1. **Assign to individual users** — via **Assign To User** action: provide which **checklist** to assign for manual audit; **For Quality Evaluations** must be set to **Yes** when allocating to QMs; **Evaluation Type** (optional — **Calibration** / **Default**) only selected when sampling calibrated cases.
2. **Assign to a group of QMs** — add all QMs to a **work queue** and select that work queue; can also pick which **interactions** within an omni-channel case to assign.

## Reporting
Plot **total cases sampled / evaluated**, audit-status data, and evaluation scores. Filter **Assigned for Evaluation By = moderation user** to see only system-assigned cases.

## Customer example — end-to-end (voice + social)
Problem: sample to QAs for voice & social; sample cases agents engaged on the **previous day**; unassign from QAs after **2 days**; **2 cases/day**; sample by **last engaged agent**; **QM-agent mapping** (specific agents → specific QAs); voice only if call duration > 2 min; social excludes specific dispositions.

**Voice config (3 rules):**
1. **Case update rule** — add all created voice cases to a dedicated **case queue**, copy agent details to case custom fields, and add cases to a **scheduler** to trigger the next rule. (On-demand rule, triggered via the work queue's **Assignees → Select rules to execute**.)
2. **On-demand rule for sampling** — add all required conditions; **remove cases from the main queue** after sampling (else stale cases linger). Triggered via the **Scheduler Engine** (see [[scheduler-engine]]).
3. **Case assignment rule** — sampling condition (number of samples + frequency) + assignment to specific QMs based on **QM-agent mapping** (field **reviewer**); uses a **business hours** condition (e.g. auto-assign between 12–2 AM so QAs have fresh cases). Store sampled cases in another **case queue** for assignment.

## Notes / gaps
- Built on the Rule Engine ([[case-update-creation]], [[on-demand-rules]], [[scheduler-engine]], [[queue-rules]]); feeds [[audit-checklist]] evaluation, [[ai-scoring]], and [[calibration]].
- Part of Quality Management: [[audit-checklist]], [[ai-scoring]], [[agent-appeals-process]], [[calibration]].

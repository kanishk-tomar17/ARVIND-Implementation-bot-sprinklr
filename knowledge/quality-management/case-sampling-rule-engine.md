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

## Percentage-based sampling ("audit X% of all cases") — WORKAROUND
**There is no native "sample N% of cases" field.** The built-in sampling action takes a *fixed count* per frequency (e.g. 2 cases/day), not a percentage — so a contractual target like "30% cumulative across the year" can't be configured directly.

**Workaround — random-number draw in a case rule** (verified in client build, 2026-09):
1. Case rule triggered **on case create** (i.e. as soon as the case enters the platform), so the decision is made once per case and the sampled pool fills in near-real-time.
2. Rule generates a **random number 1–100** into a case custom field.
3. Condition: **random number ≤ N** (N = 30 for 30%) → set a `Sampled = Yes` custom field / add to the sampling queue.
4. Report on it by comparing **Case Count** filtered to `Sampled = Yes` against total Case Count.

**Why it holds up (the argument to give a client):** the draw is applied to *every* case with identical odds and **no gating conditions**, so the sampled set is an unbiased scaled-down copy of the population — channel, language, agent, duration and time-of-day mix all mirror the total automatically, with no quotas to configure. Accuracy *improves* as volume grows (law of large numbers). Validate by building paired widgets (all cases vs sampled cases) grouped by each dimension and showing the percentages match.

**Trade-offs to flag:**
- **Trigger timing.** On **case create** you get near-real-time sampling but **no case attributes exist yet** — you cannot gate on call duration, disposition or sentiment (so the `call duration > 2 min` style criteria above are unavailable). On **case close** all attributes are final and filterable, but sampled cases only surface once complete. Pick per client; a create-trigger + close-time re-validation rule gives both at the cost of a second rule.
- Percentage is **statistical, not exact** — expect small drift in any short window; it converges over volume. Don't promise an exact monthly count.
- Because the rate is applied per case, **no monthly quota calculation is needed** — the sample scales itself with volume. This replaces the common "set sample size from last quarter's average" requirement.

**Manual allocation instead of automated day-by-day assignment:** where a client's allocation pattern varies with daily staffing, don't hardcode it. Drop sampled cases into a **shared work queue** the QM/SQ officers pull from themselves, and don't auto-unassign — unpicked cases simply remain in the queue for the agreed window. See "Assign to a group of QMs" above.

## Notes / gaps
- Built on the Rule Engine ([[case-update-creation]], [[on-demand-rules]], [[scheduler-engine]], [[queue-rules]]); feeds [[audit-checklist]] evaluation, [[ai-scoring]], and [[calibration]].
- Call-length metrics for short/medium/long banding: [[voice-backend-structure]].
- Part of Quality Management: [[audit-checklist]], [[ai-scoring]], [[agent-appeals-process]], [[calibration]].

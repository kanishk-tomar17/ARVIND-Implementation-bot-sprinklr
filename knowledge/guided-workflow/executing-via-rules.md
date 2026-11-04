# Guided Workflow — Executing via Rules

**Source:** https://www.sprinklr.com/help/articles/initiating-a-guided-workflow/executing-guided-workflows-via-rules/63d62d29468ae80d39346a53

## What it is
Triggering a Guided Workflow (GW) as an automated action from a **Case update rule**, instead of a manual entry point (case control button, nudge, widget, etc.).

## When to use
When a GW should run automatically off a case condition (e.g. status change, field update) with no agent interaction needed.

## Configuration steps
1. Go to **Rule Engine → Universal Case** category → create a new **Case update rule**.
2. Set the triggering conditions as usual.
3. In the action picker, select **Trigger Process**.
4. Pick the specific **Guided Workflow** to run (mandatory field — this is the only required field for the action).
5. Save the rule, then **add it to the rule picklist** — a rule isn't active until it's added to the picklist after creation.

## Common issues & fixes
- **Rule saved but GW never fires** → check the rule was added to the rule picklist; a created-but-not-picklisted rule stays dormant.

## Notes & gaps
- **Hard limitation:** this only works for GWs that contain **no screen nodes**. A workflow with any screen node (i.e. anything needing agent/user input mid-flow) cannot be launched this way — screen-based GWs still need a manual entry point (case control button, nudge, widget — see `guided-workflow/overview.md`).
- Related: `guided-workflow/overview.md` (all GW trigger entry points), `knowledge/quality-management/case-sampling-rule-engine.md` if cross-referencing rule engine mechanics.
- Didn't check the separate "Automatic Triggering of Guided Workflows" article (may cover non-rule automatic entry points) — fetch that one if asked about automatic triggering outside the Rule Engine.

## Sources
- https://www.sprinklr.com/help/articles/initiating-a-guided-workflow/executing-guided-workflows-via-rules/63d62d29468ae80d39346a53

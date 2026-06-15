# Manual Case Creation & Merge Case Setup (Email Care 136)
**Source:** Product Foundation Courses → Email Care / 136 Manual case creation + Merge case setup (video transcript + demo) · **Help:** search `site:sprinklr.com/help manual case creation merge cases parent child`

## Manual case creation
For a conversation that happened **outside Sprinklr**, manually create a case to record it (for tracking/monitoring).
- **Quick Publisher (pencil button) → Create Case** → dialog: enter **Email ID** (mandatory), First name, Last name, Phone → **Next** → **Subject, Description, Notes** → **Create**. Case created for that email/subject.
- **Acting on manual cases via Rule Engine:** use a **Case Creation rule** with condition **"Is profile case = Yes"** → actions then apply only to manual cases.

## Merge cases
Merge **2+ email cases** (in Agent or Care Console) when multiple cases exist for **one customer issue**. Scenarios:
- Same person emails a **different brand email ID** with the same issue.
- Same person sends a **new email** for the same issue (instead of replying).
- **Different people** from a team raise the same issue.
After merge you continue the conversation in **one case**: **one parent (master) case + one or more child cases**.

### How to merge
Case Overview / third pane → **⋯ → Merge Cases** → select the cases to merge → choose the **master (parent)** case; others become **child** cases. Change master via hover → **Mark as Master**.

### Acting on merged cases via Rule Engine
- Condition **"Is Parent Case in merge action"** → actions for the **parent**; **"Is Child Case in merge action"** → actions for the **child**.
- **Copy child/parent case number** (e.g. to a custom field): action **Copy Properties (source/destination)** with source = Case, destination = Case.
  - Child→Parent: condition is **child case**, copy the case number into the parent's custom field.
  - Parent→Child: condition is **parent case**, copy the parent case number to **all child cases**.
- **Rule trigger:** enable a **time-agnostic trigger** so the rule fires whenever a merge action occurs (condition = child-case merge action OR parent-case merge action satisfied).

## Notes / gaps
- Uses Case Creation rules + Copy-properties actions + time-agnostic triggers ([[case-update-creation]], [[batches-triggers]]). Manual case via Quick Publisher in Care/Agent Console.
- Part of Email Care: [[account-types]], [[webforms-external-gw]], [[email-signature]], [[email-collaboration]], [[ignore-duplicate-autoresponse]], [[email-templates]].

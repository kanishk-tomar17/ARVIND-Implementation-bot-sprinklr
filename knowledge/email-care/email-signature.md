# Email Signature Setup (Email Care 134)
**Source:** Product Foundation Courses → Email Care / 134 Email signature setup (video transcript + demo) · **Help:** search `site:sprinklr.com/help email signature managed signature autofill rule`

## What it is
An **email signature** = a block of text/graphics auto-appended to outgoing emails (sender name, title, contact, social links, company logo) — conveys professionalism. Most email customers use signatures.

## Two ways to set up signatures
### 1. Agent-level signatures ("Manage Signature")
- Per-agent: the agent goes to their **User → Manage Signature**.
- **Prerequisite:** the **"Manage Signatures" option is NOT visible by default** — raise a **support ticket** to enable the DP **"Account user signature move to new structure"**. Only then does the option appear at partner level.
- **Three scopes (narrowing precedence):**
  1. **Default signature** — used on all the agent's messages unless overridden.
  2. **Channel-specific signature** — overrides default **for that channel** (e.g. Email).
  3. **Account-specific signature** — overrides channel + default **for that specific account**.
  - Precedence: account-specific > channel-specific > default.
- **Drawback:** every agent must manually log in and set their own signature; not feasible at scale (e.g. 200 agents) and any change means every agent re-edits theirs.

### 2. Autofill rule (recommended at scale)
- A **rule** that **automatically applies signatures for multiple agents across accounts/channels** — no manual per-agent input.
- Set up one autofill rule for the brand with **conditions** per use case (e.g. a specific set of users/agents → a specific signature). Changes are made once in the rule.

## Notes / gaps
- Agent-level signature also referenced in Governance [[users-user-groups]] (default signature field). The autofill rule is a standard rule ([[inbound-rules]]/rule engine pattern) applying signature actions.
- Part of Email Care: [[account-types]], [[webforms-external-gw]], [[email-collaboration]], [[manual-case-merge]], [[ignore-duplicate-autoresponse]], [[email-templates]].

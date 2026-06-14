# Case Management — Survey Rules

**Source:** Product Foundation Courses → `Sprinklr Services - Case Management / 020_… Survey Rules` (video transcript) · **Cross-check:** `site:sprinklr.com/help survey rules`

How surveys built in the **Survey Builder** get **triggered** on a case after resolution — to capture CSAT/feedback.

## Where it fits
- After a case is resolved (by bot or agent), the brand triggers a **Sprinklr survey** to capture customer experience. (Survey *building* is covered in the Survey Builder videos; this is about *triggering*.)

## Survey delivery rules (per channel)
- They're **Customer Case Update rules**, **3 separate delivery rules**: **private channels** (Facebook, WhatsApp, Twitter/X…), **Live Chat**, **Email Care**. All near-identical — they differ only in **how the survey visually appears** per channel.

## Trigger & conditions (private-channel rule)
1. **Runs via trigger only** (dummy condition to save the trigger; not on normal case updates).
2. **Case in the "Ready for Survey" queue** — the rule only runs on cases in this queue. *This is how a case signals "send a survey."*
3. **Queue assignment time duration** (e.g. **1 hour**, flexible per brand) — don't survey immediately after resolution; give the customer time to review. If they reply again, the case is removed from the queue (agent gives final resolution) before survey.
4. **Channel-type check** — ensure the right rule handles the channel (this rule excludes Live Chat / Email, which have their own rules).
5. **"Survey sent" custom field = No** — tagged "No" when a case is created; set to "Yes" once a survey is sent (prevents duplicate surveys).
6. **Associated brand message count ≥ 1** — don't survey cases where the brand never replied.

## How a case enters the "Ready for Survey" queue
- When the agent finishes and applies the **Close macro**, that macro removes the case from other queues, puts it in the **Closed** queue **and** the **Ready for Survey** queue → the survey rule then fires.

## Notes / gaps
- From the course video transcript (blueprint env). Durations/conditions vary per brand. Related: `case-management/sub-cases.md` (closure→survey), Survey Builder (separate).

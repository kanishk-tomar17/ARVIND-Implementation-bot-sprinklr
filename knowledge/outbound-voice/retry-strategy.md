# Retry Strategy & Dial Plan (Outbound Voice 165)
**Source:** Product Foundation Courses → Outbound Voice / 165 Voice Campaigns – Retry Strategy and Dial Plan (video transcript) · **Help:** search `site:sprinklr.com/help voice campaign retry strategy telephony business outcome dial plan`

## Retry strategy — what & why
A **systematic approach to manage unsuccessful/unanswered outbound calls** — rules for **retrying** failed/unconnected calls later (each call has an outcome; if the customer is unavailable, redial per the strategy).
- **Benefits:** higher **contact rates**, re-engage failed calls, **optimal resource use** (prioritise by success potential), better CX (controlled timing/frequency protects brand reputation), and **flexibility** (number of retries, intervals, rules).

## Two types (Sprinkler)
- **Telephony outcome retry** — when agent & customer are **NOT connected** (busy, no answer, voicemail, network down).
- **Business outcome retry** — when they **ARE connected**; based on the **disposition/ACW** the agent fills.

## Creating a retry strategy
**Sprinklr Service → Voice Care → Call Retry Strategy → Create Strategy.**
- **Telephony outcome:** name it → add **telephony outcomes** each with a **retry-after time** (e.g. *all agents busy → 5h; customer hung up before agent → 10 min; agent call failed → 20 min; customer no answer → 3h; network out of order → 3h; all skipped (preview) →; number temporarily unavailable →*). Preview pane lists outcomes + times → Save (View/Edit later).
- **Business outcome:** name it → select a **disposition plan** (≈ a product, e.g. *Credit card*) → its **sub-dispositions** (a **main outcome** like "Lead" with sub-outcomes Sales closed / Follow-up; "Non-eligible"; etc.) → set **retry-after** per outcome (e.g. *appointment follow-up → 10h; too much documentation → 10 days*). Add **multiple disposition plans** (auto loan, car wash…) → Save.

## Dial Plan — sequential dialing
A **dial plan** dials a customer's **multiple phone-number types** (primary / alternate / tertiary) in order — if the mobile isn't picked up, try office/landline.
- **Voice Care → Dial Plan** (below Call Retry) → **Create Dial Plan.** Phone-number types come from the **data-collection** ingested columns mapped to phone numbers. Two modes:
  1. **Try the next phone-number type after one unsuccessful attempt** — add types with **Max attempts** each (e.g. 2/3/1) + a **retry plan** (telephony outcome). On a telephony outcome (e.g. no answer) it moves primary → alternate → tertiary, cycling per each type's max-attempts cap (a type at its cap is skipped). **Drag-drop** to reorder priority.
  2. **Continue calling the same type until Max attempts exhausted** — hammer the primary per the retry plan until its attempts are used, then move to alternate, etc. If the customer **picks up**, stop (no further numbers).
- Name → Save (Edit/Delete available).

## Adding to a campaign
**Campaigns** module (new or existing): set the **Dial plan** and the **Business outcome retry strategy**. Also set **Maximum attempts** (across the whole campaign date range) and **Daily attempts** (e.g. 4 total / 2 daily) → Save.

## Notes / gaps
- Telephony retry = "couldn't reach them"; business retry = "reached them, now schedule a follow-up." Both attach to the campaign.
- Phone-number types are only as good as the **data-ingestion mapping** ([[data-ingestion]]) — map primary/alternate/tertiary columns correctly.
- Max + daily attempt caps prevent over-calling (compliance/CX); they bound both dial-plan and business-retry attempts.

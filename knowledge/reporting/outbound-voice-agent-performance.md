# Outbound Voice — Agent Performance (Reporting 081)
**Source:** Product Foundation Courses → Reporting / 081 Outbound Voice Use Cases - Agent Performance (video transcript + Outbound Time Metrics glossary slide) · **Help:** search `site:sprinklr.com/help outbound agent summary report calls offered unique profiles dialer type`

## What it is
The outbound **agent summary report** — similar structure/metrics to the inbound agent report, with outbound-specific additions and differing definitions.

## Critical reporting rules (outbound)
- **Not every outbound call = offered.** In predictive/preview dialing the dialer calls first; sometimes the agent connects first, sometimes the customer. So always:
  - Apply the filter **Call States = Agent Connected** to confirm the agent was actually connected.
  - Use **Dialer Type** (Preview / Predictive / Manual) to segregate reports per scenario.

## Call metrics
- **Number of Calls Offered** — customer interactions **assigned to an agent**, *excluding* scheduled-callback and manual calls.
- **Calls Taken** — both customer + agent connected.
- **Calls Not Taken** — offered minus taken.
- **Calls Manually Dialed** — calls the agent dialed manually.
- **Scheduled Callback Dialed** — callbacks (from missed calls) the agent responded to.
- **Total Connected Calls** — custom metric summing total call volume.
- **Preview Dialer Calls Offered / Connected** — filter Dialer Type = Preview.
- **Unique Profiles per Agent** — unique customer numbers an agent contacted (vs total calls — e.g. 20 unique numbers, 40 calls because tele-sales calls the same customer repeatedly). Often shown as a daily metric.

## Time metrics (glossary)
- **Ring Time (Agent)** — time calls rang at the agent console. *Often **0** for outbound* (manual/scheduled calls dial out immediately); **>0 for predictive** (dialer made the call, it rang at the console). **Average Ring Time** = Ring Time ÷ Calls Taken.
- **Talk Time (Agent)** — time in customer interactions; **Average Talk Time** = Talk Time ÷ Calls Taken.
- **Hold Time (Agent)** + **Average Hold Time**.
- **After Call Wrap-up Time (Agent)** (disposition/sub-disposition fill) + **Average Wrap Time**.
- **Handle Time (Agent)** = Talk + Hold + Wrap; **Average Handle Time** = Handle Time ÷ Calls Taken.
- **Total Logged-in Time**, **User Logins Count**, **Time Spent in Status**.
> Post-connection metrics (talk/hold/ACW/handle) are **identical to inbound** — the structural difference is **before connection** (ring/offer behaviour).

## Notes / gaps
- Uses [[voice-backend-structure]] (Voice Agent Performance); custom metrics via [[custom-metrics]] + Call State / Dialer Type [[filtering]]. Mirrors [[inbound-voice-agent-performance]].
- Part of Reporting (Voice/Outbound): [[outbound-voice-overall]], [[outbound-voice-campaign-management]], [[outbound-voice-schedule-callback]], [[outbound-voice-ingestion-report]].

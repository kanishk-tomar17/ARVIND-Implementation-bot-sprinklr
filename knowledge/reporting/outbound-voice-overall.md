# Outbound Voice Use Case — Overall (Reporting 079)
**Source:** Product Foundation Courses → Reporting / 079 Outbound Voice Use Case - Overall (video transcript + "Outbound Reporting" overview slide) · **Help:** search `site:sprinklr.com/help outbound reporting upload contacts inventory campaign management call summary`

## What it is
Overview of outbound voice reporting — the chronology of dashboards Sprinklr provides to monitor day-to-day outbound calling.

## Outbound calling — context
An **outbound call** is made from Sprinklr to a customer. Types: **Predictive, Preview, Manual Outbound, Scheduled Callback**. Purposes: **tele-sales/telemarketing campaigns**, relationship management (satisfaction, cross-sell), and **miscall management** (auto-create scheduled callbacks when agents are busy).

## The outbound report chronology (6 dashboards)
1. **Upload Contacts Report** — every outbound centre starts with an **upload file** (customer details, at least a phone number). Sprinklr returns the processed file + extra parameters as an extract: file name, unique ID, customer name, phone number (the number called), additional details (location, etc.).
2. **Inventory Report / Call Report on Ingested Data** — the upload file **combined with Sprinklr calling data** (how many calls made, whether the customer connected / complete call). Includes file name, upload date, lead count per template, etc.
3. **Campaign Management Dashboard** — outbound calling runs via **campaigns + segments**. In a segment you set **pacing ratio, churn rate, connectors** (which calling profile dials through which dialer). The dashboard gives an overview per campaign/segment: dialer type (predictive/preview), number of agents assigned, how the segment is performing. (See [[outbound-voice-campaign-management]].)
4. **Call Summary Report** — details of every outbound call, split by **Conversation ID**: call start time, disconnect time, phone number, time statistics, properties.
5. **Agent Live Monitoring / Agent Summary Dashboard** — per agent: calls made, calls connected, time in login/ready/manual-outbound/break states, schedule callbacks made → spot over/under-performers, build incentive structures. **Live monitoring** shows, per segment/work-queue at a point in time, how many agents are available / on calls / in ACW. (See [[outbound-voice-agent-performance]].)
6. **Scheduled Callback** — reporting on scheduled callbacks. (See [[outbound-voice-schedule-callback]].)

## Notes / gaps
- Each dashboard has its own deep-dive video. Built on voice reports ([[voice-backend-structure]]); ingestion detail in [[outbound-voice-ingestion-report]]. Outbound Voice module config: see Outbound Voice KB (dialers, campaigns, etc.).
- Part of Reporting (Voice/Outbound): [[outbound-voice-campaign-management]], [[outbound-voice-agent-performance]], [[outbound-voice-schedule-callback]], [[outbound-voice-ingestion-report]], [[voice-troubleshooting]].

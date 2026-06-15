# Inbound Voice Use Cases — Agent Performance (Reporting 077)
**Source:** Product Foundation Courses → Reporting / 077 Inbound Voice Use Cases - Agent Performance (video transcript + Agent Hygiene Report screenshot) · **Help:** search `site:sprinklr.com/help inbound voice agent performance calls offered taken handle time`

## What it is
Agent performance reporting for inbound voice. The inbound flow is split into **4 report stages**: call lands on **IVR** (overall call count) → traverses IVR → requests an agent → assigned to a **queue** → assigned to an **agent**. **Agent reporting starts only when the call is assigned to an agent** — this explains why call count in agent dashboards won't match IVR call count.

## Call metrics
- **Number of Calls Offered** — total interactions assigned to an agent.
- **Number of Calls Taken** — calls where customer + agent connected.
- **Calls Not Taken** — offered minus accepted.
- **Total Transfers Initiated** / **Total Transfers Received**.

## Time metrics
- **Ring Time (Agent)** — time the call rang at the agent's console.
- **Talk Time** — agent + customer connected.
- **Hold Time** — customer on hold.
- **ACW Time** — time on after-call wrap-up.
- **Handle Time** = Talk + Hold + ACW.
- **Total Logged In Time** — time in logged-in status.
- **User Logins Count** — number of times logged in that day (e.g. login 10:00, logout 12:00, login 1:00, logout 3:00 = 2).
- **Time in Status** — distribution across availability statuses (an agent logged in but in an **unavailable** status won't receive a call).

## Agent Hygiene / Performance Report
Aggregated view of call + time matrix per agent (not by case/conversation):
- **Call matrix:** Number of Calls Taken, Not Accepted, Rejected (missed), Total Offer Missed Calls, Transfers Initiated/Received.
- **Time matrix (Agent Summary):** Average Handle Time, Average Talk Time, Average Mute Time, Average Hold Time, Hold Count (Agent), Average Wrap Time, Average Ring Time, Average Conference Time, Calls Abandoned on Hold (Agent).
- Can be plotted separately (calls on top, time below) or **side-by-side** as one aggregated view. Gives a supervisor a sense of which agent fared well by call volume.

## Build
Use **dashboard library** standard widgets to bootstrap an inbound call-centre dashboard, then modify; or build from scratch via [[creating-widget]].

## Notes / gaps
- Built on the voice reports in [[voice-backend-structure]] (Voice Agent Performance report); IVR stage in [[inbound-voice-ivr]], queue stage in [[inbound-voice-queue-report]].
- Part of Reporting (Voice): [[voice-backend-structure]], [[live-reporting-voice]], [[inbound-voice-ivr]], [[inbound-voice-queue-report]].

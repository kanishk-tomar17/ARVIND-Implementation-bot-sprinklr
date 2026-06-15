# Voice Reporting Backend Structure (Reporting 074)
**Source:** Product Foundation Courses → Reporting / 074 Voice Reporting Backend Structure (video transcript + "Key Reports for Voice" slide screenshot) · **Help:** search `site:sprinklr.com/help voice reporting ACD report voice agent performance conversation ID`

## Three key voice reports
| Report | Contains | Record granularity | Primary metric |
|---|---|---|---|
| **Voice Report** | **All** calls (inbound + outbound), whether or not agent/customer connected | One record per call (unique ID = **Conversation ID**); **aggregated** data even when multiple agents/queues involved (total talk time, AHT, total queue time, first queue time) | **Call Count** |
| **ACD Report** | All calls that **entered a queue** (after an agent is requested) | A record **each time a call enters a queue** (same call into same queue twice = 2) — for queue-level SLAs | **Total Calls (per assignment)** |
| **Voice Agent Performance** | Calls **offered to an agent** OR **initiated by an agent** | **One record per agent per call** — for agent-level talk time, dispositions, etc. | **Number of Calls Offered / Number of Calls Taken** |

## Which report when
- **Voice Report** — overall call data; aggregated per call. Use for total counts.
- **ACD Report** — queue-level reporting (how many times a call entered each queue). Calls that never requested an agent / never entered a queue **won't appear here**.
- **Voice Agent Performance** — any agent-level metric (talk time, dispositions per agent).

## Inbound flow → where data lands
Call lands on **IVR** → customer requests an agent → call enters a **queue** → agent assigned.
- Voice Report = from IVR / all initiated calls.
- ACD Report = only calls that reached a queue.
- Voice Agent Performance = only calls offered to / initiated by an agent.

## Worked example (aggregation)
A call: IVR 15s → Q1 → A1 (talk 1 min) → transfer to Q2 → A2 → transfer back to Q1 → A3 (talk 1.5 min).
- **Voice Report (1 record):** IVR time 15s; **All Participated Agents** = A1,A2,A3 (or as CSV / per-agent metric); **aggregated talk time** = 1+2+1.5 = 4.5 min (same 4.5 shown for the call); **total queue time** = 10+15+15 = 40s.
- **ACD Report:** a record per queue entry (Q1 twice + Q2).
- **Voice Agent Performance:** a record per agent (A1, A2, A3).

## Notes / gaps
- Voice equivalent of [[backend-structure-digital]]; drives the voice use-case reports ([[live-reporting-voice]], [[inbound-voice-ivr]], [[inbound-voice-agent-performance]], [[inbound-voice-queue-report]], outbound voice reports).
- Part of Reporting (Voice): [[live-reporting-voice]], [[inbound-voice-ivr]], [[inbound-voice-agent-performance]], [[inbound-voice-queue-report]].

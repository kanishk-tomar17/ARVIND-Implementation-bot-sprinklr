# Queue Standard Metrics Configuration (Work Queue thresholds)

## What it is
Per-**Work Queue** thresholds that decide how the standard queue metrics are counted — **Short Abandon**, **Assignment SLA** and **First Response SLA**. Change these and the queue/ACD reports recalculate against the new threshold. Set **per queue**, not globally.

## Where to edit it
**Launchpad → Unified Routing → Work Queues → [select queue] → ⋮ menu → Edit Work Queue → Standard Metrics** → edit → **Save** (bottom-right).

## Fields & defaults
**Short Abandon Duration** — caller hung up before this threshold ⇒ counted as *Short Abandoned*, not a real abandon.
| Field | Default |
|---|---|
| Short Abandon Time for Voice Channel | **5 seconds** |
| Short Abandon Time for Live Chat | 60 seconds |

**Assignment SLA** (based on agent assignment)
| Field | Default |
|---|---|
| Assignment Duration Threshold for Voice | **20 seconds** |
| Assignment Duration Threshold for Live Chat | 120 seconds |
| Service Level Agreement for Emails | 24 hours |
| Service Level Agreement for Socials | 2 hours |

**First Response SLA** (based on first response)
| Field | Default |
|---|---|
| Service Level Agreement for Live Chat | 120 seconds |
| Response Duration Threshold for Social | 2 hours |
| Service Level Agreement for Emails | 24 hours |

- The Live Chat / Voice threshold rows carry an **"Include Short Abandons"** toggle — decides whether short-abandoned contacts count in the SLA denominator.

## Common issues & fixes
- **"Short call / short abandon number looks wrong"** — it's per queue. Check the specific queue, not a global setting; a multi-queue report mixes different thresholds.
- **Don't confuse the two "short" metrics:**
  - **Short Abandoned** (queue-level, editable here, default 5s) = caller dropped in the **queue** before the threshold.
  - **Short Calls in IVR** (default **10s**, **not editable in the UI** — needs a Sprinklr support ticket) = call ended inside the **IVR** below the threshold. See [[inbound-voice-ivr]].
- Neither is a "short call" in the QM sense of *short/medium/long conversation length* — for that use **Talk Time** / **Total Call Duration** and band it yourself. See [[voice-backend-structure]].

## Notes & gaps
- Feeds the queue/ACD reports in [[voice-backend-structure]] and [[inbound-voice-queue-report]]; queue setup in [[routing-configuration]] / [[routing-types]]; wait-time behaviour in [[wait-time-queue]].

## Sources
- sprinklr.com/help — [Queue Standard Metrics Configuration](https://www.sprinklr.com/help/articles/standard-metrics/queue-standard-metrics-configuration/6751ae9f974a651ec2f9b3f7)

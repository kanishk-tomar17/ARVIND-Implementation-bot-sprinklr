# Dialers — Predictive, Preview, etc. (Outbound Voice 164)
**Source:** Product Foundation Courses → Outbound Voice / 164 Dialers (Predictive, Preview etc.) (video transcript) · **Help:** search `site:sprinklr.com/help dialer profile predictive preview pacing ratio drop rate`

## What a dialer is
An **automated system that dials phone numbers** to connect customers with agents — phone systems integrated into the software for outbound calls. Goal: **more calls in the same time** (save time/money), reach more prospects.
- **Use cases:** telemarketing/sales (predictive), **collection & debt recovery** (prioritise by debtor profile, auto follow-ups), customer service (manage inbound via unified routing), **appointment reminders/notifications** (outbound IVR, prerecorded — healthcare, salons), surveys/market research, lead generation.

## Dialer types (Sprinklr)
| Type | First | Behaviour / use |
|---|---|---|
| **Predictive** | **Customer-first** | Improves **agent occupancy** while staying compliant with **abandonment (drop) rate**; AI dials ahead via a **pacing ratio**; on pickup routes to an available agent. **Fastest** dialer. |
| **Preview** | **Agent-first** | Call lands to the agent, who **reviews customer info** then calls or skips. **1:1**, high-value campaigns, higher close rate. |
| **Progressive** | Agent-first | System dials the **next record as the agent moves from ACW → available**; efficiency for high-value campaigns. |
| **Outbound IVR** | — | Announcements / proactive info via **prerecorded IVR** (can pair with a voice bot). |
| **Outbound IVR with agent** | — | IVR workflow **+ agent connected via DTMF** selection (IVR + predictive). |
| **Agent dialer** | — | Agent as a **virtual relationship manager** — dedicated agent ↔ customer (e.g. bank VRM). |
| **Callback** | — | **Schedules callbacks** ("call me tomorrow 4pm"). |
| **Manual** | — | Agent enters customer details and clicks call; **status-driven**. |

## Pacing ratio & drop rate (predictive)
- **Pacing ratio** = customers dialled per available agent (ratio 2 → 2 customers per agent).
- **Abandonment/drop rate** = calls the customer picked up but **no agent was free** to take.
- **Configure pacing ratio** (fixed) **or configure drop rate** (set a **max threshold**, e.g. 3%, + initial pacing ratio; the algorithm **auto-adjusts** pacing to stay under the drop rate — high pickup → pacing down ~1.9, low pickup → up ~2.1). Keep **auto-respond on**.

## High-level journeys
- **Customer-first (predictive):** campaign manager configures → agents log in → dialer calls → customer picks up → **unified routing** connects to an agent → conversation → agent fills **disposition + ACW** (business outcome).
- **Agent-first (preview):** configure → dialer places outbound call → unified routing assigns to a free agent → agent **previews** info → calls customer → answers → agent fills ACW.

## Creating a dialer
**Sprinklr Service → Voice Care → Dialer Profiles → Add Dialers** → pick type → configure → Save. Common fields:
- **Status:** Active / Pause / Shutdown.
- **Ring time** — disconnect if customer doesn't answer (e.g. 30s → move to next record).
- **Setup time** — disconnect if telecom can't establish the connection (e.g. 2–5s; the brief pause before a call connects).
- **Queue** — the agent group taking calls.
- **Voice application** + **DID number** (the display number shown on the customer's phone).
- **Preview-type extras:** **preview time** (e.g. 30s), allow agent to **skip** on preview, allow skip straight to ACW, allow system to **auto-pick on preview timeout** (auto-respond), **preferred agent** (route a call to specific agents via an **audience-lead attribute**, e.g. agent ID).
- **Predictive extras:** pacing ratio **or** drop rate (see above).
- **Outbound IVR:** select the **IVR process** to play. **With agent:** + queue, initial pacing ratio, drop rate.
- **Callback:** status when callbacks fire (e.g. Available), preview time, voice app, DID.
- **Manual:** status when available (or a "manual outbound" status), optionally **map to a campaign** (reporting), DID.

## Attaching a dialer to a campaign
A **campaign** defines the customer list, business hours, volume, and **retry strategy** (the dialer just dials). In the **Campaigns** module, create a campaign and **select the dialer profile**, or update an existing campaign's dialer profile → Save.

## Notes / gaps
- **Customer-first (predictive) vs agent-first (preview)** is the core mental model — occupancy/scale vs quality/1:1.
- Drop-rate config is the compliant way to run predictive at scale (auto-tunes pacing); fixed pacing is simpler but riskier on abandonment.
- Dialer is half the picture — the [[campaign-creation]] holds the list/hours/[[retry-strategy]]; ACW/disposition in [[acw]]/[[post-call-workflow]].

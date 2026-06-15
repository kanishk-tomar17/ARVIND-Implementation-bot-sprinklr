# Manual Call & Call Controls (Outbound Voice 170)
**Source:** Product Foundation Courses → Outbound Voice / 170 Manual Call and Call Controls (video transcript + Care Console demo) · **Help:** search `site:sprinklr.com/help manual call call controls transfer warm blind`

## Manual outbound call
The agent **manually dials a number** (vs automatic preview/predictive dialers that run lead lists). Used for **callbacks**, after call abandonment/network issues, or to individually re-contact a customer.
- **Time-intensive** but high-value: the agent can **research history**, personalise, and guide the conversation → often **higher revenue** outcomes.

## Initiating a manual call
1. Agent logs in → **set status** (e.g. Available or a "manual call" status — status-driven, varies by client).
2. Click the **Call** icon → select the **manual dialer** → enter the **number** (country code configurable) → **Call**.
3. The **Care Console** opens, a case is created, the call is placed → customer answers.

## Call controls (Care Console, during a call)
- **End call** (red button), **Hold** (customer hears hold music), **Mute** (self, for background noise).
- **Transfer** — **internal** (Queue / Agent / IVR) or **external**:
  - **Queue** → pick a queue (skilled agent group; shows available agents), **add notes** (context) + **add skills**.
  - **Warm transfer** — heads-up to the secondary agent: customer auto-held while primary+secondary talk, then **Cancel** (secondary off, customer back to primary), **Transfer** (secondary takes the case, primary off), or **Merge** (3-way conference).
  - **Blind transfer** — no heads-up; add notes/skills → transfer → case goes to the secondary agent (primary loses it).
  - **IVR** transfer → connect the customer to a **voice bot**.
- **Add (conference)** — add an **external** number; merged with customer + primary agent.
- **Record** — for training/quality; **transcribed** by Sprinklr.
- **Settings** — choose microphone/speaker output.

## Benefits of call controls
- **Productivity** — agents transfer themselves (vs old landline connectors), with notes/heads-up/skills for faster resolution.
- **Call quality** — mute/hold/record.
- **Efficiency** — fewer errors/miscommunication (notes + skills + case history passed on).
- **Real-time support/monitoring** — supervisors can **barge-in / listen** for training (covered in Supervisor Console).

## Notes / gaps
- Warm vs blind transfer is the key agent decision — warm for complex/escalated cases (context handoff), blind for simple routing.
- Manual dialer is configured in [[dialers]]; the call controls here are shared across inbound/outbound voice in the [[../care-console/overview]].
- Supervisor barge/listen ties to the (un-ingested) Supervisor Console module.

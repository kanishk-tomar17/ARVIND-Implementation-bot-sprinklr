# Call Controls (Inbound Voice 160)
**Source:** Product Foundation Courses → Inbound Voice / 160 Call controls (video transcript + demo; terms slide captured) · **Help:** search `site:sprinklr.com/help call controls transfer warm blind agent`

## What it is
When an inbound/outbound call is accepted, **call controls** appear on the agent's screen (in the Care/K console). Visibility depends on the **call state** and **admin permissions**. (Inbound: customer picks "agent" in IVR → call routes to available agent → **call pop-up** appears.)

## Key terms
- **Inbound call** — initiated by a customer to the contact centre.
- **Outbound call** — initiated by an agent to the customer.
- **Primary agent** — first to interact (accepts inbound / makes outbound).
- **Secondary agent** — joined after being transferred/conferenced; **stays secondary until the primary leaves**. If the primary drops, the secondary **becomes the primary**.

## Controls in Sprinklr (permission-gated)
**Talk timer, Mute, Hold, End, Leave Call, Transfer**, and **After Call Work (ACW)** trigger.

### Transfer — 3 types
**Transfer to Queue, Transfer to Agents, Transfer to IVR.** For **queue transfer**, two modes:
- **Warm transfer** — call goes to a queue (supervisor/other agent); **customer on hold**; when the secondary accepts, the **primary briefs** them, then primary can **stay** in the call or **leave** (transfer completely).
- **Blind transfer** — call **ends from the primary** immediately; customer on hold waiting for any available agent; the agent who accepts becomes the **new primary**.

## Use cases
- Another agent can serve the customer better; customer followed the **wrong IVR flow** (redirect/transfer); collect **confidential info** (OTP, card number) — transfer to a secure flow/agent; customer insists on a **supervisor**.

## Demo note
Agent must **mark themselves Available** to receive the call pop-up. On accept, call controls (incl. Transfer and ACW) appear in the console.

## Notes / gaps
- Controls live in [[care-console]]; transfer-to-IVR ties to [[ivr]]; ACW → [[acw-builder]]. Permissions set by admin ([[roles-permissions]]).
- Part of Inbound Voice: [[telephony-integration]], [[voice-connectivity]], [[custom-fields]], [[ivr]], [[persona]], [[care-console]], [[guided-workflows]], [[disposition-plan]], [[acw-builder]].

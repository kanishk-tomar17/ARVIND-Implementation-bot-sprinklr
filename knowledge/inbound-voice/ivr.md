# IVR (Inbound Voice 156)
**Source:** Product Foundation Courses → Inbound Voice / 156 IVR (video transcript + demo) · **Help:** search `site:sprinklr.com/help IVR types inbound transfer conference wait time`

## What it is
**IVR (Interactive Voice Response)** — automated caller interaction via **voice + keypad (DTMF)**; pre-recorded menus, self-service, call routing. Significance: enhances CX/self-service, reduces cost (fewer agents needed), improves **call routing** (direct to right dept/agent), and captures data for insights.

## IVR types supported in Sprinklr
- **Inbound IVR** — standard/basic IVR flow (the default).
- **IVR Transfer / Connect-back** — agent/customer redirects the call to an IVR so the IVR can take subsequent use cases/queries.
- **IVR Conference** — agent adds an IVR into a live call (supported by limited providers — e.g. **Twilio**).
- **Open Dialer / Phone Dialer IVR** — IVR triggered to a customer first (presents options), then connects to an agent if required.
- **IVR Call Another Flow** — **hierarchical** IVR: jump from one IVR to another.
- **IVR Wait Time** — runs a workflow while the customer is **in queue** waiting for an agent.
- (Also: IVR System.)

## Configure (demo)
- **Home → Voice → IVR** (IVR Builder) → **Create IVR** → choose **type**, **language**, **timeout message**, **invalid message** (voiced when the customer presses an unlisted option), and **visibility** (share across workspace / user types).
- Build the flow per requirement, then **link the IVR to a Voice Application** in the **IVR Process** field → whenever a customer dials that number, this IVR process plays. (See [[telephony-integration]].)

## Notes / gaps
- Deep IVR node/build detail is in the dedicated **IVR module** ([[communication-nodes]], [[system-nodes]], [[api-integration]], [[disconnect-journey]]). This topic = IVR **types** + linking to a Voice Application for inbound voice. Every voice customer (Lenskart, HDFC) uses IVR.
- Part of Inbound Voice: [[telephony-integration]], [[voice-connectivity]], [[custom-fields]], [[persona]], [[care-console]], [[guided-workflows]], [[call-controls]], [[disposition-plan]], [[acw-builder]].

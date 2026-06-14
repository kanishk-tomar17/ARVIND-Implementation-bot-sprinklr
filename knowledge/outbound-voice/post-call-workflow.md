# Post Call Workflow (Outbound Voice 169)
**Source:** Product Foundation Courses → Outbound Voice / 169 Post Call Workflow (video transcript) · **Help:** search `site:sprinklr.com/help post call workflow journey facilitator voice campaign`

## What it is
A **sequence of automated tasks that run after a call ends**, as part of the campaign — to keep engaging the customer and ensure the message lands even if the call was unsuccessful.
- **Examples (omnichannel):** customer doesn't pick up → send a **WhatsApp** "we tried to call"; picks up → auto-send a **product link**; voicemail → reminder follow-up; "interested but needs time" → schedule a follow-up call or send a nudge email.
- **Benefits:** efficiency (automate follow-ups/scheduling/record updates), engagement, higher conversion, consistent communication, data tracking.
- **Use cases:** sales (interested → follow-up + link), debt collection (can't pay → reminder/schedule), surveys (thank-you + compile data), appointment confirmation, promotional (discount follow-up).

## Building it — Journey Facilitator
**Sprinklr Service → Resolve → Journey Facilitator** → **Create Journey** (a journey = the set of post-call steps, then attached to the campaign).
1. **Create journey:** name → select the **campaign** → select **audience** (segments) **or** make it **trigger-based** (fires on conditions/a rule) → Save & proceed.
2. **Journey builder nodes:** **Send message**, **Send resolve message**, **Send survey**, **Custom field check** (decision box — e.g. branch on *voice conversation customer connected = true* vs a default "not connected" path), **Schedule call** (pick dialer, business hours, optional outbound-IVR automated message, timeout), **Add delay** (e.g. 1 day), **End**.
   - *Send message* options: a **resolve message** (name/account/phone/text) or pick an **approved asset from the DAM**, then choose the **account/channel** (WhatsApp, SMS…). **Preview** what the customer sees.
   - *Example:* not connected → send a message; connected → send a product link → optional **scheduled call after a delay** → End → **Save as draft** / **Save and deploy**.
   - **Clone** a deployed journey to edit; add more paths for different call outcomes (connected-but-busy, connected-no-answer).

## Attaching to a campaign
**Voice Campaign Management → Post Call Workflow** option → select the journey → Save (new or existing campaign).

## Notes / gaps
- Journeys are built in **Journey Facilitator** (the same engine as broader journeys) and **bound to the campaign** via the Post Call Workflow field.
- The **custom-field/voice-conversation "connected" check** is the key branch — drives connected (send link/schedule) vs not-connected (omnichannel nudge) paths.
- Schedule-call nodes can re-enter the dialer ([[dialers]]); suppression "don't call" requests are added here/ACW → [[suppression-list]].

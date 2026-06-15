# IVR Communication Nodes (IVR 146)
**Source:** Product Foundation Courses → IVR / 146 IVR communication nodes (video transcript + demo; node-list slide captured) · **Help:** search `site:sprinklr.com/help IVR communication nodes gather response operator says`

## IVR basics (high-level call flow)
A customer dials a number → call lands at their **network provider** (e.g. Airtel) → routed to Sprinklr's **telephony partner** (integrated) → if the number is configured in Sprinklr, the IVR runs. IVR is built on a **canvas** of components: **communication nodes, system actions, agent actions**.

## The 7 communication node types
1. **Gather Customer Response** — collect input via **keypad entries** (preferences, account info).
2. **Gather Customer Language** — let the customer **select preferred language**.
3. **Operator Says** — **voice out** information (text→speech, recorded prompt, or a variable).
4. **Send SMS / Email / WhatsApp** — send communications on those channels (order confirmations, statements, offers).
5. **Deflect** — deflect to alternate channels (SMS, WhatsApp, Live Chat, FAQs, KB, chatbot) to **reduce call volume at high wait times**.
6. **Send to Voicemail** — let customers leave a recorded message when agents are unavailable (assigned to an agent to call back by query type/priority).
7. **Send Survey** — send a **digital survey** (link via SMS/WhatsApp/email) for feedback after the call.

## Configuring nodes (demo)
- **Launchpad → Voice → IVR** → **Create IVR** → name it, select **language(s)** (e.g. English + Spanish) → Save → canvas UI to add components.

### Operator Says
Name the node; provide the message via: **Text** (converted by **TTS** to speech), an **uploaded recording/prompt**, or a **variable** (also TTS'd, e.g. voice out the caller's name). Define the equivalent message per language (English, Spanish).

### Gather Customer Language
Message e.g. "Press 1 for English, 2 for Spanish." Option to **ask every call** (checked) or **skip if language already known / treat as preferred** (unchecked). Define **valid responses** (1→English, 2→Spanish), a **default path**, number of **retries** (e.g. 3), **timeout** + **invalid-input** messages (played before each retry); after retries exhaust → default path.

### Gather Customer Response
Define **number of input digits expected** and valid digits (e.g. "Press 1 for query, 2 for complaint" → 1 digit, valid 1/2) → creates **multiple paths** per input for custom logic; set retries.
- **Multi-digit input** (e.g. 10-digit phone): set number of input digits, save to a **variable** (e.g. `phone number`) for later decisioning.
- **Unknown-length input:** don't set digit count — instead define an **end key** (e.g. instruct "enter phone number followed by #") → takes input until the customer presses **#**; save to a variable.

### Send SMS / Email / WhatsApp
Name node; choose channel (SMS/Email/WhatsApp); select **account** to send from; set **phone number** (e.g. use the **Caller ID** variable); optional **send time** (blank = immediately); type the **message** or pick an **asset**. Save → node executes during the call. Email/WhatsApp configured similarly.

### Send Survey
Similar to Send SMS/Email/WhatsApp — sends a survey link on the chosen channel.

## Notes / gaps
- A ~1:01–9:54 segment (extended IVR-overview intro + start of node detail) wasn't captured; the 7-node list (slide) + per-node config above is complete.
- **Variables** captured here (phone number, caller ID) feed decisioning across the IVR — see [[system-nodes]], [[api-integration]]. Other IVR topics: [[disconnect-journey]], [[transaction-reporting]], [[pci-input]].

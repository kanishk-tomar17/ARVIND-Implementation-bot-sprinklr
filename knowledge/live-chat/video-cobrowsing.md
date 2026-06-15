# Video Call & Co-browsing Configuration (Live Chat 094)
**Source:** Product Foundation Courses → Live Chat / 094 Video call and co-browsing configuration (video transcript + demo) · **Help:** search `site:sprinklr.com/help live chat co-browsing invite asset screen control annotation`
*(The video focuses on **co-browsing**; video-call enablement follows the same support-ticket pattern.)*

## What co-browsing is
Lets an **agent see the customer's screen** in real time to guide them through product purchases, complex form-filling, or confusing info — **while preserving privacy/security**.
- **Value:** reduces average resolution time, reduces care cost (fewer follow-ups), reduces **cart abandonment**.
- **Use cases:** banking (guide through net-banking processes), e-commerce (help through the **payment step** / drop-off points).

## Configuration — 3 steps
1. **Raise a support ticket** to enable co-browsing: include **partner details, expected session volume, and number of agents** who'll use it.
2. **Create a co-browse asset:** Sprinklr **Social → Assets (Digital Asset Manager)** → create a **chat-only template** of type **"Co-browse invite"** → set **title, description, accept label, deny label** → Save.
3. **Set up via Live Chat Builder:** in the **Co-browsing** section, toggle **ON** → select the **co-browse request asset** created above.
   - Option to let customers **hide a particular URL** from agents (screen shows **blacked out** for sensitive/payment pages).
   - **Cross-domain:** add URLs to support co-browsing across domains.
   - **Update** the app.

## Capabilities
- **Mask/redact certain URLs** from agents (in the Builder).
- **Mask specific fields** (e.g. a card number) — raise a **support request**.
- **Screen control** — agent can take control of the customer's screen (edit forms, browse for them).
- **Annotation** — agent can annotate/point on the customer's screen.
- **Screen sharing** — customer can share their **entire screen** (not just one browser tab).

## User experience
1. Agent **requests a co-browsing session** → the **request asset** is sent to the customer.
2. Customer **accepts/rejects**. On accept: the agent sees the customer's screen load; the customer sees a bar *"the agent is viewing your screen"* with an option to **stop co-browsing anytime**.
3. **Screen control:** agent requests → customer accepts/denies → bar shows *"screen control in progress"* → agent can browse/control (open tabs, navigate, interact).
4. **Annotation:** agent points/annotates on the customer's screen.

## Notes / gaps
- Co-browsing (and video call) **must be enabled via support ticket** first — not self-serve.
- Privacy controls (URL masking, field masking, customer "stop" button, blackout of sensitive pages) are the compliance backbone — highlight these for finance/PII use cases.
- Pairs with [[chat-deflection]] (088) — social→live-chat deflection is often the trigger for starting a co-browse/video session.

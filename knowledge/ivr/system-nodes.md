# System Nodes in IVR (IVR 150)
**Source:** Product Foundation Courses → IVR / 150 System nodes in IVR (video transcript + demo) · **Help:** search `site:sprinklr.com/help IVR system nodes decision set priority set skills`

## IVR recap
IVR = the **first level of interaction** when a customer calls a brand; the customer interacts via **DTMF input** ("press 1 for English…"). Benefits: efficiency, 24/7, personalized (greet by name), faster resolution, omni-channel, cost saving, **routing & prioritization**.
- **Create:** IVR Manager → **Create IVR Flow** → name, select **languages** (e.g. English, Hindi), define **timeout** + **invalid message** per language → Save → canvas.

## Three node types on the IVR canvas
1. **Communication nodes** — hold the conversation with the customer (see [[communication-nodes]]).
2. **System nodes** — define **business logic / decisions / rules** + data retrieval (this topic).
3. **Route/Forward node** — forward/route the call from IVR to an agent.

## System nodes (enable decision-making & data retrieval)
- **Decision box** — create **multiple paths** based on a condition (e.g. priority vs non-priority customer → different experiences; priority gets direct-agent option).
- **API** — push/pull data from an external system (e.g. fetch by phone number / customer ID) and use it in the flow → key for **self-service journeys**. (See [[api-integration]].)
- **Custom Field Action** — **set / add / merge** a **case or profile custom field** in the IVR.
- **Set Priority** — set the caller's priority; later used by **Unified Routing** to assign the call/case (prioritize high-priority customers).
- **Set Skills** — set skills in the IVR; **Unified Routing** uses them to assign to the **best/expert agent** with that skill (e.g. a language skill → agent with that skill).
- **Add / Remove Queues** — add the case (the call's case) to, or remove it from, a **case queue** (queues drive many rules).
- **Merge Profile** — merge the customer's different profiles into the **universal profile**.

## Notes / gaps
- System nodes feed **Unified Routing** (priority/skills → agent assignment — see [[routing-configuration]], [[agent-skills]]) and use [[queues]] + [[custom-fields]]. API node detail in [[api-integration]].
- Part of IVR: [[communication-nodes]], [[disconnect-journey]], [[transaction-reporting]], [[api-integration]], [[pci-input]].

# Different Nodes in a Dialogue Tree — Advanced (Conversational AI 101)
**Source:** Product Foundation Courses → Conversational AI / 101 Different Nodes in a Dialogue Tree - Advanced (video transcript) · **Help:** search `site:sprinklr.com/help dialogue tree fallback timeout manage records deflect scheduled callback`

## Scope
Advanced nodes: **fallback & timeout, accumulating user replies, Manage Records, Define Variable (3 nodes), Scheduled Callback, Deflect.**

## Fallback & Timeout (on a User Reply node)
- **Local fallback** — when the user replies unexpectedly (e.g. *"I don't know"* to a question expecting a specific answer), gives a **default response** or guides the user **back to the expected options**.
- **Timeout** — fires when the user doesn't respond within a set time; sends a **reminder** or runs predefined actions.
- **Handle invalid user reply** options (e.g. bot asked for a 10-digit phone, user sent 9 digits):
  - **Insert invalid user reply path** — adds a new path to configure nodes.
  - **Define FAQs** — catch an intent and give a specific answer.
  - **Invalid reply setting** — publish a bot reply, set **how many times** to repeat; a checkbox **repeats the parent bot reply**.
- **Timeout screen:** set the **wait time** (e.g. 5s), the bot reply to publish on timeout, the **repeat count**, and the same two checkboxes as fallback.

## Accumulating user replies
- When a customer **breaks a query into multiple small messages**, the bot **waits N seconds** (e.g. 5s) to receive them all, then **stitches them into a single query** for a more accurate reply.
- Config: just specify the **wait time**.

## Manage Records node
- **Fetch / update / create** single or multiple records from Sprinklr entities (**case, profile, custom**), filter as needed, **store in a variable**, sort asc/desc. Three operations: **Get / Update / Create records**.
- Config (Get): name the node → **select entity** → **define a variable** → choose **single/multiple** → set **conditions** (e.g. mobile number matches) → **Save**. The variable is then usable in bot replies, decision boxes, etc. (Update/Create configured the same way.)
- This is the in-dialogue-tree equivalent of GW [[../guided-workflow/records-manipulation]].

## Define Variable — three nodes
1. **Update Properties** — assign the value of an output parameter (e.g. **JSON output**) to a variable, for use in decision boxes/bot replies. Write **custom code** or select a **pre-existing global variable**.
2. **Business Hours** — select business hours → define an **"is in business hours"** variable (true if the message arrives within hours); can also expose start-of-business-hours format.
3. **Work Queue Properties** — define a variable for a **work queue**; exposes properties like **idle agents, agents available, wait time**, usable in decisions/replies.

## Scheduled Callback
- Schedules a **callback to the customer at a later time**. Example: user contacts the brand **after business hours** wanting an agent → a call is scheduled and placed **when an agent becomes available**.
- Config: set the node properties, then **assign a journey, a work queue, or a specific agent** → when the agent is available the case is assigned and the call placed.

## Deflect node
- **Deflects the user's chat from one channel to another** while keeping the **same case** throughout.
- Use cases:
  - **Voice/IVR → messaging** (a query a configured bot can resolve → user gets a message on another channel).
  - **WhatsApp → Live Chat** (e.g. appointment-booking asset exists only in Live Chat → send a link → user is redirected, books, returns).
- Config: name the node → **Deflect to channel** (e.g. WhatsApp Business) → **account** → optional checkbox to send the asset to the **current** channel → select the **asset** for the deflected channel → select the **channel/account** to deflect via → choose a **URL shortener** if sending a URL → **Save**.

## Notes / gaps
- Builds on [[dialogue-nodes-basic]] (100). Work-queue/business-hours variables tie bot logic to routing and [[../case-management/assignment-rules]].
- Deflect keeps one case across channels — important for reporting continuity; pairs with [[../live-chat/chat-deflection]].
- Manage Records inside a bot uses the same entity model as [[discovery-run]]/CRM data.

# Different Nodes in a Dialogue Tree — Basic (Conversational AI 100)
**Source:** Product Foundation Courses → Conversational AI / 100 Different Nodes in a Dialogue Tree - Basic (video transcript) · **Help:** search `site:sprinklr.com/help dialogue tree nodes bot reply user reply DTMF decision box assign agent`

## Scope
Configuring the core node types in a dialogue tree: **Bot reply, User reply, DTMF, Decision box, Assign to Agent, End of conversation vs End of dialogue tree, Transfer to another tree, Custom field actions.**

## Bot Reply node
- Add: addition (+) icon → **Bot Reply** → name it → enter the bot response.
- **Conditions/checkpoints:** detect a **profile property, message property, or bot-level property** (e.g. set user language = English → bot replies in English).
- **Groovy** can be written in the bot response to build a **dynamic response** from fields in the AI flow.
- **Smart paraphrase** — AI-powered suggestions for articulate, grammatically correct responses, faster.
- **Best practice:** add **multiple variations** of the response so the bot feels more human.
- **Assets:** use existing assets from the Sprinklr panel as the response, or create a new one.

## User Reply node
- Add: addition icon → **User Reply** → choose one of two filters:
  - **Match Intent and Entity** — captures an intent, optionally an entity. E.g. *"I would like to close my account"* → intent **Account closure**, entity **account**. The value can be **saved to a parameter** for later use.
  - **Match only entity** — captures **discrete input** like confirmation number, username, email address.

## DTMF node (voice)
- **DTMF** = Dual-Tone Multi-Frequency — the tones from telephone keypad presses (numbers/symbols/commands).
- Add: addition icon → **DTMF Response (voice)** in the three-dot menu → name it → set **number of input digits** → add **valid digit values** → add the **operator response** in the text reply section → **Save**.
- Then configure each branch originating from the DTMF response individually.

## Decision box
- Directs the user down a path based on **one or more conditions**.
- Add: addition icon → **Decision box** → add a **path** (name it, add conditions) → **Save**. Add multiple paths.
- A decision box **always has a default path** — taken when **none** of the configured conditions are met.

## Assign to Agent node
- Hands the conversation to an agent (e.g. customer drops off mid-payment and needs human help).
- Add: addition icon → **Assign agent** node.
  - **Select a work queue** → case goes to an available agent in that queue, **or**
  - **Leave the work queue blank** → the **Bot Application / Conversant State** system field is set to **"routed to agent"** in the back end; use that property in the **Rule Engine** to route the case into the right queue later.

## End of conversation vs End of dialogue tree
- Both are terminal nodes. **End of dialogue tree** ends the current tree; **End of conversation** signifies the whole bot conversation ending. *(Exact distinction detail is in the Sprinklr KB — verify per implementation.)*

## Transfer to another dialogue tree
- A node lets you **transfer flow from one dialogue tree to another**, so trees can be modularised and chained. *(Config detail in the KB.)*

## Custom field actions
- Use a **custom field's value** to drive a **decision box** later in the flow, or decisions in the **Rule Engine**.
- Configure: addition icon → **Custom field actions** → define the **action** to execute → choose the **custom field** to tag → set the **value** to tag into it.

## Notes / gaps
- Builds on [[dialogue-tree-basics]] (099); advanced nodes are in [[dialogue-nodes-advanced]] (101).
- The 7:11–9:40 segment (full *end-of-conversation vs end-of-dialogue-tree* and *transfer-to-another-tree* walkthroughs) wasn't fully captured in the transcript scrape — confirm those two on the Sprinklr KB if a consultant needs exact steps.
- "Assign to agent with blank queue → routed-to-agent flag → Rule Engine" is the key pattern linking bots to [[../case-management/assignment-rules]] / routing.

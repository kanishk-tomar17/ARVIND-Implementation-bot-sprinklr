# Basics of Dialogue Tree (Conversational AI 099)
**Source:** Product Foundation Courses → Conversational AI / 099 Basics of Dialogue Tree (video transcript) · **Help:** search `site:sprinklr.com/help dialogue tree trigger filters bot reply user reply node`

## What it is
A **dialogue tree** is the structured **blueprint of a bot conversation** — the systematic arrangement of an exchange between a user and a virtual agent, where flow is driven by the bot's questions and the user's responses. It's a collection of **interconnected nodes**; each node can present information, accept input, or manipulate data, triggering a pathway through the dialogue.

## Configuring a dialogue tree
1. On the application landing page, go to **Build → Dialogue Trees**.
2. Click **Add Dialogue Tree** (top-right).
3. In **Create Dialogue Tree**: enter a **name** and **language** → **Save**.
4. Then add nodes/responses to build the flow.

## Trigger filters
**Trigger filters** are the **checkpoints/conditions** that must be met for the dialogue tree to execute. Conditions can be any type (e.g. **intent detected**, **user type**).
- Configure: open the tree → click the **Trigger Filters** node → **edit** → select the condition.
- Example: **Detected Intent = Account Closure** → the tree runs **only when** the *account closure* intent is detected.

## Node types
- **Bot reply node** — where the bot generates and delivers a response (information, guidance, or an action). Can include **text, images, buttons, or prompts**.
  - Add: **Add element → Bot reply** → enter **text** or choose from **Sprinklr chat templates**.
- **User reply node** — where the system **awaits and processes the user's response**. Acts as the interaction point for input/answers/preferences.
  - Add: **Add element → User reply** → choose a filter: **match intent AND entity**, or **match entity only**.
  - Example: select *match intent and entity* → specify intent **Account Closure** → name the node → **Save**.

## Canvas operations
- **Auto Layout** — automatically organises and arranges nodes/connections for readability. One click turns a messy tree into a clean, retraceable one.
- **Create a connection** — drag-and-drop the **open node** of an element to the target spot.
- **Break a connection** — click the **crosshair** on the connection → **Delete connection**.
- **Subtree ops (three-dot menu on a node):** **Move element with subtree** (pick destination), **Copy element with subtree** (pick destination), **Delete element with subtree**.

## Notes / gaps
- Trigger filters are how an intent ([[intents]]) routes into a specific dialogue tree; user-reply nodes match on intents + entities ([[entities]]).
- Node *types* in depth are covered in [[dialogue-nodes-basic]] (100) and [[dialogue-nodes-advanced]] (101).
- Auto Layout is purely cosmetic but essential for maintaining large trees.

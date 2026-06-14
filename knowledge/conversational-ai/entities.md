# Entities & Entity Creation (Conversational AI 098)
**Source:** Product Foundation Courses → Conversational AI / 098 Entities & Entity creation (video transcript) · **Help:** search `site:sprinklr.com/help conversational AI entity slot ASR contextualization` (public KB has 5 detailed articles)

## What it is
An **entity** is a **structured piece of information inside a user's message** — any detail that may be reused later in the conversation.
- Example: *"I'd like to book a flight to Sydney"* → entity **Destination** = value **Sydney**.
- Other examples: email ID, address, name, etc.
- Capturing entities makes the bot **smarter** — it pulls relevant user details to drive subsequent bot workflows, improving **deflection rates**.

## Slots
**Slots** are an **advanced form of entities**: they let the bot **reuse a value already mentioned earlier** in the conversation, so it can **smartly skip re-asking** for it.

## Configuring an entity
1. **Conversational AI → AI Tools → Entity.** (Environments usually already have many entities.)
2. Click **Add entity** (top-right) → fill the form.
3. An entity can be based on:
   - a **regex**, or
   - a **keyword match query**.
4. **Multilingual:** one entity supports **multiple languages**.
5. To capture specific values (e.g. *Sydney*, *New Delhi* as a Destination):
   - Toggle to **leverage existing entities/slots**, or
   - Use **keyword match queries** to configure **synonyms, spell-fix, variations, and business logic** that detect those values as the entity.

## Default entities
On a newly created environment, **7 default entities** are provided (frequently used in bots): time formats (24h/12h), **phone number**, **email**, **date**, **alphanumeric** character, etc.

## Advanced (later sessions / public KB)
- Creating a **regex**, building a **keyword magic query**, and **ASR contextualization** (advanced, used in chatbots).
- Sprinklr's **public KB has a 5-article series** covering the full entity creation process, slots, and ASR contextualization.

## Customer example
Sprinklr itself uses entities in its own chatbot — entities built to identify specific **keyword-match queries based on business validation** and to trigger specific keyword/brand-related queries.

## Notes / gaps
- Intents = *what the customer wants*; entities = *the specific details inside the request*. Both feed the bot's [[dialogue-tree-basics]].
- Slots are the mechanism that prevents a bot from re-asking for info the customer already gave — key to a smooth flow.
- Exact regex/keyword-query syntax and ASR contextualization are in the public 5-article KB, not memorised here.

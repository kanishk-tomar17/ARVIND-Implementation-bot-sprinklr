# Customer Memory in AI Agent (Contextual Memory)
**Source:** sprinklr.com/help — https://www.sprinklr.com/help/articles/monitor-workflow-audit-logs/customer-memory-in-ai-agent/6ab20bbda7b8f581fcbb2598

**Also:** https://www.sprinklr.com/help/articles/ai-agent-voice/conversation-settings-advanced-controls/6a452bc989aa7c7d6a01d114 (Conversation Settings: Advanced Controls)

## What it is
- Lets an AI Agent remember a customer across conversations. Without it, conversations are stateless.
- **Off by default.** Turn on in AI Agent Builder: **Build > Conversation Settings > Contextual Memory > "Enable Contextual Memory"**. The article points to "Conversation Settings: Advanced Controls" for more settings (not documented in the article itself).

## What is stored (per customer memory profile)
- **Profile attributes:** configured attributes, sourced from profile custom fields.
- **Semantic Memory:** long-term customer facts and preferences, categorised, with a relevance score, continuously updated.
- **Episodic Memory:** timestamped summaries of key events/outcomes from past conversations, with a relevance score.

## When it is created
- After a conversation meets the **configured memory criteria** and stays **inactive for a defined duration**, the agent extracts profile attributes, semantic and episodic memory and stores them on the customer's profile.
- The article gives no default criteria, no default inactivity period and no availability delay.

## How the agent uses it
- **Automatic.** Relevant memory is added to the AI Agent prompt on later interactions. No placeholder, variable or tool has to be referenced in the prompt.
- The injected context can include configured profile attributes plus relevant semantic and episodic records.

## Settings under Conversation Settings > Contextual Memory (Advanced Controls article)
- **Enable Contextual Memory:** "Retrieves relevant context at the start of a conversation and updates it when the conversation ends." (so retrieval is per conversation start, not per message)
- **Memory Selection Criteria** (+ Add Condition): which conversations are eligible for memory processing.
- **Profile Attributes** (Select Attribute, Attribute Description): customer profile attributes used as *conditions* for memory processing.
- No defaults/allowed values, inactivity duration, injection limits or relevance threshold are documented there; nothing says whether the Router (vs tasks) receives memory, or how anonymous vs authenticated customers are keyed.
- Practical check: if memory records exist but never show up in a prompt, review the selection-criteria conditions and the attribute conditions — a chat that does not satisfy them may be excluded.

## Where to look / troubleshoot
- **Monitor > Customer Memory:** list of memory profiles with episodic/semantic counts, last modified, categories covered. Open a profile to see its attributes, semantic and episodic records.
- **Injection Prompt icon** in the Profile Memory window: shows what gets injected.
- **Monitor > Audit Logs:** the task's full prompt includes the injected memory, so you can confirm whether memory actually reached the model.

## Not documented (verify in-tenant, don't assume)
- How a chat is matched to a memory profile. Consultant-reported, NOT in the article (verify): an anonymous chat gets a profile created from IP + browser, so memory follows the browser/IP, not the person; a new browser, incognito or another network starts an empty profile. Authentication needs are still undocumented. Observed in AI Agent audit metadata (inference, verify): identified chats carry profileId SPRINKLR_LIVE_CHAT_C_<customer account number>, anonymous chats SPRINKLR_LIVE_CHAT_A_<24-hex id> (the same hex ids appear as unnamed rows in Monitor > Customer Memory). To check whether memory reached the model, search the request's system prompt for a known memory fact.
- **Router / Groovy-generated prompts (consultant-supplied, not in the help article — verify):** memory is injected automatically into task prompts, but a Router whose prompt is built by a Groovy script gets nothing unless the script appends the memory variable. Pattern: `if (UNIVERSAL_PROFILE_MEMORY) { rv += '\n' + UNIVERSAL_PROFILE_MEMORY; }` plus an instruction sentence naming the "Customer Personalization Context" section. Observed before this was added: an identified profile's Router request had no memory block. Guard the variable (try/catch) so chats without memory do not break the script, and test an anonymous chat.
- The memory criteria and inactivity duration values.
- Any recommended prompt wording for how the agent should talk about remembering a customer (privacy, what it may say). The model's default stateless reply ("I don't have access to previous conversations") can still appear unless the prompt says otherwise.

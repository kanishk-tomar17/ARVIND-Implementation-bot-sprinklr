# Intents & Intent Creation (Conversational AI 097)
**Source:** Product Foundation Courses → Conversational AI / 097 Intents & Intent creation (video transcript) · **Help:** search `site:sprinklr.com/help intent model create intent train`

## What it is
An **intent** automatically identifies a **customer's intention**. Sprinklr AI classifies messages into **niche categories (intents)**, giving deeper insight into what customers want — which chat/voice bots use to **trigger the right bot workflow** and resolve the query, improving **deflection rates**.

## How AI detects an intent (background)
1. Break the customer expression into **individual words**.
2. Identify **relevant phrases**.
3. Detect the **intents**, tagging the dominant one as **primary**.
- Example: *"My device takes too long to charge, please replace it"* → two intents detected: **Replacement** and **Product complaint** (slow charging). The customer's main goal is replacement → **Replacement = primary intent**.

## Why intents matter
- **Without** intents: no automated filtering, prioritisation, or efficient routing → fewer cases solved, longer response times.
- **With** Sprinklr AI: messages go beyond engageable/non-engageable into **niche intents** → bots auto-answer, and you get **filtering, prioritisation, and routing** based on what the customer is actually talking about.

## Configuring an intent
1. **Sprinklr Service → Conversational AI → Intent Model.** (A **model** = a group of intents.)
2. **Create the model:** Create intent model → **name** it → turn the **"Disable AI" toggle OFF** → **Create**.
3. Open the model. It may already hold predefined intents.
4. **Add an intent:** click **Add intent** → name it → **Save**.
   - Example intent: *Account opening* (customer asks how/wants to open an account).
5. Add **expressions** (sample utterances) to the intent:
   - The model is **multilingual** — add expressions in English or additional languages.
   - **Sprinklr AI can auto-generate expressions** — add them to the model with one click instead of writing all by hand.
6. Click **Train** to build the model.

## Beyond the basics (covered in later sessions)
A production-ready model also needs: **golden test set** ([[golden-test-set]] 107), **accuracy improvement**, and **deployment**.

## Customer example
Brand "Esalinga" built intent models in the UI from topics surfaced in their **Discovery Run** ([[discovery-run]] 096), then used those intents in **chatbot workflows** to identify customer needs and trigger the right workflow.

## Notes / gaps
- Intents are the bridge between Discovery Run (what customers contact about) and the bot ([[dialogue-tree-basics]]) that acts on it.
- One message can carry multiple intents; the **primary** intent is what routing/bot logic keys off.
- AI-generated expressions speed up training but still feed into the golden-test-set/accuracy loop before go-live.

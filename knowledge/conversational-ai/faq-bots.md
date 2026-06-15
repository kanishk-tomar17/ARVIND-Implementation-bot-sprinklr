# FAQ Bots (Conversational AI 103)
**Source:** Product Foundation Courses → Conversational AI / 103 FAQ Bots (video transcript) · **Help:** search `site:sprinklr.com/help FAQ bot create excel asset manager`

## What it is
**FAQ bots** let support teams scale and provide **24/7** support, handling **repetitive enquiries** so agents focus on complex issues and meet SLAs. They deploy across preferred customer channels, improve first-time response and agent efficiency, and yield data for strategy. **Supports 15 languages.**

## Create an FAQ bot via Excel
1. **Sprinklr Service → Conversational AI** → search/select your application → **FAQ Bots** (under **Build**).
2. Click **Add FAQ bot** (top-right) → enter **name, description, language**.
3. Under **FAQ source**, choose **Import from Excel**.
   - **Download the sample Excel** to see the required format; fill it in and **upload**.
4. **Save**, then **configure replies** for the imported questions:
   - **Multiple replies** can be set for a single question.
   - **Multiple question variations** can map to a single answer.
5. **Save** → the bot is ready to deploy on the customer's channels.

## Create an FAQ bot manually (from scratch)
1. **FAQ Bots → Add FAQ bot** → name/description/language → **FAQ source = Start from Scratch**.
2. On the bot configuration page:
   - Give the **query a title**.
   - Add the **question variations** a customer might ask (or select from existing **intents / test sets** already in the application).
   - Configure the **text reply** the bot gives when it recognises the query; add **multiple reply variations** to feel more human.
3. **Save**.

## Response types (Asset Manager)
Edit a bot via its **three-dot menu**. A reply can be a plain **text reply**, or **Select from Asset Manager**:
- **Multi-option carousel**, **QR code**, **image**, **URL**, **dynamic image** — chosen per use case.
- Configure the asset → **Save**.

## Notes / gaps
- FAQ bots are the lightweight, no-dialogue-tree path for repetitive Q&A; full flows use the [[dialogue-tree-basics]] instead.
- Question variations can be sourced from [[intents]] (097) — reuse existing intent training rather than retyping.
- Asset Manager (carousel/QR/image/URL) is shared across bot types — richer replies than text alone.

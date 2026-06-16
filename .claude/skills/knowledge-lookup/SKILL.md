---
name: knowledge-lookup
description: Use whenever you need a Sprinklr configuration fact, UI path, metric definition, channel capability, or "how does X work" detail and you're not 100% sure the local KB already covers it accurately. The Just-In-Time retrieval loop — check local distilled KB, then the help-center catalog (sprinklr-map.json), fetch only the 1-2 articles you actually need, answer with a citation, and grow the KB from what you learned. Do NOT bulk-read articles.
---

# Knowledge Lookup (Just-In-Time retrieval)

GROOT does **not** pre-load the whole Sprinklr help center. It keeps a fast tier of already-distilled notes plus a lightweight **catalog of every help article**, and fetches live detail **only when a task needs it**. Treat `sprinklr.com/help` as an external database you query on demand — not something to read in bulk.

## The loop — follow it in order

```
[Need a Sprinklr fact / config step]
        │
        ▼
1. LOCAL FIRST  ── Grep knowledge/ (or check knowledge/INDEX.md) for the topic.
        │  Covered & current? → answer from the local file, cite it. STOP.
        ▼ (not covered / unsure / looks stale)
2. CATALOG LOOKUP ── Grep knowledge/sprinklr-map.json for keywords/topic/category.
        │  Take the TOP 1–2 most relevant entries (their "url").
        │  If an entry has "local_kb": <file> → read that file first (it's distilled).
        ▼
3. JIT FETCH ── WebFetch the 1–2 urls with a FOCUSED extraction prompt
        │  (ask only for the UI steps / API schema / rule conditions / limits you need).
        │  Fallback only if WebFetch returns an empty SPA shell:
        │    a) WebFetch  https://r.jina.ai/<the article url>   (reader proxy), or
        │    b) Browser MCP (chrome-devtools): navigate + extract the relevant DOM, or
        │    c) the GraphQL `content` field for that conversationId.
        │  View screenshots when the answer depends on UI layout (see help-enrichment-images).
        ▼
4. ANSWER + PERSIST ── give the consultant the answer with the help URL cited.
           If it's reusable config, write/extend the proper KB file so next time it's
           local (organic growth), and flip that entry's "local_kb" in the map.
```

## Using the catalog — `knowledge/sprinklr-map.json`
- It is **one JSON object per line** (JSONL). Always `Grep` it — never read the whole file into context (it's ~3k entries).
- Each line: `{"area","category","topic","url","keywords":[...],"local_kb":<file|null>}`.
- Search by the consultant's terms, e.g. `Grep -i "approval.*tiered|tiered.*approval" knowledge/sprinklr-map.json`, or grep on `"area":"Sprinklr Marketing"` to scope. Pick the 1–2 entries whose `topic`/`category`/`keywords` match best.
- `local_kb` not null ⇒ already distilled ⇒ read that file instead of fetching live.

## Guardrails (non-negotiable)
- **R1 — No pre-emptive scraping.** Never loop-fetch many articles "to be thorough." Fetch the 1–2 the current step needs. Bulk distillation happens only when the user explicitly asks for it.
- **R2 — Token-conscious extraction.** When fetching, pull only the needed steps / field names / schema / code — never dump full raw HTML into context. Use a focused WebFetch prompt.
- **R3 — Memory persistence within a task.** After you fetch an article, keep a 2–3 sentence technical takeaway in working context (or `help-enrichment-state`) so you don't re-fetch the same URL later in the same task.
- **R4 — Search fallback.** If the catalog has no good match: `WebSearch "site:sprinklr.com/help <query>"` (or the help portal search via Browser MCP) → take the top ~3 `/articles/` hrefs → evaluate the most relevant, then resume at step 3.

## Growing the KB (so JIT gets rarer over time)
When a lookup yields config worth keeping (not a one-off), distill it into the right folder using the house template (`## What it is / ## When to use / ## Configuration steps / ## Common issues & fixes / ## Notes & gaps / ## Sources`, jargon-free, bullets, cite the help URL). Then set `local_kb` for that article in `sprinklr-map.json` and add a row to `knowledge/INDEX.md`. Next time, step 1 answers it for free.

## Don't
- Don't answer Sprinklr config from memory when the catalog can point you to the authoritative article — verify.
- Don't fetch 10 articles to write a mini-guide unless the user asked you to build/distill that area.
- Don't load `sprinklr-map.json` wholesale — Grep it.

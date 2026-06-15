# Help-center enrichment — catalog & method (locked 2026-06-15)

Backbone for enriching GROOT's KB from **sprinklr.com/help** (whole platform, exhaustive). This folder is the **resumable tracking layer**; it is not GROOT knowledge itself.

## Files
- `sitemap-urls.txt` — all 3040 URLs from `https://www.sprinklr.com/help/sitemap.xml` (2978 `/categories/` + 61 `/topics/` + home). **The sitemap contains NO `/articles/` URLs** — categories are index pages; the real articles are discovered by scraping each category page.
- `catalog.md` — one row per enumerated article: `area | category | article-title | article-url | target KB file | status`. Updated as batches complete; lets every run skip done work.

## Locked pipeline — GraphQL API (proven 2026-06-15)
The help center is a Sprinklr **Community SPA** backed by a GraphQL endpoint. Plain `curl`/WebFetch can't read `/categories/` pages, BUT the GraphQL API gives everything fast and scriptable from an `evaluate_script` in the chrome-devtools browser (same-origin `fetch`).

**Endpoint:** `POST https://www.sprinklr.com/help/schema/community`
**Headers:** `content-type: application/json`, `x-community-id: 4e8e4610-73cc-4dcd-8768-50db50021004`, `x-baselanguage: en_US`, `x-language: en_US`, **`x-csrf-token: <token>`**.
**CSRF token** = the HttpOnly `communityToken` cookie — NOT readable via `document.cookie`. Get it each session by: navigate to any `/help/...` page → `list_network_requests` → find a `schema/community` POST → `get_network_request` → read the `x-csrf-token` request header. (Session-stable; re-capture per session. 2026-06-15 token was `121821d3-689e-4358-b34d-4208930a377b`.)

**Queries:**
- Area + children of a category (area = `hierarchy[0].name`; `categories:[]` ⇒ leaf):
  `{ community { category(id:"<ID>") { id:categoryId title hierarchy categories { id:categoryId title } } } }`  (`hierarchy` is a JSON scalar — return whole, extract `name` client-side.)
- Articles in a category (the gold):
  `{ community { conversations(conversationType:"POST" includeCustomPages:"false" includeComments:"false" includeHierarchyDetails:"true" appendLastReplyByUser:"true" first:100 types:[] excludeTypes:[{type:POLLS}{type:CONTEST}{type:CONTEST_ENTRY}{type:EVENT}{type:SURVEY}] topicIds:[] folderIds:[] sortKey:{type:ORDER} sortOrder:"ASC" dateFrom:0 page:0 isScopedEntity:true currentCategoryId:"<ID>" categoryIds:["<ID>"] applyUserSort:"false" tags:[] customFields:{} filterByCurrentCategory:true highlightKeywordEnabled:false) { totalCount edges { node { path title type content } } } } }`
  - `node.path` → article URL = `https://www.sprinklr.com/help/articles/<path>`. `type` = `KB_ARTICLE`. `content` = FULL body as HTML (huge — do NOT return to context; only request `content` in the distill step, and strip HTML).
  - Do NOT add subfields to `hierarchy` inside a node — breaks the query.

**Two steps:**
1. **Enumerate (in-page GraphQL, batched ~80 cats/call):** loop the 2978 category IDs from `sitemap-urls.txt`; per cat run `category()` (area) + `conversations()` (articles, no content). Return compact rows, persist to disk. ~30–40 evaluate calls total.
2. **Distill (parallel — Workflow):** per article, **WebFetch** `https://www.sprinklr.com/help/articles/<path>` (server-rendered → clean prose, small) and distill → KB markdown. WebFetch is parallelizable across workflow subagents (no browser). (Alternatively pull `content` via GraphQL + strip HTML, but WebFetch gives cleaner prose.)

## Product areas (mirror the help center)
Sprinklr **Service · Social · Marketing · Insights · AI · Platform** (+ each area's Getting Started / Glossary / Release Notes). Map to existing `knowledge/<module>/` folders where they overlap (enrich in place); create new folders (`social/`, `marketing/`, `insights/`, `ai-studio/`, `platform/`, `service/`, `glossary/`) for uncovered areas.

## File-ownership rule (safe parallel writes)
Each target KB file is owned by exactly one workflow subagent per run → no two agents write the same file. One file may aggregate several source articles.

## Resume
Re-runs read `catalog.md`, skip `status=done`, and continue. Enumeration and distillation are tracked separately (an article can be `enumerated` but not yet `distilled`).

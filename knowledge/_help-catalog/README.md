# Help-center enrichment — catalog & method (locked 2026-06-15)

Backbone for enriching GROOT's KB from **sprinklr.com/help** (whole platform, exhaustive). This folder is the **resumable tracking layer**; it is not GROOT knowledge itself.

## Files
- `sitemap-urls.txt` — all 3040 URLs from `https://www.sprinklr.com/help/sitemap.xml` (2978 `/categories/` + 61 `/topics/` + home). **The sitemap contains NO `/articles/` URLs** — categories are index pages; the real articles are discovered by scraping each category page.
- `catalog.md` — one row per enumerated article: `area | category | article-title | article-url | target KB file | status`. Updated as batches complete; lets every run skip done work.

## Locked pipeline (proven on "Content Variants")
The help center is a **client-side-rendered Sprinklr Community SPA** — plain `curl`/WebFetch CANNOT read `/categories/` pages (truncated SSR). Two-step method:

1. **Enumerate (browser, sequential — chrome-devtools):** navigate to a `/help/categories/<slug>/<id>` URL, then `evaluate_script` to scrape:
   - **Product-area breadcrumb** — `a[href*="/help/categories/"]` whose first crumb is the top area (e.g. `Sprinklr Marketing`).
   - **Child article links** — `a[href*="/help/articles/"]` → `{title, href}`.
   - This is the only browser-bound step (one Chrome tab, can't parallelize across workflow agents).
2. **Distill (WebFetch, parallel — Workflow):** WebFetch each `/help/articles/<cat>/<slug>/<id>` URL — these ARE server-rendered, so WebFetch returns the full body reliably. Distill → KB markdown. Parallelizable across workflow subagents (no browser).

## Product areas (mirror the help center)
Sprinklr **Service · Social · Marketing · Insights · AI · Platform** (+ each area's Getting Started / Glossary / Release Notes). Map to existing `knowledge/<module>/` folders where they overlap (enrich in place); create new folders (`social/`, `marketing/`, `insights/`, `ai-studio/`, `platform/`, `service/`, `glossary/`) for uncovered areas.

## File-ownership rule (safe parallel writes)
Each target KB file is owned by exactly one workflow subagent per run → no two agents write the same file. One file may aggregate several source articles.

## Resume
Re-runs read `catalog.md`, skip `status=done`, and continue. Enumeration and distillation are tracked separately (an article can be `enumerated` but not yet `distilled`).

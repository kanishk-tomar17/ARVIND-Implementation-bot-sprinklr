# AI+ Reporting (generic AI+ usage — covers Reply Assistance)

**Source:** https://www.sprinklr.com/help/articles/ai-reporting/ai-reporting/6964a8edc0c0b637f93ec65e

## Where
**Care Reporting → + Create Widget → data source "AI+ Reporting."**

## Metrics
- `AI+ Request Count`
- Token metrics: input, output, cached, audio, image, reasoning tokens
- `Latency` (response generation time)

## Dimensions
- Workspace, User, Timestamp, Configuration Set, Error Details, AI Provider, Temperature, **Prompt Node ID**

## Gap — verify in-tenant
The doc tracks AI+ usage **generically** (total request count), not broken out by which reply-box option was used (Reword vs Fix Spelling & Grammar vs Modify Tone vs Translate, see [[reply-assistance-ai-plus]]). `Configuration Set` or `Prompt Node ID` *might* map 1:1 to each option in a live tenant (each option is likely its own AI+ prompt/config) — confirm by checking what values those dimensions actually take when filtering a real workspace, rather than assuming.

Related: [[reply-assistance-ai-plus]], [[smart-compose-reporting]].

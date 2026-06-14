# GROOT Knowledge Base — Index

The master map of what GROOT knows locally. **Check here first** before live sources.

- **Status** `✅` = distilled KB file exists; `🟡` = transcript generated in Stream, KB not yet written; `⬜` = not started.
- **Lookup order:** this KB → `sprinklr.com/help` (`site:sprinklr.com/help <topic>`) → RaptorCX SharePoint videos.

## How the source library is structured (confirmed June 2026)
RaptorCX SharePoint → `Training Material/Sprinklr Trainings/Product Foundation Courses/`. **Reorganized into ~60 per-topic folders.** Each topic folder = a numbered subfolder `NNN_<Topic>` holding the **course video (.mp4)** + a **slide PDF** (`Presentation2*.pdf`). Videos are Microsoft Stream screen-recordings.

**Videos have no captions by default**, but GROOT (Kanishk's account has edit access) **generates transcripts in Stream itself**, then reads them. Full procedure stored in auto-memory `groot-build-state`. This is the real content source — far richer than the slide PDFs. `sprinklr.com/help` cross-checks config specifics.

Top-level `01_Process Foundation.mp4` = overall CCaaS Voice training/process overview (Stages 1–6: S2S kickoff → Discovery/BRW → ACD/Care Console/governance → Voice/IVR → ACW/Reports → Outbound → UAT/Go-live → Empower → Closure).

---

## Care Console
| Topic | Status | KB file |
|---|---|---|
| Care Console Overview | ✅ | care-console/overview.md |
| Care Console Manager | ✅ | care-console/manager.md |
| Case Third pane | ✅ | care-console/case-third-pane.md |
| Case Stream — Filters, SLA, Case Inactivity Timers (035) | ✅ | care-console/case-stream-sla.md |
| Case Control buttons — GP, CFs and macros (036) | ✅ | care-console/case-control-buttons.md |
| Agent Assist — AI features in Care Console (034) | ✅ | care-console/agent-assist-ai.md |
| Shortcuts — Canned Responses & Macros (033) | ✅ | care-console/shortcuts.md |
| Layouts based on channels (037) | ✅ | care-console/layouts-by-channel.md |
| Standard & Custom widgets (040) | ✅ | care-console/widgets.md |
| Iframe Widget (041) | ✅ | care-console/iframe-widget.md |
| Collaboration Notes (038) | ✅ | care-console/collaboration-notes.md |

## Case Management
| Topic | Status | KB file |
|---|---|---|
| Assignment Rules / Assignment Engine (019) | ✅ video | case-management/assignment-rules.md |
| Bot Rule (018) | ✅ | case-management/bot-rule.md |
| Case Creation Logic & Case Maker Rule (016) | ✅ | case-management/case-creation-logic.md |
| Sub-cases / Ticketing (017) | ✅ | case-management/sub-cases.md |
| Survey Rules (020) | ✅ | case-management/survey-rules.md |
| Checking Case Activity & Properties (021) | ✅ | case-management/case-activity-properties.md |
| *(parent folder: Sprinklr Services - Case Management)* | | |

## Guided Workflow (per-topic folders `Guided Workflow - <topic>`; videos 112-120)
| Topic | Status | KB file |
|---|---|---|
| Overview (112) | ✅ | guided-workflow/overview.md |
| Screen Creation (113) | ✅ | guided-workflow/screen-creation.md |
| Input components — variable (114) | ⬜ | guided-workflow/input-components.md |
| API node (115) | ⬜ | guided-workflow/api-node.md |
| Groovy Scripts (116) | ⬜ | guided-workflow/groovy-scripts.md |
| Variables & Resource Manager (117) | ⬜ | guided-workflow/variables-resource-manager.md |
| Records manipulation (118, subfolder "…CreateGetUpdate") | ⬜ | guided-workflow/records-manipulation.md |
| Record Page Basics (119) | ⬜ | guided-workflow/record-page-basics.md |
| Public-facing Guided Workflows (120) | ⬜ | guided-workflow/public-facing.md |

## Conversational AI (15 items) — bot building
| Topic | Status | KB file |
|---|---|---|
| (enumerate subfolder — bot flows, intents, NLU, etc.) | ⬜ | conversational-ai/*.md |

## Community (11 items)
| Topic | Status | KB file |
|---|---|---|
| (enumerate subfolder — community builder, moderation, etc.) | ⬜ | community/*.md |

## Email Care (7 items)
| Topic | Status | KB file |
|---|---|---|
| (enumerate subfolder) | ⬜ | email-care/*.md |

## Live Chat
| Topic | Status | KB file |
|---|---|---|
| User authentication | ⬜ | live-chat/user-authentication.md |
| Specific reporting metrics | ⬜ | live-chat/reporting-metrics.md |
| Rule actions | ⬜ | live-chat/rule-actions.md |
| (+ Basics, Builder, Customisation, Web setup & SDKs, Mobile, Video call & co-browsing, Chat deflection — confirm in folder) | ⬜ | live-chat/*.md |

## Below the fold — to enumerate next session
Unified Routing (routing config, capacity, smart routing, wait times, troubleshooting), Outbound Voice (data ingestion, ACW, post-call workflow, suppression list, retry strategy, skill-based assignment), Sandbox/ALM & Change Management (sandbox features, refresh, inbound/outbound changesets, tiered approvals), Knowledge Base (builder features, community builder). Re-list the Product Foundation Courses folder to capture exact folder names.

---

## Topic-file template
```
# <Topic> (<Module>)
**Source:** Product Foundation Courses → <folder> (video transcript) · **Help:** <sprinklr.com/help URL>
## What it is
## When to use
## Configuration steps
## Common issues & fixes
## Notes / gaps
```

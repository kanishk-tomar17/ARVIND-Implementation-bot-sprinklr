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
| Input components — variable (114) | ✅ | guided-workflow/input-components.md |
| API node (115) | ✅ | guided-workflow/api-node.md |
| Groovy Scripts (116) | ✅ | guided-workflow/groovy-scripts.md |
| Variables & Resource Manager (117) | ✅ | guided-workflow/variables-resource-manager.md |
| Records manipulation (118, subfolder "…CreateGetUpdate") | ✅ | guided-workflow/records-manipulation.md |
| Record Page Basics (119) | ✅ | guided-workflow/record-page-basics.md |
| Public-facing Guided Workflows (120) | ✅ | guided-workflow/public-facing.md |

> **Folder structure confirmed June 2026 (corrected).** Two layouts exist in `Product Foundation Courses/`:
> - **Hyphenated module folders** (e.g. `Guided Workflow - <topic>`, `Care Console - <topic>`) → each contains a numbered subfolder `NNN_<same name>` → `NNN_<same name>.mp4`.
> - **Single-word module folders** (e.g. `Conversational AI`, `Sprinklr Services`) → contain numbered item folders `NNN_<Module> - <topic>` → `NNN_<Module> - <topic>.mp4`.
> The INDEX's earlier "Conversational AI/Community/Email Care item counts" were guesses; the real module list is below.

## Conversational AI (folder: `Conversational AI`; items 096–110)
| Topic | Status | KB file |
|---|---|---|
| Discovery Run (096) | ✅ | conversational-ai/discovery-run.md |
| Intents & Intent creation (097) | ✅ | conversational-ai/intents.md |
| Entities & Entity creation (098) | ✅ | conversational-ai/entities.md |
| Basics of Dialogue Tree (099) | ✅ | conversational-ai/dialogue-tree-basics.md |
| Different Nodes in a Dialogue Tree — Basic (100) | ✅ | conversational-ai/dialogue-nodes-basic.md |
| Different Nodes in a Dialogue Tree — Advanced (101) | ✅ | conversational-ai/dialogue-nodes-advanced.md |
| API Node (102) | ✅ | conversational-ai/api-node.md |
| FAQ Bots (103) | ✅ | conversational-ai/faq-bots.md |
| Bot Rule Setup (105) | ✅ | conversational-ai/bot-rule-setup.md |
| Message Validation & Intent Test Projects (106) | ✅ | conversational-ai/message-validation.md |
| Golden Test Set & Version Control (107) | ✅ | conversational-ai/golden-test-set.md |
| Application Testing (108) | ✅ | conversational-ai/application-testing.md |
| Standard Reporting Dashboard (110) | ✅ | conversational-ai/standard-reporting.md |

## Live Chat (hyphenated folders `Live Chat - <topic>`; 12)
| Topic | Status | KB file |
|---|---|---|
| Basics of Live chat (085) | ✅ | live-chat/basics.md |
| Live Chat Builder (086) | ✅ | live-chat/builder.md |
| Live chat customisation (087) | ✅ | live-chat/customisation.md |
| Live chat web setup and SDKs (091) | ✅ | live-chat/web-setup-sdks.md |
| Live chat mobile implementation (092) | ✅ | live-chat/mobile.md |
| Live chat user authentication (093) | ✅ | live-chat/user-authentication.md |
| Live chat rule actions (089) | ✅ | live-chat/rule-actions.md |
| Live chat specific reporting metrics (090) | ✅ | live-chat/reporting-metrics.md |
| Proactive Prompt Builder and Rule Configuration (095) | ✅ | live-chat/proactive-prompts.md |
| Video call and co-browsing configuration (094) | ✅ | live-chat/video-cobrowsing.md |
| Chat deflection (088) | ✅ | live-chat/chat-deflection.md |

## Unified Routing (hyphenated folders `Unified Routing - <topic>`; 8)
| Topic | Status | KB file |
|---|---|---|
| Routing types (029) | ✅ | unified-routing/routing-types.md |
| Routing configuration (025) | ✅ | unified-routing/routing-configuration.md |
| Capacity configuration (024) | ✅ | unified-routing/capacity-configuration.md |
| Agent Skills and skill groups (023) | ✅ | unified-routing/agent-skills.md |
| Smart routing (028) | ✅ | unified-routing/smart-routing.md |
| Stickiness, capacity, timeout settings (026) | ✅ | unified-routing/stickiness-timeout.md |
| Average wait time / number in queue (027) | ✅ | unified-routing/wait-time-queue.md |
| Troubleshooting Assignment issues (030) | ✅ | unified-routing/troubleshooting-assignment.md |

## Outbound Voice (hyphenated folders `Outbound Voice - <topic>`; 13)
| Topic | Status | KB file |
|---|---|---|
| Voice Campaign Creation (166) | ✅ | outbound-voice/campaign-creation.md |
| Data Ingestion (163) | ✅ | outbound-voice/data-ingestion.md |
| Dialers (Predictive, Preview etc.) (164) | ✅ | outbound-voice/dialers.md |
| Voice Campaigns — Retry Strategy and Dial Plan (165) | ✅ | outbound-voice/retry-strategy.md |
| Voice Campaigns — Suppression List (167) | ✅ | outbound-voice/suppression-list.md |
| Skill based assignment in Voice Campaigns (168) | ✅ | outbound-voice/skill-based-assignment.md |
| Manual Call and Call Controls (170) | ✅ | outbound-voice/manual-call-controls.md |
| Callback (173) | ✅ | outbound-voice/callback.md |
| Agent Desktop (172) | ✅ | outbound-voice/agent-desktop.md |
| ACW (171) | ✅ | outbound-voice/acw.md |
| Post Call Workflow (169) | ✅ | outbound-voice/post-call-workflow.md |
| Reporting (174) | ✅ | outbound-voice/reporting.md |

## Sandbox / ALM (hyphenated folders `Sandbox - <topic>`; 5)
| Topic | Status | KB file |
|---|---|---|
| Sandbox Features (191) | ✅ | sandbox/features.md |
| Sandbox Refresh (192) | ✅ | sandbox/refresh.md |
| Inbound Change sets (193) | 🟡 transcript stuck | sandbox/inbound-changesets.md (193 transcript hung server-side; re-generate next pass) |
| Outbound Change sets (194) | ✅ | sandbox/outbound-changesets.md |
| Application Lifecycle Management and best practices (195) | 🟡 transcript stuck | sandbox/alm-best-practices.md (195 transcript hung server-side; re-generate next pass) |

## Knowledge Base (folders `Knowledge Base - <topic>`; 8 topics — **NO VIDEOS**)
> **Source (confirmed 2026-06-15):** KB topics have **no course video** — numbered subfolders are empty. Content lives in **"KB Microskills - <topic>.pdf"** slide decks. Text-extraction returns only glyphs, but **downloading the PDF + reading it visually** (SharePoint `download.aspx?SourceUrl=…` → local Read) renders the slides as images and works. **7/8 distilled this way.** These are overview decks (concepts + a touchpoint diagram), not deep config — in-platform demos aren't in the slides; flag config specifics for `sprinklr.com/help` / live.

| Topic | Status | KB file |
|---|---|---|
| Enablement of Knowledge Base (124) | ✅ (PDF) | knowledge-base/enablement.md |
| Users, User Groups, Permissions, Personas, Roles (122) | ✅ (PDF) | knowledge-base/users-permissions.md |
| Tiered Approval Workflow (123) | ✅ (PDF) | knowledge-base/tiered-approval.md |
| Community Builder (mapping, article ordering, etc.) (125) | ✅ (PDF) | knowledge-base/community-builder.md |
| Knowledge Base Builder Features (autotranslate, tags, editing, scheduled publish) (126) | ❌ **no source** — folder empty, no PDF/video; needs help.sprinklr / live | knowledge-base/builder-features.md |
| Integration / Consumption & Touchpoints (Smart Assist, Smart Comprehend, AI+, Bot) (128) | ✅ (PDF) | knowledge-base/integration.md |
| Knowledge Base Reporting (dashboard import, visualisations) (130) | ✅ (PDF) | knowledge-base/reporting.md |
| Change Management (Inbound/Outbound Changesets) (131) | ✅ (PDF) | knowledge-base/change-management.md |

## Sprinklr Services (folder: `Sprinklr Services`; Case Management done elsewhere)
| Topic | Status | KB file |
|---|---|---|
| Case Management (016–021) | ✅ | case-management/*.md (done — see Case Management section) |
| Governance | ⬜ | sprinklr-services/governance.md |
| Rule Engine | ⬜ | sprinklr-services/rule-engine.md |

## Other module folders — not yet enumerated (single-word folders)
Each likely holds numbered `NNN_<Module> - <topic>` item folders; enumerate when reached:
- **Community**
- **Email Care**
- **Inbound Voice**
- **Journey Facilitator**
- **Messaging**
- **Quality Management**
- **Reporting**
- **Supervisor Console**
- Top-level `01_Process Foundation.mp4` (CCaaS Voice overview) — still ⬜.

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

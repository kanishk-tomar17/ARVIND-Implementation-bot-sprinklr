# ARVIND Knowledge Base — Index

The master map of what ARVIND knows locally. **Check here first** before live sources.

- **Status** `✅` = distilled KB file exists; `🟡` = transcript generated in Stream, KB not yet written; `⬜` = not started.
- **Lookup order:** this KB → **`sprinklr-map.json` catalog → JIT WebFetch** → `site:sprinklr.com/help` search → RaptorCX SharePoint videos. Run the **`knowledge-lookup`** skill when unsure the local KB covers a fact.

> **Just-In-Time retrieval (since 2026-06-17):** ARVIND no longer bulk-ingests the help center. `knowledge/sprinklr-map.json` is a catalog of **every** help article (one JSON object per line: topic/category/url/keywords/local_kb) — Grep it to find the 1–2 articles a task needs, then WebFetch only those. Regenerate with `knowledge/_help-catalog/build_map.py`. The distilled folders below are the fast "already known" tier; everything else is reached on demand and distilled into the KB as it's used. See the `knowledge-lookup` skill.
>
> **Distilled from the help center so far:** `ai-studio/` (Sprinklr AI, 16) · `social/publishing` (9) · `social/engagement` (4) · `social/reporting` (9) · `social/channels/` big-6 (facebook, instagram, x-twitter, youtube, linkedin, tiktok) + 14 long-tail channels. Everything else (rest of Service/Marketing/Insights/Platform + remaining channels) → JIT via the map.

## How the source library is structured (confirmed June 2026)
RaptorCX SharePoint → `Training Material/Sprinklr Trainings/Product Foundation Courses/`. **Reorganized into ~60 per-topic folders.** Each topic folder = a numbered subfolder `NNN_<Topic>` holding the **course video (.mp4)** + a **slide PDF** (`Presentation2*.pdf`). Videos are Microsoft Stream screen-recordings.

**Videos have no captions by default**, but ARVIND (Kanishk's account has edit access) **generates transcripts in Stream itself**, then reads them. Full procedure stored in auto-memory `groot-build-state`. This is the real content source — far richer than the slide PDFs. `sprinklr.com/help` cross-checks config specifics.

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

## Unified Routing (hyphenated folders `Unified Routing - <topic>`; 11)
| Topic | Status | KB file |
|---|---|---|
| **Overview — app map / 6 tabs** (live + help) | ✅ | unified-routing/overview.md |
| Custom Channels (help) | ✅ | unified-routing/custom-channels.md |
| Debug Console — historical wait reasons (help) | ✅ | unified-routing/debug-console.md |
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
| Inbound Change sets (193) | ✅ | sandbox/inbound-changesets.md |
| Outbound Change sets (194) | ✅ | sandbox/outbound-changesets.md |
| Application Lifecycle Management and best practices (195) | ✅ | sandbox/alm-best-practices.md |

## Knowledge Base (folders `Knowledge Base - <topic>`; 8 topics — **NO VIDEOS**)
> **Source (confirmed 2026-06-15):** KB topics have **no course video** — numbered subfolders are empty. Content lives in **"KB Microskills - <topic>.pdf"** slide decks. Text-extraction returns only glyphs, but **downloading the PDF + reading it visually** (SharePoint `download.aspx?SourceUrl=…` → local Read) renders the slides as images and works. **7/8 distilled this way.** These are overview decks (concepts + a touchpoint diagram), not deep config — in-platform demos aren't in the slides; flag config specifics for `sprinklr.com/help` / live.

| Topic | Status | KB file |
|---|---|---|
| Enablement of Knowledge Base (124) | ✅ (PDF) | knowledge-base/enablement.md |
| Users, User Groups, Permissions, Personas, Roles (122) | ✅ (PDF) | knowledge-base/users-permissions.md |
| Tiered Approval Workflow (123) | ✅ (PDF) | knowledge-base/tiered-approval.md |
| Community Builder (mapping, article ordering, etc.) (125) | ✅ (PDF) | knowledge-base/community-builder.md |
| Knowledge Base Builder Features (126) | ✅ (from sprinklr.com/help — no local video) | knowledge-base/builder-features.md |
| Integration / Consumption & Touchpoints (Smart Assist, Smart Comprehend, AI+, Bot) (128) | ✅ (PDF) | knowledge-base/integration.md |
| Knowledge Base Reporting (dashboard import, visualisations) (130) | ✅ (PDF) | knowledge-base/reporting.md |
| Change Management (Inbound/Outbound Changesets) (131) | ✅ (PDF) | knowledge-base/change-management.md |

## Sprinklr Services — Governance (folder `Sprinklr Services - Governance`; 002–008, 7 videos)
| Topic | Status | KB file |
|---|---|---|
| User and User Groups basics (002) | ✅ | governance/users-user-groups.md |
| Roles and permissions (003) | ✅ | governance/roles-permissions.md |
| Accounts & Account Groups (004) | ✅ | governance/accounts-account-groups.md |
| Customer vs Workspace (005) | ✅ | governance/customer-vs-workspace.md |
| Custom Fields (006) | ✅ | governance/custom-fields.md |
| Understanding Macros (007) | ✅ | governance/macros.md |
| Understanding Queues (008) | ✅ | governance/queues.md |

## Sprinklr Services — Rule Engine (folder `Sprinklr Services - Rule Engine`; 009–015, 7 videos)
| Topic | Status | KB file |
|---|---|---|
| Inbound rules (009) | ✅ | rule-engine/inbound-rules.md |
| Rule Batches & Triggers (010) | ✅ | rule-engine/batches-triggers.md |
| Queue Rules (011) | ✅ | rule-engine/queue-rules.md |
| Case update and creation rules (012) | ✅ | rule-engine/case-update-creation.md |
| On demand rules (013) | ✅ | rule-engine/on-demand-rules.md |
| Scheduler Engine (014) | ✅ | rule-engine/scheduler-engine.md |
| LoginLogout rule (015) | ✅ | rule-engine/login-logout-rule.md |

## Sprinklr Services — Case Management (done elsewhere)
| Case Management (016–021) | ✅ | case-management/*.md |

## Community (folder: `Community`; items 180–190; 11)
| Topic | Status | KB file |
|---|---|---|
| Community Builder (180) | ✅ | community/community-builder.md |
| Global and Workspace Roles & Permissions (181) | ✅ | community/global-workspace-roles.md |
| Community-specific Message-level Rules (182) | ✅ | community/message-level-rules.md |
| Live Chat on Community (183) | ✅ | community/live-chat-on-community.md |
| Guided Workflow on Community (184) | ✅ | community/guided-workflow-on-community.md |
| Spam Model (185) | ✅ | community/spam-model.md |
| Case Management for Community (186) | ✅ | community/case-management-for-community.md |
| Social/Single Sign-Ons (187) | ✅ | community/social-sso.md |
| Survey on Community (188) | ✅ | community/survey-on-community.md |
| Support Ticket / Support Cases (189) | ✅ | community/support-ticket.md |
| Community Reporting (190) | ✅ | community/community-reporting.md |

## Email Care (folder: `Email Care`; topics 132–138; 7 — topic folders may hold multiple `_videoN.mp4` parts)
| Topic | Status | KB file |
|---|---|---|
| Account types and addition process (132, 3 parts) | ✅ | email-care/account-types.md |
| Webforms — External Guided Workflows (133) | ✅ | email-care/webforms-external-gw.md |
| Email signature setup (134) | ✅ | email-care/email-signature.md |
| Email collaboration — Forward as email (135) | ✅ | email-care/email-collaboration.md |
| Manual case creation + Merge case setup (136) | ✅ | email-care/manual-case-merge.md |
| Ignore duplicate & auto-response emails (137) | ✅ | email-care/ignore-duplicate-autoresponse.md |
| Email templates (HTML) (138) | ✅ | email-care/email-templates.md |

## IVR (folder: `IVR`; topics 146–151 + verified builder; 7)
| Topic | Status | KB file |
|---|---|---|
| IVR flow builder — manager, create flow & full 52-node catalog | ✅ VERIFIED live (prod8, 2026-06-18) | ivr/flow-builder.md |
| IVR communication nodes (146) | ✅ | ivr/communication-nodes.md |
| IVR disconnect journey (147) | ✅ | ivr/disconnect-journey.md |
| IVR transaction and its reporting (148) | ✅ | ivr/transaction-reporting.md |
| API integration in IVR (149) | ✅ | ivr/api-integration.md |
| System nodes in IVR (150) | ✅ | ivr/system-nodes.md |
| PCI input in IVR (151) | ✅ (slide; transcript pending) | ivr/pci-input.md |

## Inbound Voice (folder: `Inbound Voice`; topics 153–162; 10)
| Topic | Status | KB file |
|---|---|---|
| Telephony Integration (153) — + verified Voice Settings hub / Voice Application (4-tab) / Voice Account | ✅ VERIFIED live (prod8, 2026-06-18) | inbound-voice/telephony-integration.md |
| Voice connectivity (154) | ✅ | inbound-voice/voice-connectivity.md |
| Custom fields (155) | ✅ | inbound-voice/custom-fields.md |
| IVR (156) | ✅ | inbound-voice/ivr.md |
| Persona (157) | ✅ | inbound-voice/persona.md |
| Care console (158) | ✅ | inbound-voice/care-console.md |
| Guided Workflows (159) | ✅ | inbound-voice/guided-workflows.md |
| Call controls (160) | ✅ | inbound-voice/call-controls.md |
| Disposition plan (161) — + verified 3-step builder (Settings/Autowrap/Share) + Edit Fields | ✅ VERIFIED live (prod8, 2026-06-18) | inbound-voice/disposition-plan.md |
| ACW builder (162) — + verified ACW Manager, settings form & node palette | ✅ VERIFIED live (prod8, 2026-06-18) | inbound-voice/acw-builder.md |

## Journey Facilitator (folder: `Journey Facilitator`; topics 139–145; 7)
| Topic | Status | KB file |
|---|---|---|
| Audience Profile import (139) | ✅ | journey-facilitator/audience-profile-import.md |
| Segment Manager (140) | ✅ | journey-facilitator/segment-manager.md |
| Campaigns (141) | ✅ | journey-facilitator/campaigns.md |
| Basics of Journey Builder (142) | ✅ | journey-facilitator/journey-builder-basics.md |
| Different nodes in a Journey Builder (143) | ✅ | journey-facilitator/journey-nodes.md |
| Channels Supported (144) | ✅ | journey-facilitator/channels-supported.md |
| Journey Reporting (145) | ✅ | journey-facilitator/journey-reporting.md |

## Messaging (folder: `Messaging`; topics 052–060; 9)
| Topic | Status | KB file |
|---|---|---|
| Messaging Channels Overview (052) | ✅ | messaging/channels-overview.md |
| WhatsApp Account Addition (053) | ✅ | messaging/whatsapp-account-addition.md |
| Facebook Account Addition (054) | ✅ | messaging/facebook-account-addition.md |
| Apple Messages for Business Account Addition (055) | ✅ | messaging/apple-messages-account-addition.md |
| Google Business Messaging Account Addition (056) | ✅ | messaging/google-business-messaging-account-addition.md |
| WhatsApp Supported Templates (057) | ✅ | messaging/whatsapp-templates.md |
| Facebook Supported Templates (058) | ✅ | messaging/facebook-templates.md |
| Apple Messages for Business Supported Templates (059) | ✅ | messaging/apple-messages-templates.md |
| Google Business Messaging Supported Templates (060) | ✅ | messaging/google-business-messaging-templates.md |

## Quality Management (folder: `Quality Management`; topics 175–179; 5)
| Topic | Status | KB file |
|---|---|---|
| Quality Monitoring / Audit Checklist (175) | ✅ | quality-management/audit-checklist.md |
| AI Scoring / Automated QM (176) | ✅ | quality-management/ai-scoring.md |
| Agent Appeals Process (177) | ✅ | quality-management/agent-appeals-process.md |
| Calibration (178) | ✅ | quality-management/calibration.md |
| Case Sampling via Rule Engine (179) | ✅ | quality-management/case-sampling-rule-engine.md |

## Reporting (folder: `Reporting`; topics 061–084; 24)
| Topic | Status | KB file |
|---|---|---|
| Organising & Creating Dashboards (061) | ✅ | reporting/organising-creating-dashboards.md |
| Dashboard Feature Overview (062) | ✅ | reporting/dashboard-feature-overview.md |
| Creation of a Widget (063) | ✅ | reporting/creating-widget.md |
| Filtering (064) | ✅ | reporting/filtering.md |
| Custom Metrics (065) | ✅ | reporting/custom-metrics.md |
| Export & Schedule Export (066) | ✅ | reporting/export-schedule-export.md |
| Reporting Backend Structure — Digital (067) | ✅ | reporting/backend-structure-digital.md |
| Most Common Metrics & Dimensions (068) | ✅ | reporting/common-metrics-dimensions.md |
| Live Reporting — Digital (069) | ✅ | reporting/live-reporting-digital.md |
| Agent Performance — Macro/Availability/Occupancy (070) | ✅ | reporting/agent-performance-digital.md |
| Volume & SLA (071) | ✅ | reporting/volume-sla.md |
| Survey Reports (072) | ✅ | reporting/survey-reports.md |
| Other Modules — KB/GW/Smart Response (073) | ✅ | reporting/other-modules-reporting.md |
| Voice Reporting Backend Structure (074) | ✅ | reporting/voice-backend-structure.md |
| Live Reporting — Voice / Queue Monitoring (075) | ✅ | reporting/live-reporting-voice.md |
| Inbound Voice — IVR Reporting (076) | ✅ | reporting/inbound-voice-ivr.md |
| Inbound Voice — Agent Performance (077) | ✅ | reporting/inbound-voice-agent-performance.md |
| Inbound Voice — Queue Report (078) | ✅ | reporting/inbound-voice-queue-report.md |
| Outbound Voice — Overall (079) | ✅ | reporting/outbound-voice-overall.md |
| Outbound Voice — Campaign Management (080) | ✅ | reporting/outbound-voice-campaign-management.md |
| Outbound Voice — Agent Performance (081) | ✅ | reporting/outbound-voice-agent-performance.md |
| Outbound Voice — Scheduled Callback (082) | ✅ | reporting/outbound-voice-schedule-callback.md |
| Outbound Voice — Ingestion Report (083) | ✅ | reporting/outbound-voice-ingestion-report.md |
| Common Errors & Troubleshooting — Voice (084) | ✅ | reporting/voice-troubleshooting.md |

## Supervisor Console (folder: `Supervisor Console`; topics 042–050; 9)
| Topic | Status | KB file |
|---|---|---|
| Home Page Features (042) | ✅ | supervisor-console/home-page-features.md |
| Agent Monitoring Features (043) | ✅ | supervisor-console/agent-monitoring.md |
| Queue Monitoring Features (044) | ✅ | supervisor-console/queue-monitoring.md |
| Callback Monitoring Features (045) | ✅ | supervisor-console/callback-monitoring.md |
| Campaign Monitoring Features (046) | ✅ | supervisor-console/campaign-monitoring.md |
| Announcement Features (047) | ✅ | supervisor-console/announcement.md |
| Peer to Peer Chat Features (048) | ✅ | supervisor-console/peer-to-peer-chat.md |
| Supervisor Console Best Practices (049) | ✅ | supervisor-console/best-practices.md |
| Persona Builder (050) | ✅ | supervisor-console/persona-builder.md |

## Asset Manager (Digital Asset Manager) — VERIFIED live prod8 (no course video)
| Topic | Status | KB file |
|---|---|---|
| Asset Manager overview (DAM): views, Create Asset taxonomy (+ Templates/Advertising/Advanced Options sub-menus), filters, approval, folders | ✅ live | asset-manager/overview.md |

## Loose ends
- Top-level `01_Process Foundation.mp4` (CCaaS implementation lifecycle + docs) — ✅ `process-foundation.md`.
- **IVR 151 PCI input** — ✅ re-scraped from full transcript + Gather Customer's Response demo (`ivr/pci-input.md` enriched).
- **KB 126 Builder Features** — ✅ written from **sprinklr.com/help** (no local video/PDF existed); re-ingest if a source video surfaces.

## INGESTION COMPLETE (2026-06-15)
Every Product Foundation Course module has been ingested from Stream transcripts with transcript-aligned screenshots, distilled to KB files, and committed/pushed to branch `knowledge-ingestion-2026-06`. The one topic without a local source (KB 126 Builder Features) was filled from sprinklr.com/help. **No gaps remaining.**

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

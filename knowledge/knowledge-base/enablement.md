# Enablement of Knowledge Base (KB 124)
**Source:** Product Foundation Courses → Knowledge Base - Enablement of Knowledge Base → **"KB Microskills - Enablement" PDF** (no course video exists for this module; the numbered video subfolder is empty) · **Help:** search `site:sprinklr.com/help knowledge base enablement`

> **Note:** The Knowledge Base module ships as **"KB Microskills" slide PDFs**, not videos. Most are image-only; this Enablement deck is the one with extractable detail. Treat config specifics below as a partial extract — confirm against `sprinklr.com/help` or the live platform.

## What it is
Enabling Knowledge Base for a partner is a **back-end enablement** done per environment/cluster. It involves checking KB status, enabling KB for the partner, and setting up **Intuition Feedback** (the Elasticsearch backing for KB).

## Enablement steps (per partner)
For the partner's environment, the support/ops side performs:
1. **Check Knowledge Base Enablement Status.**
2. **Enable Knowledge Base for Partner.**
3. **Intuition Feedback ES Setup** — configure the Elasticsearch (ES) server. Done via a REST client with parameters:
   - `partnerId`
   - `ES_SERVER_TYPE = INTUITION_FEEDBACK`
   - `clusterName` = the ES cluster for that environment (see table)

## Environment → RED URL → ES cluster reference
Each Sprinklr environment sits on a cloud with its own RED admin URL and KB/Intuition ES cluster:

| Env | Cloud | RED URL | Type | KB Intuition ES cluster |
|---|---|---|---|---|
| prod | AWS | https://prod-red.sprinklr.com | Production | pz-reporting1-es7 |
| prod2 | Azure | https://prod2-red.sprinklr.com | Production | care-misc-es7 |
| prod3 | Azure | https://prod3-red.sprinklr.com | Production | care-misc-es7 |
| prod4 | AWS | https://prod4-red.sprinklr.com | Production | care-misc-es7 |
| prod6 | AWS | https://red.prod6.spr-ops.com | Production FedRAMP | — |
| prod8 | GCP | https://red.prod8.spr-ops.com | Production | ss-core1-es7 |
| prod11 | AWS | https://prod11-red.sprinklr.com | Production | core1-es7 |
| prod12 | AWS | https://red.prod12.spr-ops.com | Self Serve / Production | core19-es7 |
| prod15 | AWS | https://red.prod15.spr-ops.com | Production | core1-es7 |
| qa4 | AWS | https://qa4-red.sprinklr.com | QA | — |
| qa5 | GCP | https://red.qa5.spr-ops.com | QA | — |
| prod0 | AWS | https://prod0-red.sprinklr.com | Pre-production | (Intuition Feedback ES setup) |
| azrqa | Azure | https://azrqa-red.sprinklr.com | Pre-production | — |

## Notes / gaps
- **RED** = the back-end admin console used to check/enable KB and run the ES setup REST calls per partner.
- **Intuition Feedback** is the ES index powering KB search/feedback; the **clusterName** must match the partner's environment (table above).
- Source is a slide PDF, not a video — steps are summarised; the exact REST payloads/screens are on the slides as images. Verify on `sprinklr.com/help` / live RED before using in a client environment.
- Related KB topics (mostly image-only PDFs, not yet ingestible): [[users-permissions]], [[tiered-approval]], [[community-builder]], [[integration]], [[reporting]], [[change-management]].

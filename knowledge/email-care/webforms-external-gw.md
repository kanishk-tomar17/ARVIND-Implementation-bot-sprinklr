# Webforms — External Guided Workflows (Email Care 133)
**Source:** Product Foundation Courses → Email Care / 133 Webforms - External Guided Workflows (video transcript + demo) · **Help:** search `site:sprinklr.com/help webform external guided workflow application manager`

## What it is
A **webform** built from an **(external) Guided Workflow** — a public form the brand embeds on their website so users can **report an issue** (which creates a case in Sprinklr). A Guided Workflow is an automation tool that collects inputs and performs actions per a predefined business flow.

## Four steps to build a webform
1. **User experience** (the GW flow), 2. **UI** (screen + fields), 3. **Back-end** (create case, etc.), 4. **Web form URL** for the client to integrate on their site.

## Create the webform screen (Guided Workflow)
1. **Launchpad → Agent Augmentation → Guided Workflows** → **Add** (top-right) → enter name → **Save**.
2. **Add Element → Screen**: set **Title bar text** (the webform title, e.g. "Report an issue").
3. **Add components** (field types — each collects a specific input):
   - **Email Input** (label e.g. "Email ID"), **Phone** (label "Mobile number", set **default country code**), **Text Input** (label e.g. "Issue"), etc.
   - **Mark field as mandatory** → user can't submit without it (else error).
4. **Add background actions** via **Add Element**: **Create Case, Update Property, Schedule Callback**, decision boxes, etc. (the back-end process).
5. **Save** → **Save and Deploy** (deploys the GW).

## Generate the webform URL
1. After deploy, copy the **6-digit code in the URL** = the **Guided Workflow ID** (keep handy as `gwid`).
2. Go to the **Application Manager**: there's no direct link — in the URL, put **`application-`** before **`manager`** (i.e. navigate to the GW application manager).
3. **Create a new application** there to generate the **web form ID / URL**, which the client integrates into their website.

## Notes / gaps
- Same Guided Workflow engine as [[guided-workflow-on-community]] / GW module ([[overview]], [[public-facing]]) — here used as an **external/public webform** that creates Email Care cases. Transcript cut just as application creation began; the application-manager step mirrors the community Application-ID flow.
- Part of Email Care: [[account-types]], [[email-signature]], [[email-collaboration]], [[manual-case-merge]], [[ignore-duplicate-autoresponse]], [[email-templates]].

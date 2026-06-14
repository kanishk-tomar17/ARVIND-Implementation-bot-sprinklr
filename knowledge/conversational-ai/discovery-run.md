# Discovery Run (Conversational AI 096)
**Source:** Product Foundation Courses → Conversational AI / 096 Discovery Run (video transcript + slide) · **Help:** search `site:sprinklr.com/help conversational AI discovery run intent clustering`

## What it is
**Discovery Run** identifies **contact reasons** by analysing conversation data with **unsupervised clustering**. AI scans historical customer conversations, groups them into **clusters and sub-clusters**, and you build an **intent model** on top. Analysis is based on **customer lexicons** — no manual guesswork — so bot strategy is data-driven.
- Net effect: improves efficiency/automation by surfacing what customers actually contact about.

## Why it matters
- **Day-zero problem:** a brand building a conversational AI bot doesn't know *which workflows to build first*. Discovery Run identifies the contact reasons → tells you which intents/workflows to create.
- **Post-go-live:** run it on conversations where the **bot failed to resolve** → find new workflows to add **and** feed signals back to the AI model → **higher AI accuracy** over time.

## How to trigger a Discovery Run
1. **Sprinklr Service → Conversational AI → Manage → Discovery Run.**
2. Choose the **data source**:
   - **Existing messages in Sprinklr** (historical conversations), or
   - **Excel upload** of data from external systems (download the template, paste your data dump, upload).
   - (Newer capability: it can also **recommend new workflows**, not just contact reasons.)
3. For a Sprinklr-data run, fill the form:
   - **Name** the run.
   - **Language** to analyse on.
   - **Time range.**
   - **Filters:** analyse **customer** conversations (not brand-initiated); a **relevant account**; only **engageable** messages.
   - **Seed clustering (optional):** set the **granularity level** and provide example clusters if you already know some.
     - **Higher granularity → smaller, more specific clusters**; lower granularity → broader clusters.

## Analysing the results
- Output is **clusters + sub-clusters** (demo: "Ordering – general issues" top, then "Delivery issues" → sub-clusters "general queries" and "tracking issues"). Shown as a **bubble view** and a **list view**.
- **Create intents** from the **list view** on top of a cluster: select **language**, select a **model** from the data, **name** the intent.
- You can also **merge a cluster** into another from this screen.

## Customer story (from the video)
A brand imported historical Sprinklr conversations *before* starting their bot build, ran Discovery, found top issues (e.g. **warranty**, with sub-clusters), went to list view, **created new intents**, and **trained a model** on them — devising their bot strategy from real data.

## Notes / gaps
- This is the **first step** of a Conversational AI build — feeds [[intents]] (097) and the bot/[[dialogue-tree-basics]] that follow.
- Two-phase value: pre-launch (what to build) and post-launch (what the bot is missing + accuracy feedback).
- Granularity is the main tuning knob — too high fragments intents, too low merges distinct reasons.

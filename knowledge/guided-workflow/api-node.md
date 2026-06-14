# API Node (GW 115)
**Source:** Product Foundation Courses → Guided Workflow - API node (115, video transcript) · **Help:** search `site:sprinklr.com/help guided workflow API node extension`

## What it is
An **API node** lets a guided workflow talk to **external systems** — to fetch data from them or perform actions on them.
- An API is a set of rules/protocols that lets different software applications communicate.
- Typical uses: integrate an external **CRM**, **fetch a customer's data** from the client's data source, or **update the client's database**.

## How it works in Sprinklr (important)
- The **integration team creates "extensions"** that actually call the API.
- Inside the guided workflow you **call the extension** via the API node — the extension in turn calls the real API.
- So you don't configure raw endpoints in the GW; you pick a pre-built **extension**.

## Why an API node is used (per the deck)
1. **Retrieving data from external sources.**
2. **Updating the external database.**

## Configuration steps
1. In the Guided Workflow builder, click the **plus (+) icon → search "Add API node"** → add it.
2. **Name the node.**
3. **Select the API** — open the dropdown and pick the **extension** you want to call.
4. On selecting the extension, **all available inputs for that extension auto-populate** in the node.
5. For each input, enter the **value to send to the API** (right side of the input variable):
   - These values are usually **already captured by the agent on a previous screen**.
   - Fetch them with the **resource selector / resource picker** option (e.g. pass `first name` and `last name` captured earlier).
6. **Output variable mapping:** map the values **returned by the API** to variables you can use later in the workflow (demo stored the output in a variable named `response`).
7. **Full / raw response (optional):** the field *"enter any name for full API response variable"* stores the complete **unmodified** response sent by the client system. Name a variable here to keep the raw response.

## Notes / gaps
- Inputs come *into* the node from earlier screen variables; outputs go *out* to variables for later screens — this is the bridge between agent-entered data and external systems.
- The full/raw response variable is useful when you need to post-process with **Groovy** (see GW 116) because the structured output mapping isn't enough.
- API node is what powers the "by API" option source seen in dynamic [[input-components]] (GW 114).

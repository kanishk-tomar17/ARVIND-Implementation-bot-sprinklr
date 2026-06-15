# Different Nodes in Journey Builder (Journey Facilitator 143)
**Source:** Product Foundation Courses → Journey Facilitator / 143 Different nodes in a Journey Builder (video transcript + demo; Journey Builder canvas screenshot) · **Help:** search `site:sprinklr.com/help journey builder nodes send message decision box`

## What it is
The **Journey Builder canvas** is where you assemble a journey from **nodes**. Key node families: **Manage Record, Utility, Send Message, Decision Box, Set Field/Set Action**. A journey starts at a **Start** node and ends at an **End Event** node.

## Manage Record nodes
Create, fetch, and update **entities** in the Sprinklr database. Three node types: **Create Record, Load (Get) Record, Update Record**.
- **Entity types:** **System** (created from backend), **Standard** (common across all partners — cases, profiles, messages), **Custom** (built to a client's requirement).
- **Create Record (demo — create a case):**
  1. Select the **entity** to create (e.g. Case).
  2. **Name** the node (e.g. "Create New Case").
  3. Set **fields** — e.g. *From Social Network* + *From Social Network User ID* (Email/SMS/WhatsApp/etc.), the recipient's email ID, and any others.
  4. Give the case a **variable name** (lets you reference it in later decision-making).
  5. **Save.**
- **Get / Update Record** behave similarly — retrieve or update entries in the DB.

## Utility nodes
Manipulate/transform data, perform calculations, and other utility tasks:
- **Go To node** — connect two nodes; in the path select Go To and choose the target node to redirect the workflow (e.g. route back to an earlier node).
- **Add Comment node** — add comments at **message / profile / case** level: name, select asset, write the comment, Save.
- **Add Delay node** — insert a predefined time interval between two actions (e.g. 4-hour gap between two messages): pick the time unit and duration, Save.
- **End Event node** — ends the journey at that point.

## Send Message nodes
Send notifications/alerts/messages across channels:
- Add via the **+** icon → search **Send Message** (or scroll the list).
- In the pop-up: **Add from DAM** tab → select the message → **Next** → select the **app account** to send from.
- Optionally **set/copy Outbound Custom Fields** — **Add New Field** (set value) or **Copy Fields** (copy).
- **Preview:** click the message in the journey → **Show Preview** (right options box) to see how it reaches the recipient; can also delete from here.
- **Send Resolve node** — schedule a message at a specific time: select channel, sending account, recipient's social-network user ID, the **time in epoch format**, and configure the channel-appropriate text.

## Decision Box & Set Field nodes
- **Decision Box** — conditional logic / branching. Name each path, define logical **conditions / condition groups**, add to workflow. A **default path** is followed if none of the conditions are met.
- **Set Field / Set Action** — set values/actions within the flow.

## Save / deploy
Canvas footer: **Close**, **Save as Draft**, **Save & Deploy**.

## Notes / gaps
- The canvas is reached after the [[journey-builder-basics]] details page; messages tie to channels in [[channels-supported]]; entities/custom fields link to [[custom-fields]].
- Part of Journey Facilitator: [[audience-profile-import]], [[segment-manager]], [[campaigns]], [[journey-builder-basics]], [[channels-supported]], [[journey-reporting]].

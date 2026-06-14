# Public-facing (Customer-facing) Guided Workflows (GW 120)
**Source:** Product Foundation Courses → Guided Workflow - Public facing Guided Workflows (120, video transcript) · **Help:** search `site:sprinklr.com/help customer facing guided workflow application manager`

## What it is
A **customer-facing guided workflow** is an interactive, step-by-step interface that lets a **customer independently resolve their own issue**. It can be embedded into:
- the client's **website**,
- **Sprinklr Community**, or
- **Knowledge Base articles**.

## Key functionalities
- **Customizable styling** — embed in external systems (brand website, mobile app, community) and **personalize design elements** to match the brand's visual identity.
- **Case creation** — prompts the customer for relevant info (contact details, order number, issue details); on submit, a **case is created in Sprinklr** storing all details.
- **Website embedding** — step-by-step self-service on the brand's site.
- **Real-time API calls** — retrieve information from the client's applications (e.g. **CRM**) live.

## Use cases
- **Web forms** on brand websites — complaint form, registration form, order form, etc. — to streamline data collection.
- **Self-help / troubleshooting tools** — customers fix issues without contacting a care center.

## Configuration — two parts
1. **Create the guided workflow** — identical to an agent-facing GW (see [[overview]], [[screen-creation]]). No difference in build.
2. **Map the GW to an application:**
   1. In the URL bar, append **`care/Guided-Workflow-Application-Manager`** (Care → Guided Workflow Application Manager).
   2. Click **Add Application**.
   3. Give it a **name**, **enable** it, and **select the guided workflow** to map.
   4. **Theme details** — the **CSS** (currently written by the back-end team) that styles the GW to the brand's requirement.
   5. **Save.**

## IDs
- An external/customer-facing GW has both an **Application ID** (found in the Application Manager) and a **Guided Workflow ID** (fetched from the end of the GW's URL — see [[record-page-basics]]).

## Notes / gaps
- Build once, surface two ways: the same GW build serves agent-facing (via record-page widget/button) and customer-facing (via Application Manager mapping).
- Brand-specific **styling/CSS is currently a back-end-team task** in theme details — flag this dependency when scoping a customer-facing rollout.
- Real-time API calls + case creation make these viable as full web forms and self-service deflection tools, not just info pages.

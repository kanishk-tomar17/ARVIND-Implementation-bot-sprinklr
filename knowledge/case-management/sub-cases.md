# Case Management — Sub-cases (Ticketing system)

**Source:** Product Foundation Courses → `Sprinklr Services - Case Management / 017_… Sub-cases` (video transcript) · **Cross-check:** `site:sprinklr.com/help sub-cases ticketing`

A **ticketing** setup: a customer-facing **case** spawns back-end **tickets (sub-cases)** so specialist teams resolve parts of the issue without talking to the customer.

## Why
- Handle customer conversations across all channels (voice, email, WhatsApp, live chat, social, SMS) on one platform.
- Separate **front-ending** (customer care team, talks to customer) from **back-end teams** (e.g. refunds, supply chain — don't talk to the customer). An **intermediary team** collects extra info from the customer when a back-end team needs it (e.g. bank details for a refund).

## End-to-end flow (from the Lucid diagram)
1. Customer reaches out → **Case** created via **Case Maker**.
2. **Front-End Assignment rule** assigns the case to the front-end team; agent sees it in Care Console.
3. A **Guided Workflow widget** lets the agent capture the gathered info; on submit, the case moves to a **case queue** and a rule fires.
4. **Two paths:**
   - **First-time issue** → **create a ticket (sub-case)**; copy case info to the ticket.
   - **Existing complaint** → **don't create a duplicate**; update the old ticket (e.g. raise priority, increment a **ticketing touchpoint counter**) — reduces duplicate tickets.
5. **Back-End Pre-Assignment rule** checks if the ticket meets conditions to go to a back-end team → **Back-End Assignment rule** routes the ticket to the **dedicated work queue** (e.g. refund team).
6. When a back-end agent is available, the ticket assigns to them; appears in their Care Console with a **back-end-only Guided Workflow** offering two options:
   - **Resolve & close** → a **closure rule** runs → **survey** triggered.
   - **Send to other department** (e.g. refund → banking team) → that team gets the GW, resolves, and closes.

## Notes / gaps
- From the course video transcript (blueprint env + live demo). Requires Case Maker, assignment rules, guided workflows, and closure/survey rules wired together. Related: `case-management/case-creation-logic.md`, `case-management/assignment-rules.md`, `case-management/survey-rules.md`, `guided-workflow/overview.md`.

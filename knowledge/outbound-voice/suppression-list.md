# Voice Campaigns — Suppression List (Outbound Voice 167)
**Source:** Product Foundation Courses → Outbound Voice / 167 Voice Campaigns – Suppression List (video transcript) · **Help:** search `site:sprinklr.com/help suppression list compliance DNC voice campaign`

## Compliance context
Outbound voice must follow laws (**TCPA, GDPR**, industry-specific like **FDCPA, HIPAA**) to avoid penalties/fines, protect consumers from unwanted calls, and preserve reputation/trust. A **suppression list** is the core compliance tool.

## What it is
A **list of phone numbers that must NOT be contacted** — Do-Not-Call (DNC) requests, people who asked to be removed, or those ineligible for certain calls. If a customer says "don't call me again," add them to the suppression list and they won't be dialed.

- **Benefits:** regulatory compliance (DNC), risk mitigation (exclude opt-outs), better data accuracy, respecting preferences, efficient resource use (focus on likely buyers), reputation + CX.
- **Use cases:** telemarketing/sales (TCPA, national/international DNC), event management (attendee opt-outs), financial services & debt collection (FDCPA), nonprofits (donor opt-outs), healthcare (HIPAA).

## Two list types
- **Standard** — the **default per partner**; name always starts with **"standard"** (e.g. *standard voice suppression list*); **always Evergreen**; initially empty; add contacts **manually or via API** (back-end handled).
- **Custom** — created via the **Create Suppression List** button.

## How numbers get added
- An **agent adds a customer via ACW** when they say "don't call me."
- An **admin attaches the suppression list to the campaign** so those numbers are excluded.

## Creating a suppression list
1. **Create Suppression List** → **name**, description, **expiry time** (no expiry = **Evergreen**).
2. **Add contacts** — manually (name, **phone number with country code**, expiration date) or **import Excel** (sample columns: contact name, phone number, expiration date; blank expiry = Evergreen).
3. **Save.** View / add more / delete (individual or **bulk**).

## Attaching to a campaign
**Campaigns → Create Campaign** (or **Edit Campaign**) → select the **suppression list** → Save.

## Notes / gaps
- **Always include the country code** when adding numbers manually.
- Standard list (API-fed, Evergreen) vs custom list (manual/file) — most DNC integrations feed the **standard** list via API.
- The agent-via-ACW path is how live "remove me" requests get honoured — wire it into [[post-call-workflow]].

# API Integration in IVR (IVR 149)
**Source:** Product Foundation Courses → IVR / 149 API integration in IVR (video transcript + demo; JSON-response screenshot captured) · **Help:** search `site:sprinklr.com/help IVR API node response variable loop node`

## What it is
An **API** lets two systems communicate (request → process → response). In IVR, an **API node** calls an external API mid-call and uses the response for **decisioning** and **setting fields**.

## Prerequisites
1. **Extensions added in the platform** (so the API can be called from IVR) — request these.
2. **Know the request & response structure** — which **input parameters** are mandatory, their **data types**, and the **output (response) structure**.

## Configuring the API node (demo)
- Select the API. Map its **input parameters**:
  - From a **resource** (resource selector): a created resource (e.g. `phone number` in correct format), a **case/profile custom field**, another API's output, etc.
  - Or a **constant** value (e.g. country_code = "FI").
- **Output:** best practice = map the **complete response** into a **response variable** (rename e.g. `IVR response`). Also define an **exception variable** (e.g. `full`) holding the full API response to detect failures.

## Using the response
- **Set custom fields** via simple **Groovy** referencing the JSON path, e.g. `IVR response.contact.first_name` → set a profile custom field; `IVR response.contact.last_name` → another.
- **Decision box** on a response field, e.g. `IVR response.ABC_code == A` → high-priority customer; add paths for **medium** (`MVC_code`), **low**, etc.
- **Always add a default path** (best practice) — if the expected field isn't present, the path won't break.
- Per branch take actions: set **priority = High**, **directly assign case to agent** (high), different behaviour for medium/low.

## API success vs failure paths
The API node has **two outgoing paths: API Success and API Failure**, decided by the **exception parameter**.
- **API Failure = connection broken** between systems (not a data error).
- A **data error** (e.g. phone number in wrong format) still takes the **Success** path but returns an **error field** in the response → branch on that error field separately.

## Complex / nested & array responses
- Nested fields: `IVR response.order.customer_phone_number`, `IVR response.order.header_charge.invoice_charge_amount`, etc.
- **Arrays** (e.g. `order_line` — a dynamic array, varying element count per customer): use a **Loop node** that iterates over the array variable (e.g. loop on `order_line`) to act on each element.

## Notes / gaps
- Mirrors the Guided Workflow / CAI **API node** pattern (map inputs from resources, store response, Groovy to parse, branch). See [[api-node]] (GW), [[api-node]] (CAI), [[groovy-scripts]]. The JSON-response example (customer_id, country_code, abc_code, contact{...}) was captured.
- Part of IVR: [[communication-nodes]], [[disconnect-journey]], [[transaction-reporting]], [[system-nodes]], [[pci-input]].

# API Node (Conversational AI 102)
**Source:** Product Foundation Courses → Conversational AI / 102 API Node (video transcript) · **Help:** search `site:sprinklr.com/help conversational AI API node input output mapping exception timeout`

## The 4-step API lifecycle in Sprinklr
1. **API discovery** — our integration team + the client's integration team scope it.
2. **API configuration** — technical back-and-forth; the **client exposes an external API**.
3. **API extension** is passed into the Sprinklr environment and **tested**.
4. Once onboarded, **consume it via nodes** in a **dialogue tree** or **guided workflow** (this session's focus).

## What bots use APIs for
Integration with external services, **data retrieval**, **authentication**, **real-time updates**, and **database integration**.

## What you configure on the node
- **Input mapping**, **output mapping**, **exception handling**, **timeout handling**.

## Configuring an API node in a dialogue tree
1. Add node → search **API** → select the **API name** (demo: *Order tracking*).
2. **Input mapping:** left = **API inputs**; right = the **variable/parameter to send** (e.g. send the captured `order number`).
3. **Output mapping:** left = **API output value** (e.g. `response`); right = the **variable to store it in** (e.g. `response1`).
4. **Exception variable:** populated whenever an exception occurs — use it to **report errors / debug**.
5. **Full API response variable:** name a variable to capture the **entire** response (vs the one or two mapped output values).
6. **Timeout:** set a threshold (e.g. 5s) — the node waits that long for the API; if exceeded, it **prints a configured message**.

## Using the results
After configuration, the output variables can be used **anywhere in the dialogue tree**: print them in a bot reply, build a variable, write **Groovy** over them, or **pass values into a custom field**.

## Notes / gaps
- Same idea as the GW [[../guided-workflow/api-node]] (extensions, input→send, output→store, full raw response) but inside the bot's dialogue tree, with explicit **exception** and **timeout** variables.
- The actual API/extension must be **onboarded by integration first** — consultants can't point a node at an arbitrary URL.
- Exception + timeout handling are the reliability levers — always set them so the bot degrades gracefully when the external system is slow/down.

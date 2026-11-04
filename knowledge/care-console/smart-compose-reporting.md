# Smart Compose — Reporting

**Source:** https://www.sprinklr.com/help/articles/smart-compose/reporting-on-smart-compose/64886f57723d925979dbca26

## Metrics
- `Compose Count (Smart Compose)` — requests sent by the user for a suggestion
- `Received Count (Smart Compose)` — predictions returned by the AI model
- `Rendered Count (Smart Compose)` — predictions actually shown to the agent
- `Accepted Count (Smart Compose)` — predictions the agent used (funnel: Compose → Received → Rendered → Accepted; **Accepted/Rendered = adoption rate**)

## Dimensions
- Query Phrase (the customer's original message)
- Responses (the AI-generated suggestion)
- Used Response Phrase (the predicted text as used/edited by the agent)

## Business-impact widgets (with-vs-without adoption)
- Average Case Processing SLA, with Smart Compose usage vs. without
- Average Predicted CSAT Score, with vs. without
- Case-wise Case Processing SLA comparison view

Doc doesn't name the exact report/module path — build via the standard Care Reporting widget creator ([[../reporting/creating-widget.md]] pattern) using the metrics/dimensions above.

Related: [[agent-assist-ai]], [[reply-assistance-ai-plus]].

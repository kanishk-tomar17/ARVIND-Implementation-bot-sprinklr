# SLA Monitoring (Sprinklr Social — Reporting)
**Source:** sprinklr.com/help — Reporting sub-area (multiple articles; see links below)

## What it is
- SLA Monitoring tracks how well your team meets response/resolution targets, measured in the **SLA Dashboard** under Sprinklr Social > Reporting (Analyze).
- An **SLA Preset** defines the thresholds and business hours used to calculate SLA performance (e.g. response time objective, compliance target, working hours, inactive/holiday hours).
- Presets can be applied at both **Standard Dashboard** and **Custom Dashboard** levels, and to individual widgets.
- The SLA dashboard is **enabled by default in any partner** — no separate activation needed (contact your Success Manager for details).
- See also: [[reporting]], [[engagement-dashboards]], [[care-console]], [[rule-engine]], [[data-engine]].

## Key features & how to use

### SLA Preset Configuration
- Path: New Tab icon > **Reporting** (Sprinklr Social) > **Dashboard Menu** > select **SLA** > **Filter** icon (top-right) > **SLA: Select SLA** tab > **SLA Preset** > fill the **Apply SLA Configuration** window > **Save & Apply**.
- After saving, hover over a preset to get **Edit** or **Delete** icons.
- Configuration fields:
  - **Name** — label for the SLA configuration.
  - **Preset SLA Configurations** — pick a pre-existing configuration from the dropdown.
  - **Frequency Distribution Ranges** — time ranges used for measurement.
  - **SLA Objective** — the desired response-time threshold.
  - **SLA Compliance Target** — target percentage of messages meeting the objective.
  - **Country** — location for statistics tracking.
  - **Timezone** — timezone for displaying metrics.
  - **Lock SLA** — checkbox to prevent future changes to the preset.
  - **Define Working Hours** — set operational hours via the hour boxes.
  - **Add Inactive Hours** — set non-operational hours.
- For **Custom Dashboards**: click the options icon and select **Set SLA Preset** to apply a preset.

### Add Account in SLA Preset
- Lets you attach specific accounts to an SLA preset; the preset is then applied in reporting based on the **source account** of the message/case for SLA calculation.
- Path: New Tab icon > **Reporting** under Social Core Cloud > **Add Widget** (upper right) > set **Type = Social Analytics** > enter a name, choose Visualization, add dimensions > scroll to **SLA** dropdown > **Add SLA Preset** > in the **Account** section, add accounts > **Save & Apply**.
- You can select **multiple accounts** associated with the preset.
- You no longer need to select a preset while creating SLA Reporting — account-based application handles it.

### Set Holiday Hours in SLA Presets
- Lets you apply inactive hours to **specific calendar dates** (one-off holidays with unique names), rather than annually recurring holidays. Multiple dates supported.
- Path: New Tab icon > **Reporting** (within Analyze, Sprinklr Social) > **Dashboard Menu** (top-left) > **SLA** under Dashboards > **Filter** icon (top-right) > **SLA: Select SLA** tab > **SLA Preset** > **Apply SLA Configuration** window.
- Check the **Add Inactive Hours** box, then select the specific date(s).
  - By default, **All Day** is checked on the Inactive Hours calendar, which excludes the entire chosen date from your SLA.
  - Uncheck **All Day** to select specific hours instead.
- Click **Save & Apply**. Hover over a preset afterward for Edit/Delete icons.
- You can set an **auto-response** to be sent during non-business hours.

### SLA FAQs (quick reference)
- **Enabling the SLA dashboard:** Enabled by default in any partner; contact your Success Manager for activation details.
- **Move a widget to a custom dashboard:** Reporting (Analyze) > select an SLA widget (e.g. "Average Response Time trend over time") > three-dot menu > **Add to Custom Dashboard** > pick target dashboard > confirm.
- **Add SLA preset and filters:** Reporting Home (Analyze) > search the SLA dashboard > Filter icon > **SLA Preset** > complete Apply SLA Configuration (Name, Preset SLA Configuration, SLA Objective, SLA Frequency, Business Hours) > Save & Apply.

## Common issues & fixes
- **Holiday hours not working on mobile:** Setting holiday hours in SLA presets is **not supported on the Sprinklr Mobile App** — configure from web.
- **Preset keeps getting changed:** Use the **Lock SLA** checkbox in the preset to prevent future edits.
- **Whole day wrongly excluded from SLA:** The **All Day** box is checked by default under Inactive Hours; uncheck it to exclude only specific hours of a date.

## Notes & gaps
- Prerequisite/permissions: articles state the SLA dashboard is on by default per partner but do **not** specify user roles/permissions required to create or edit presets.
- Articles do **not** define exact metric formulas (e.g. how Average Response Time or compliance % is calculated), nor allowed value ranges/limits for SLA Objective, Compliance Target, or number of accounts/holiday dates per preset.
- "Frequency Distribution Ranges" and "SLA Frequency" appear across articles but are not fully defined.
- Related ARVIND topics: [[sla-monitoring]], [[reporting]], [[engagement-dashboards]], [[care-console]], [[rule-engine]], [[data-engine]].

## Sources
- SLA Preset Configuration — https://www.sprinklr.com/help/articles/sla-monitoring/sla-preset-configuration/6454ec83f65d86626c82b9c7
- Add Account in SLA Preset — https://www.sprinklr.com/help/articles/sla-monitoring/add-account-in-sla-preset/6454ea24f65d86626c82b9c2
- Set Holiday Hours in SLA Presets — https://www.sprinklr.com/help/articles/sla-monitoring/set-holiday-hours-in-sla-presets/6454e28cf65d86626c82b9b6
- SLA FAQs — https://www.sprinklr.com/help/articles/sla-monitoring/sla-faqs/6454ec810d27fc559bbeb54a

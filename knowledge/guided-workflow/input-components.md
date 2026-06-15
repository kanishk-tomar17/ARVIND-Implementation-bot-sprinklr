# Input Components — Variable / Dynamic Inputs (GW 114)
**Source:** Product Foundation Courses → Guided Workflow - Input components - variable (114, video transcript) · **Help:** search `site:sprinklr.com/help guided workflow radio group picklist dynamic table option source`

## What it is
Three Guided Workflow input components can take their options **dynamically** instead of being typed in by hand:
- **Radio group**
- **Pick list**
- **Dynamic table**

"Variable inputs" = the options shown to the agent are pulled from a **variable** or an **API** at runtime, rather than defined upfront when building the screen.

## When to use
- The option list is **too long** to type manually, OR
- The options aren't known at build time because they **come from an API at runtime** (e.g. product lists, country-dependent brands).
- If you know the full, short, static list upfront → just add options manually (covered in the previous session). Use variable/API only when the list is dynamic.

## Core concept — everything is a key–value pair
Whenever options come from a variable, the data **must be in key–value pairs**:
- **`label`** = the key whose value is **shown to the agent** on screen.
- **`value`** = the key whose value is **stored in the back end**.
- Example: store `A1235` in the back end but display `mobile` to the agent → `label: mobile`, `value: A1235`.

## Configuration steps

### 1. Define the source variable (Update Properties node)
1. On the canvas, **Add element → search "Update Properties" → select the Update Properties node.**
2. Name the variable (demo used `product select set`).
3. Click the **resource picker icon (`$(x)`) → Enter custom code** (a Groovy/JSON editor; "Groovy Library" available) to define the variable.
4. Define it as an **array of key–value pairs**, each entry having a `label` and a `value` key.
   - *On-screen Update Properties dialog:* fields are **Name**, then **"Select/Create Fields to update their values"** with mapping rows of **Select/Create Parameter · Select Operator · Select Value**, plus **Add Another Mapping**.

### 2. Radio group — by variable
1. Add the radio group; **name the API** and write the **label** (the question/content shown).
2. **Option source** → choose **By variable** (other choice is **Manual**).
3. **Choose variable** → click resource picker → search or scroll to pick your variable.
4. Enter the **key to value** and **key to label** (i.e. tell it which key in your pairs is the stored value and which is the displayed label).
5. Save.

### 3. Pick list — by variable OR by API
Name the API and label first. Option source has **three** choices: **Manual**, **By API**, **By variable**.
- **By variable:** same as radio group — choose variable, map key→value and key→label.
- **By API:**
  1. Select the **name of the API** that returns the options.
  2. **Pass inputs** the API needs — add the input names and their values.
  3. The API response **must be key–value pairs**. If it isn't, **adapt the response with a Groovy script** in the provided section.
  4. `value` and `label` mapping work the same as the by-variable option.

### 4. Dynamic table
Option sources: **By variable**, **By API**, **By entity**.
- **By variable:**
  1. Define the variable as **multiple arrays of key–value pairs** (demo variable named `dynamic table`).
  2. Each **key name becomes a column name**; all values under that key fill that column. (Demo keys: `name` and `value`.)
  3. Add the component → by variable is selected by default → search/select the variable.
  4. Enter each **key/column name** (e.g. `name`, then `value`), optionally set the **variable type** per column.
  5. Set the **Primary key** — **mandatory** — then Save.
- **By API:** select the API name → enter required inputs → if response isn't key–value pairs, **adapt the response** (Groovy) via the provided option.

## Verified on agent screen (demo)
- A pick list **dynamically fetches** options from an API; selecting a different **country** changes the **brand** values shown (dependent/cascading lists driven by API).
- A defined **array** renders as a **dynamic table** on the agent screen — keys become columns, associated values populate rows.

## Notes / gaps
- Key–value-pair format is the recurring requirement across all three components and both variable and API sources — get the variable shape right first.
- Groovy "adapt response" is the escape hatch whenever an API doesn't already return clean key–value pairs (ties into GW 116 Groovy Scripts).
- The variable itself is built in an **Update Properties** node via custom code (ties into GW 117 Variables & Resource Manager).

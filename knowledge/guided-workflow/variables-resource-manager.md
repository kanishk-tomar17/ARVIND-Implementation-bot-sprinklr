# Variables & Resource Manager (GW 117)
**Source:** Product Foundation Courses → Guided Workflow - Variables and resource manager (117, video transcript) · **Help:** search `site:sprinklr.com/help guided workflow resource picker manage resources variable`

## What it is
Covers two things:
- **Resource picker** — how to *access* a variable you've already created, on a screen component.
- **Manage Resources** — how to *view, edit, and create* variables (and see other field types).

(Defining a variable itself is covered in [[input-components]] / via the Update Properties node.)

## Accessing a variable with the resource picker
1. On a screen component (e.g. a **description text**), click the **resource picker icon** (`$(x)`).
2. Either **search** for the variable by name, or **scroll the list** and select it.
- This is how you drop a stored variable's value into screen content, inputs, etc.

## Manage Resources
- Click the **Manage resource icon** (top-right of the builder).
- It lists **all variables created**, plus **case-level fields**, **profile-level fields**, and the **custom fields** you've created.
- Click the **three dots** on a resource to **access / edit** it. For a variable you'll see:
  - **Resource type** = Variable
  - **API name** = the variable's name
  - **Data type** = already set
  - **Available for reporting** — toggle ON to make this variable available in **reporting**.
  - **Available for output** / **Available for input** — **being deprecated; skip these** (don't rely on them).

## Creating a new variable from Manage Resources
1. In Manage Resources, choose to **create a new variable**.
2. **Name** the variable.
3. Select the **data type**.
4. Optionally tick **Available for reporting** (if the variable is needed in reports).
5. Click **Create**.

## Notes / gaps
- "Available for reporting" is the one flag that still matters when managing variables — set it if the value must surface in dashboards/reports.
- Resource picker reaches not just GW variables but also case/profile/custom fields — useful when a workflow needs existing record data.
- Ties to [[input-components]] (defining variables), [[api-node]] (output variables), and [[groovy-scripts]] (variables holding Groovy results).

# Dashboard Adaptation Note

## Audience

Community health workers working on a nutrition project who need a
plain-language overview of BMI patterns in the classroom NHANES equity
dataset.

## Dashboard Question

Among adults age 20-80, how does mean BMI vary across NHANES cycles for one
selected income group?

## Control And Visualization

- Control or interaction: `selected_income`, initially set to `"Low Income (<1.3)"`.
  In this static dashboard, the user changes the value and re-renders the file.
- Visualization affected: the bar chart of mean BMI by NHANES cycle, as well
  as the summary table and chart title.
- What changes when the control changes: the selected income group changes;
  the table and bars are recalculated for that group.

## Before And After

| Original text | Revised text | Why the revision helps |
|---|---|---|
| Audience: a public-health analyst preparing a short briefing. | Community health workers working on a nutrition project who need a plain-language overview. | Connects the dashboard to a practical project context and signals that the results should be accessible to a community-facing audience. |
| Among adults age 20-80, how does mean BMI vary across cycles for one selected income group? | The question and age range remain the same. | Preserves the starter's analytic cohort and keeps the question aligned with the unchanged age filter. |
| `selected_income <- "Low Income (<1.3)"` | The default remains `"Low Income (<1.3)"`. | Preserves the starter's default analysis; the existing control can still be changed by the user. |
| A line and points show mean BMI across cycles. | Bars show mean BMI for each cycle. | Makes cycle-by-cycle values easier to compare as separate categories. |
| The starter cautions against causal claims about income and BMI. | The adaptation also states that BMI alone is not a comprehensive measure of nutrition or health and that the dashboard does not evaluate project impact. | Helps prevent the descriptive BMI comparison from being mistaken for a complete nutrition assessment or evidence of project effectiveness. |

## Test Result

Rendered from the repository root with
`quarto render assignments/assignment07-dashboard/submission/dashboard.qmd`.
Rendering completed successfully and created the HTML output for the default
`"Low Income (<1.3)"` selection.

## Confirmation: Analytic Logic

No analytic logic was changed. The age range, default income group, missing
value exclusions, grouping by NHANES cycle, and unweighted mean BMI
calculation match the starter. The audience-facing wording and BMI caveat
clarify interpretation, while changing the line-and-point chart to bars
changes only the presentation.

## Limitation

The summary is descriptive and unweighted. It does not account for NHANES
survey design, support causal claims about income and BMI, or evaluate a
nutrition project's impact. BMI alone is not a comprehensive measure of
nutrition or health.

## Privacy Check

The dashboard displays aggregate mean BMI and counts by cycle, not
row-level records. The accompanying privacy guidance says to avoid
interpreting small counts; no small-cell suppression is applied, so low
counts should be treated cautiously. The limitation states that the results
are unweighted and descriptive, should not be used for causal claims or
project-impact evaluation, and that BMI alone is not a comprehensive measure
of nutrition or health.

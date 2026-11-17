# Before-and-After Changes

| Original text or design | Revised text or design | Why the change helps the audience |
|---|---|---|
| Audience: a public-health analyst preparing a short briefing on descriptive BMI patterns. | Audience: community health workers working on a nutrition project who need a summarized overview of BMI patterns. | Makes the intended users and practical project context explicit, supporting clear, relevant communication. |
| Question: among adults age 20-80, how does mean BMI vary across NHANES cycles for one selected income group? | The question and age range remain the same. | Preserves the starter's analytic cohort and keeps the question aligned with the unchanged age filter. |
| `selected_income <- "Low Income (<1.3)"` | The default remains `"Low Income (<1.3)"`. | Preserves the starter's default income-group subset; the existing control can still be changed to compare another group. |
| A line and points display mean BMI across cycles. | Bars display mean BMI for each cycle. | Makes comparisons between cycle-specific values more direct. The bars show differences, not their causes. |
| The starter cautions against causal interpretation of the descriptive pattern. | The adaptation also says BMI alone is not a comprehensive measure of nutrition or health and that the dashboard does not evaluate project impact. | Helps prevent the audience from treating a BMI summary as a full nutrition assessment or as evidence that a nutrition project worked. |

## Confirmation: Analytic Logic

**No, the analytic logic did not change.** The age range (20-80), default
income-group selection (`"Low Income (<1.3)"`), missing-BMI and missing-cycle
exclusions, grouping by NHANES cycle, and unweighted mean BMI calculation
remain the same as in the starter. The audience-facing wording and added BMI
caveat clarify interpretation, while changing the line-and-point chart to
bars changes only the presentation.
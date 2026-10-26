# Visual Audit Note

## Plot Question

Write the descriptive question the plot answers.
Among records with nonmissing BMI and income group, how did the mean BMI for each income group compare between the first and last NHANES cycles in the data?

## Issues Checked

<!-- AI-EDIT(2026-06-11): SS-035 — worked example row added — needs review -->
The first row is a worked example of the expected shape — replace it with your own issue.

| Issue | Category | Why it matters | Correction |
|It only includes first and last NHANES cycles, then connects those two points|Aggregation/time coverage|The plot cannot show what happened in the intervening cycles.| A connecting line can imply a continous trend between variables which in fact is not the case.| Summarize all available cycles and order them in chrononological order before connecting points.|


## Final Caption
Unweighted mean BMI among records with nonmissing BMI and income group in the first and last NHANES cycles included in this dataset. The line connects the two observed cycle means; it does not show intervening cycles or establish a trend. These are descriptive sample means, not survey-weighted population estimates, and do not imply causation.

Write the final caption with data source, statistic, exclusions, and limitation.

## AI-Use Check
AI was used to help identify possible issues in the plot, and generating suggestions and code for revised plot. Suggestions were verified by checking dataset, variable definitions,NHANES survey-design guidance. 
State what AI helped with and how the code, labels, and claims were verified.

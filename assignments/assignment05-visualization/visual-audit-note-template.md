# Visual Audit Note

## Plot Question
How did age-standardized obesity prevalence among US adults (aged 20 and above)differ across income groups in each NHANES cycle? 

## Issues Checked

|Cycles plotted as equally spaced categories | Design | Time period of March 2012-2020 is about 3 years instead of 2, equal spacing distorts time scale |Adding label to clearly show cycle's timeframe)2017-2020 and note uneven length in caption |

|Single weight column being assumed for all cycles  | Correctness | Using wrong weight creates bias for cycle's estimates |Checked to see that each cycle had correct weight in column  |


| BMI greater than and equal to 30 being used as the definition of obesity | Interpretation | BMI does not fully measure individual body composition, the BMI value itself is based on several factors in relation to body fat (ie age, sex ) |Clearly definining obesity as a screening measure and specifying that obesity is defined by BMI greater than/equal to 30kg/m^2 |

## Final Caption

Data source: NHANES (National Health and Nutrition Examination Survey) from the first to last cycle, includes US adults aged 20 and over with BMI and reported income. 

Statistics: survey-weighted prevalence of obesity (BMI > 30kg), (ages 20-39, 40-59, 60+) with bars showing 95% confidence intervals. 

Exclusions: Participants under 20, those with missing BMI values, or missing income group. 

Limitations: BMI as a standardized value does not fully capture individual body weight, missing values for income may not be random, and could indicate potential flaws from initial data collection. 

## AI-Use Check

Used AI to help generate code for revised plot, checked file to see column names in code chunk match CSV file, checked that colors run from low to high income, and ensured that cycles appear in chronological order. For estimates, compared two cycle's obesity prevalence and checked against NCHS figure
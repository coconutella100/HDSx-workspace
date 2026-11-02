## AI-Use Check
AI was used to load the NHANES equity CSV with relative path from submission/" This was verified by rendering; dim() shows 105,626 rows x 18 columns; "NA" shows missing values. 

Prompted AI to filter to ages 20-80 and count exclusions. Verified by checking that filter uses >= and <=; cohort= 57,137 and raw-excluded = cohort
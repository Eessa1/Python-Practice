import pandas as pd
import numpy as np
from scipy import stats 

df = pd.DataFrame({
    "student": range(1, 13),
    "course":  ["CS","CS","CS","CS","CS","CS","Maths","Maths","Maths","Maths","Maths","Maths"],
    "hours_studied": [5, 8, 6, 10, 7, 9, 4, 6, 5, 8, 3, np.nan],
    "mock_score":    [52, 68, 60, 79, 63, 75, 48, 58, 55, 70, 41, 50],
    "final_score":   [58, 72, 63, 85, 66, 80, 49, 63, 54, 74, 45, 53],
    "passed":        ["no","yes","yes","yes","yes","yes","no","yes","no","yes","no","no"],
})
median = df['hours_studied'].median()
df['hours_studied'] = df["hours_studied"].fillna(median)
mathdf = df[df['course'] == 'Maths']
CSdf = df[df['course'] == 'CS']
contingent_table = pd.crosstab(df['course'],df['passed'])
res = stats.chi2_contingency(contingent_table)
print(res.statistic)
print(res.pvalue)
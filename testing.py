from scipy import stats
import pandas as pd
from sklearn.impute import SimpleImputer

impute = SimpleImputer(strategy= "mean")
df = pd.DataFrame({
    "group":  ["A","A","A","A","A","B","B","B","B","B"],
    "score":  [72, 68, 75, None, 70, 80, 78, 85, 79, 83],
    "passed": ["yes","no","yes","yes","no","yes","yes","yes","yes","no"],
})
group_a = df[df['group'] == 'A']['score']
group_b = df[df['group'] == 'B']['score']
ct = pd.crosstab(df['group'],df['passed'])
print(ct)
chi2, p, dof, expected = stats.chi2_contingency(ct)
print(p)
import pandas as pd 
from scipy import stats

df= pd.DataFrame({"before": [55,62,48,70,65,58,52,67,60,63], "after": [61,66,50,75,64,65,58,72,63,70]})

res = stats.ttest_rel(df['before'],df['after'])
print(res.statistic)
print(res.pvalue)
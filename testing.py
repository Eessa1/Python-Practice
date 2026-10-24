import pandas as pd
import numpy as np
from scipy import stats 

df = pd.DataFrame({
    "old":   [62, 70, 68, 75, 71, 66, 73, 69],
    "new":   [74, 78, 72, 80, 77, 75, 79, 76],
})
res = stats.ttest_ind(df['old'],df['new'])
print(res.statistic)
print(res.pvalue)
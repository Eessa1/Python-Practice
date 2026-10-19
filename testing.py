from scipy import stats

group_a = [23,25,28,30,22,27,26]
group_b = [29,33,34,36,26,30,33]

t_stat, p_value = stats.ttest_ind(group_a,group_b)
print(p_value)
print(t_stat)
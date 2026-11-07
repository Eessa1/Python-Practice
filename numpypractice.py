import pandas as pd 
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
print(df.head())
print(df.describe())
print(df.corr)
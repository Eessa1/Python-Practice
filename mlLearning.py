from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets", filter="data")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

housing_full = load_housing_data()
train_set, test_set = train_test_split(housing_full,test_size=0.2,random_state=42)
print(len(train_set))
print(len(test_set))

housing_full["income_cat"] = pd.cut(housing_full["median_income"], bins = [0.,1.5,3.0,4.5,6.,np.inf], labels = [1,2,3,4,5])
cat_p = housing_full["income_cat"].value_counts().sort_index()
cat_p.plot.bar(rot=0, grid = True)
plt.xlabel ("income categories")
plt.ylabel ("Number of districts")
plt.show()

strat_train_set, strat_test_set = train_test_split(housing_full, test_size=0.2,stratify= housing_full["income_cat"],random_state=42 )
print(strat_test_set["income_cat"].value_counts()/len(strat_test_set))
print(housing_full["income_cat"].value_counts()/len(housing_full))
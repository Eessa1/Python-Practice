from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.plotting import scatter_matrix

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
housing_full["income_cat"] = pd.cut(housing_full["median_income"], bins = [0.,1.5,3.0,4.5,6.,np.inf], labels = [1,2,3,4,5])
strat_train_set, strat_test_set = train_test_split(housing_full, test_size=0.2,stratify= housing_full["income_cat"],random_state=42 )
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1,inplace =True)

housing = strat_train_set.copy()
housing["rooms_per_house"] = housing["total_rooms"] /housing["households"]
housing["bedrooms_ratio"] = housing["total_bedrooms"] /housing["total_rooms"]
housing["people_per_house"] = housing["population"] /housing["households"]
corr_matrix = housing.corr(numeric_only=True)
print(corr_matrix["median_house_value"].sort_values(ascending=False))
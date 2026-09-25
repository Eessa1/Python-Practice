from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.linear_model import LinearRegression
from sklearn.compose import TransformedTargetRegressor
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer,make_column_selector
from sklearn.cluster import KMeans
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.metrics import root_mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

class ClusterSimilarity(BaseEstimator,TransformerMixin):
    def __init__(self,n_clusters = 10, gamma = 1.0, random_state=None):
        self.n_clusters = n_clusters
        self.gamma = gamma
        self.random_state = random_state
    def fit(self,X, y= None, sample_weight = None):
        self.kmeans_ = KMeans(self.n_clusters,random_state= self.random_state)
        self.kmeans_.fit(X, sample_weight= sample_weight)
        return self
    def transform(self,X):
        return rbf_kernel(X,self.kmeans_.cluster_centers_,gamma=self.gamma)
    def get_feature_names_out(self,names= None):
        return [f"Cluster {i} similarity" for i in range(self.n_clusters)]
def column_ratio(X):
    return X[:,[0]] / X[:,[1]]
def ratio_name(function_transformer, feature_names_in):
    return ["ratio"]
def ratio_pipeline():
    return make_pipeline(SimpleImputer(strategy= "median"),FunctionTransformer(column_ratio,feature_names_out=ratio_name),StandardScaler())
log_pipeline = make_pipeline(SimpleImputer(strategy="median"),FunctionTransformer(np.log,feature_names_out="one-to-one"),StandardScaler())
cat_pipeline = make_pipeline(SimpleImputer(strategy="most_frequent"),OneHotEncoder(handle_unknown="ignore"))
cluster_simil = ClusterSimilarity(n_clusters= 10, gamma = 1, random_state=42)
default_num_pipeline = make_pipeline(SimpleImputer(strategy="median"),StandardScaler())
preprocessing = ColumnTransformer([("bedrooms", ratio_pipeline(), ["total_bedrooms","total_rooms"]), ("rooms_per_house", ratio_pipeline(), ["total_rooms","households"]),
("people_per_house", ratio_pipeline(), ["population",
"households"]),
 ("log", log_pipeline, ["total_bedrooms", "total_rooms",
"population",
 "households", "median_income"]),
 ("geo", cluster_simil, ["latitude", "longitude"]),
 ("cat", cat_pipeline, make_column_selector(dtype_include=object)),],remainder=default_num_pipeline)
log_transformer = FunctionTransformer(np.log,inverse_func=np.exp)
target_scaler = StandardScaler()
std_scaler = StandardScaler()
cat_encoder = OneHotEncoder()
imputer = SimpleImputer(strategy="median")
num_pipeline = Pipeline([("impute", SimpleImputer(strategy="median")),("standardize", StandardScaler())])
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

housing = strat_train_set.drop("median_house_value", axis = 1)
housing_labels = strat_train_set["median_house_value"].copy()
housing_num = housing.select_dtypes(include=[np.number])
imputer.fit(housing_num)
X = imputer.transform(housing_num)
housing_cat = housing[["ocean_proximity"]]
housing_cat_1hot = cat_encoder.fit_transform(housing_cat)
housing_num_std_scaled = std_scaler.fit_transform(housing_num)
age_simil_35= rbf_kernel(housing[["housing_median_age"]],[[35]],gamma=0.1)
model = TransformedTargetRegressor(LinearRegression(),transformer=StandardScaler())
model.fit(housing[["median_income"]],housing_labels)
data = housing[["median_income"]].iloc[:5]
predictions = model.predict(data)
log_pop = log_transformer.transform(housing[["population"]])
similarities = cluster_simil.fit_transform(housing[["latitude","longitude"]],sample_weight=housing_labels)
forest_reg = make_pipeline(preprocessing,RandomForestRegressor(random_state=42))
forest_rmse = -cross_val_score(forest_reg,housing,housing_labels,scoring="neg_root_mean_squared_error",cv=10)
print(pd.Series(forest_rmse).describe())
print("hi")

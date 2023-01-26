import pandas as pd
import bentoml
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

data = pd.read_csv("cs-training.csv", index_col=0)
rf_pipe = Pipeline([("imputer", SimpleImputer()), ("model", RandomForestClassifier())])
rf_pipe.fit(data.iloc[:, 1:].values, data.SeriousDlqin2yrs)
bentoml.sklearn.save_model(
    "scoring_model",
    rf_pipe
)
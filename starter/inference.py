import pandas as pd
import os
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder
from starter.ml.data import process_data
from starter.ml.model import inference
from starter.ml.model import compute_model_metrics
import logging

test_path = os.getcwd() + '/data/census_test.csv'
test = pd.read_csv(test_path)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
encoder = pd.read_pickle(os.getcwd() + "/model/encoder.pickle")
model = pd.read_pickle(os.getcwd() + "/model/model.pickle")
lb = pd.read_pickle(os.getcwd() + "/model/lb.pickle")

X_test, y_test, _, _ = process_data(test, cat_features, label= "salary", encoder=encoder, lb=lb, training=False)
y_preds=inference(model, X_test)
print(y_preds)
print(y_test)
prc, rcl, fb = compute_model_metrics(y_test, y_preds)
log = "Precision: %s Recall: %s FBeta: %s" % (prc, rcl, fb)
print(log)
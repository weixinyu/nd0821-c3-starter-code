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
slice_metrics = []
for cat in cat_features:
    for cal_val in test[cat].unique():
        df_tmp = test[test[cat] == cal_val]
        
        X_test, y_test, _, _ = process_data(df_tmp, cat_features, label= "salary", encoder=encoder, lb=lb, training=False)
        y_preds=inference(model, X_test)
        prc, rcl, fb = compute_model_metrics(y_test, y_preds)
        log = "[%s->%s] Precision: %s Recall: %s FBeta: %s" % (cat, cal_val, prc, rcl, fb)
        logging.info(log)

        slice_metrics.append(log)

with open('slice_output.txt', 'w') as out:
    for slice_metric in slice_metrics:
        out.write(slice_metric + '\n')
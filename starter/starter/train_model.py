# Script to train machine learning model.
import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split


from ml.data import process_data
from ml.model import train_model
from ml.model import compute_model_metrics

# load in the data.
data = pd.read_csv(os.getcwd() + '/data/census_clean.csv')    
# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

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
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

# Train and save a model.
model = train_model(X_train, y_train)

with open('model/model.pickle', 'wb') as f:
    pickle.dump(model, f)


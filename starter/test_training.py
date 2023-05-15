import pandas as pd
import pytest
import os
from starter.ml.data import process_data
from starter.ml.model import train_model
from sklearn.model_selection import train_test_split

@pytest.fixture
def raw_data():
    """ Simple function to import raw data."""
    data = pd.read_csv(os.getcwd() + '/data/census_clean.csv')
    return data

@pytest.fixture
def train_data(raw_data):
    """ Processing data."""
    train, test = train_test_split(raw_data, test_size=0.20)
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
    return X_train, y_train

@pytest.fixture
def model(train_data):
    """ Simple function to import raw data."""
    X_train, y_train = train_data
    model = train_model(X_train, y_train)
    
    return model

def test_data_shape(raw_data):
    """ Test whether the shape of raw data is right. """
    assert raw_data.shape == raw_data.dropna().shape, "Dropping null changes shape."


def test_column_names(raw_data):
    """ Test whether the column names of raw data is right. """
    expected_colums = ['age', 'workclass', 'fnlgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
       'salary']

    these_columns = raw_data.columns.values

    # This also enforces the same order
    assert list(expected_colums) == list(these_columns)
    
def test_process_data(train_data):
    """ Test whether the process data function return the right training data. """
    X_train, y_train = train_data
    assert 108 == X_train.shape[1]
    
def test_model(model):
    """ Test whether the training function return the right model type. """
    assert "RandomForestClassifier" == model.__class__.__name__
# Put the code for your API here.
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import os
from starter.ml.data import process_data
from starter.ml.model import inference

# Instantiate the app.
app = FastAPI()

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
encoder = pd.read_pickle(os.getcwd() + "/starter/model/encoder.pickle")
model = pd.read_pickle(os.getcwd() + "/starter/model/model.pickle")
lb = pd.read_pickle(os.getcwd() + "/starter/model/lb.pickle")


class Predictor(BaseModel):
    age: int = Field(example=65)
    workclass: str = Field(example='Private')
    fnlgt: int = Field(example=153522)
    education: str = Field(example='HS-grad')
    education_num: int = Field(alias='education-num', example=9)
    marital_status: str = Field(alias='marital-status', example='Widowed')
    occupation: str = Field(example='Other-service')
    relationship: str = Field(example='Unmarried')
    race: str = Field(example='White')
    sex: str = Field(example='Female')
    capital_gain: int = Field(alias='capital-gain', example=0)
    capital_loss: int = Field(alias='capital-loss', example=0)
    hours_per_week: int = Field(alias='hours-per-week', example=40)
    native_country: str = Field(alias='native-country', example='United-States')


# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}

@app.post("/predict")
async def predict(payload: Predictor):
    data = pd.DataFrame(payload.__dict__, index=[0])
    data.columns = ['age', 'workclass', 'fnlgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country']
    print(data)
    X_test, _, _, _ = process_data(data, cat_features, label= None, encoder=encoder, lb=lb, training=False)
    pred=inference(model, X_test)
    print(pred)
    if pred[0] == 0:
        result = '<=50K'
    else:
        result = '>50K'
    return {"result": result}
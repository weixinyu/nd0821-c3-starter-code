import requests
import os
import json
import subprocess
import pandas as pd
#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000/"

#################Load config.json and get path variables
data = '{"age": 65, "workclass": "Private", "fnlgt": 153522, "education": "HS-grad", "education-num": 9, "marital-status": "Widowed", "occupation": "Other-service", "relationship": "Unmarried", "race": "White", "sex": "Female", "capital-gain": 0, "capital-loss": 0, "hours-per-week": 17, "native-country": "United-States"}'
h = {'Content-Type': 'application/json;charset=UTF-8'}
#Call each API endpoint and store the responses
response1 = subprocess.run(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', data, 'http://127.0.0.1:8000/predict'],capture_output=True).stdout
#response1 = subprocess.run(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', '{"file-location": "testdata", "filename": "testdata.csv"}', 'http://127.0.0.1:8000/predict'],capture_output=True).stdout
response2 = requests.get(URL).content


#combine all API responses
responses = [response1, response2]

print(responses)

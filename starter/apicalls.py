import requests
import os
import json
import subprocess
#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000/"

#################Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 
model_path = os.path.join(config['output_model_path'])
d = {'filelocation': 'testdata', 'filename': 'testdata.csv'}
h = {'Content-Type': 'application/json;charset=UTF-8'}
#Call each API endpoint and store the responses
response1 = subprocess.run(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', '{"filelocation": "testdata", "filename": "testdata.csv"}', 'http://127.0.0.1:8000/prediction'],capture_output=True).stdout
response2 = requests.get(URL + 'scoring').content
response3 = requests.get(URL + 'summarystats').content
response4 = requests.get(URL + 'diagnostics').content

#combine all API responses
responses = [response1, response2, response3, response4]

#write the responses to your workspace
apireturns_file = open(os.getcwd() + '/' + model_path + '/' + 'apireturns2.txt','w')
apireturns_file.write(str(responses))



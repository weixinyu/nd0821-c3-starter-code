import requests
import subprocess
URL = "https://predict-income.onrender.com/"
#Call each API endpoint and store the responses
data = '{"age": 65, "workclass": "Private", "fnlgt": 153522, "education": "HS-grad", "education-num": 9, "marital-status": "Widowed", "occupation": "Other-service", "relationship": "Unmarried", "race": "White", "sex": "Female", "capital-gain": 0, "capital-loss": 0, "hours-per-week": 17, "native-country": "United-States"}'
response4 = requests.post(URL + 'predict', data = data)
print(response4.status_code)
print(response4.content)
h = {'Content-Type': 'application/json;charset=UTF-8'}

response1 = subprocess.run(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', data, URL + 'predict'], capture_output=True).stdout
data3 = '{"age": 58, "workclass": "Federal-gov", "fnlgt": 72998, "education": "11th", "education-num": 7, "marital-status": "Divorced", "occupation": "Craft-repair", "relationship": "Not-in-family", "race": "Black", "sex": "Female", "capital-gain": 14084, "capital-loss": 0, "hours-per-week": 40, "native-country": "United-States"}'
response3 = subprocess.run(['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', data3, 'http://127.0.0.1:8000/predict'], capture_output=True).stdout
response2 = requests.get(URL).content


#combine all API responses
responses = [response1, response2, response3, response4]
print(responses)



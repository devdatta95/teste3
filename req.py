import requests
import json

url = "http://172.20.192.1:5080/prediction"

payload = json.dumps({
  "Gender": 0,
  "Married": 0,
  "Dependents": 10,
  "Education": 1,
  "Self_Employed": 0,
  "ApplicantIncome": 1000000,
  "CoapplicantIncome": 0,
  "LoanAmount": 104300,
  "Loan_Amount_Term": 36,
  "Credit_History": 0,
  "Property_Area": 2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

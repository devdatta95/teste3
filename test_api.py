import requests
import json

url = "http://192.168.1.89:5080/prediction"

payload = json.dumps({
  "Gender": 1,
  "Married": 0,
  "Dependents": 10,
  "Education": 1,
  "Self_Employed": 0,
  "ApplicantIncome": 1,
  "CoapplicantIncome": 0,
  "LoanAmount": 10,
  "Loan_Amount_Term": 456,
  "Credit_History": 1,
  "Property_Area": 2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

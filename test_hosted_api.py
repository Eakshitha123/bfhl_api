import requests

url = "https://bfhl-api-82eh.onrender.com/bfhl"
data = {"data": ["a","1","334","4","R","$"]}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)  # should print 200
print("Response JSON:", response.json())     # should print your API response

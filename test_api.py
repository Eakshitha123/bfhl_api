import requests

url = "http://127.0.0.1:5000/bfhl"  # Local URL
data = {"data": ["a","1","334","4","R","$"]}

response = requests.post(url, json=data)
print(response.json())

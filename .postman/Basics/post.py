import requests

response = requests.post("https://dummyjson.com/products/add")
print(response.status_code)
print(response.json())
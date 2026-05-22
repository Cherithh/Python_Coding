import requests

response = requests.delete("https://dummyjson.com/products/1")
obj = response.json()
print(response.status_code)
print(obj)
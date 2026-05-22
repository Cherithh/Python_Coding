import requests

# 200
response2 = requests.get("https://httpbin.org/status/200")
print(response2.status_code)

# 404
response3 = requests.get("https://httpbin.org/status/404")
print(response3.status_code)

# 401
response1 = requests.get("https://httpbin.org/status/401")
print(response1.status_code)

#  500
response = requests.get("https://httpbin.org/status/500")
print(response.status_code)

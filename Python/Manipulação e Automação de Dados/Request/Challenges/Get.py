import requests

url = requests.get("httpbin.org/get", verify=False)
print(url)
print(url.json())
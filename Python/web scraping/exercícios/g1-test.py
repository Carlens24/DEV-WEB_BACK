import requests

response = requests.get("https://g1.globo.com/", verify=False)
print(response.status_code)

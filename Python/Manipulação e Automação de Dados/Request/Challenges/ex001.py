import requests

payload = {"Nome": "Carlens", "Sobrenome": "Oslin"}
R = requests.post("https://httpbin.org", data=payload, verify=False)
print(R.text)

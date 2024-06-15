import requests as re

payload = re.get("https://www.google.com.br/", verify=False)
print(payload.text.)

import requests

url = requests.get("https://carlens23.github.io/Projeto-cordel/")
print(url)
print(url.text)
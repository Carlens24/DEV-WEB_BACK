import re 
import requests

path = requests.get("https://pt.wikipedia.org/wiki/Portal:Eventos_atuais", verify=False)
print(path.content.find("div", class_='main-page-block-heading'))


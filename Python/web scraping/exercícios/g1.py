import requests as re
from bs4 import BeautifulSoup as beau
response = re.get("https://g1.globo.com/", verify=False)

content = response.content

site = beau(content, 'html.parser')

noticia = site.find('span', attrs={'class': 'bstn-hl-title gui-color-primary gui-color-hover gui-color-primary-bg-after'})

print(noticia.prettify())




"""import requests as re
from bs4 import BeautifulSoup

response = re.get("https://g1.globo.com/", verify=False)
content = response.content

url = BeautifulSoup(content, 'html.parser')
news = url.find("div", attrs={'class': 'floating-bar'})
title = news.find("a", attrs={"class": 'bstn-hl-link bstn-related'})
print(title.text)

subtitle = news.find("div", attrs={'class': 'feed-post-body-resumo'})
print(subtitle.text)"""


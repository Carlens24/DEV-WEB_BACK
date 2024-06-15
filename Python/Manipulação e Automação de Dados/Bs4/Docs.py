import requests as re
from bs4 import BeautifulSoup as bs4

path = "https://www.bing.com/search?pglt=171&q=cota%C3%A7%C3%A3o+do+d%C3%B3lar+hoje+no+brasil"

# Uso do headers pra que o navegador reconheça a requisição como uma pesquisa feita pro navegador e não feita por python.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}

requ = re.get(path, verify=False, headers=headers)
print(requ)
#print(requ.text)

# A estrutura "HTML" do site inteiro
web = bs4(requ.text, 'html.parser')
"""print(web.prettify())"""

# titulo 00 - por numeração da tag
tlt00 = web.find_all("span", class_='fin_scitl')
"""print(tlt00[3])"""

# titulo 01 - por especificação da class da tag 
tlt = web.find_all("div", class_='fin_scTitle')
"""print(tlt.get_text())"""

# Resultado da pesquisa final
rsl = web.find("div", class_='b_focusTextSmall curr_totxt')
"""print(rsl.prettify())"""

# Pegando pelo valor que esta dentro da tag
bp = web.find("textarea", class_='b_searchbox')
print(bp)
print(bp["value"])
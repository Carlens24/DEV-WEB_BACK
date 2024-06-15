import requests as re
from bs4 import BeautifulSoup as bs4

# URL que será raspada
path = "https://www.bing.com/search?pglt=171&q=cota%C3%A7%C3%A3o+do+d%C3%B3lar+hoje+no+brasil"

# Headers - para simular uma requisição de navegador
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}

# Fazendo a requisição para a URL
requ = re.get(path, verify=False, headers=headers)
print(requ.status_code)  # Imprime o status da requisição

# Criando um objeto BeautifulSoup com o conteúdo da resposta
web = bs4(requ.text, 'html.parser')

# Buscando todos os elementos 'span' com a classe 'fin_scitl'
tlt00 = web.find_all("span", class_='fin_scitl')

# Buscando todos os elementos 'div' com a classe 'fin_scTitle'
tlt = web.find_all("div", class_='fin_scTitle')

# Buscando o elemento 'div' com a classe 'b_focusTextSmall curr_totxt'
rsl = web.find("div", class_='b_focusTextSmall curr_totxt')

# Buscando o elemento 'textarea' com a classe 'b_searchbox'
bp = web.find("textarea", class_='b_searchbox')

# Imprimindo o valor dentro da tag 'textarea'
print(bp["value"])

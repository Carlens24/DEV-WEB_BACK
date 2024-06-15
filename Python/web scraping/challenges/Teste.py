import requests
from bs4 import BeautifulSoup as bs
import selenium

path = "https://www.pichau.com.br/hardware/placa-de-video"

web = requests.get(path, verify=False)
sp = bs(web.content, 'html.parser')
plc = bs.find_all("div", class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-2')

lst = bs.find("span", classs_='MuiTouchRipple-root')
""'
import requests
from bs4 import BeautifulSoup as bs

path = "https://www.pichau.com.br/hardware/placa-de-video"

# Não é necessário definir cabeçalhos personalizados neste caso
web = requests.get(path)

# Verifica se a solicitação foi bem-sucedida
if web.status_code == 200:
    sp = bs(web.content, 'html.parser')
    
    # Encontre todos os elementos que correspondem à classe desejada
    plc = sp.find_all("div", class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-2')
    
    # Para cada elemento encontrado, obtenha o texto dentro da tag span
    for item in plc:
        span = item.find("span", class_='MuiTouchRipple-root')
        if span:
            print(span.text)
else:
    print("Erro ao carregar a página:", web.status_code)
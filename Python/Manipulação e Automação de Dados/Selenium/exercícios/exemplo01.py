import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do WebDriver (ajuste o caminho do driver de acordo com o seu sistema operacional)
driver = webdriver.Chrome('caminho/do/chromedriver')

# Lista de URLs dos filmes no IMDb
urls_filmes = [
    'https://www.imdb.com/title/tt0111161/',  # Exemplo: "Um Sonho de Liberdade"
    'https://www.imdb.com/title/tt0468569/'  # Exemplo: "Batman: O Cavaleiro das Trevas"
]

# Listas para armazenar os dados
nomes = []
notas = []

# Iterar sobre as URLs dos filmes
for url in urls_filmes:
    # Navegar para a página do filme
    driver.get(url)
    
    # Extrair nome do filme
    nome_filme = driver.find_element(By.XPATH, '//h1').text
    nomes.append(nome_filme)
    
    # Extrair nota do filme
    nota_filme = driver.find_element(By.XPATH, '//span[@itemprop="ratingValue"]').text
    notas.append(nota_filme)

# Criar DataFrame Pandas
df = pd.DataFrame({'Nome do Filme': nomes, 'Nota IMDb': notas})

# Salvar DataFrame em um arquivo Excel
df.to_excel('filmes_imdb.xlsx', index=False)

# Fechar o navegador
driver.quit()

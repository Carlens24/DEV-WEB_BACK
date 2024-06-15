from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://meta.wikimedia.org/wiki/Event:%C2%A1Alto!_Mujeres_haciendo_historia/pt-br")

login = driver.find_element(By.ID, "pt-login-2").click()
nome = driver.find_element(By.ID, "wpName1")
nome.send_keys("carlens.os")
senha = driver.find_element(By.ID, "wpPassword1")
senha.send_keys("schneidine")
button = driver.find_element(By.XPATH, "//button[@id='wpLoginAttempt']").click()

title = driver.find_element(By.XPATH, "//h1[@id='firstHeading']")
print("\n", title.text, "\n")

parags = driver.find_elements(By.TAG_NAME, "P")
print(parags[3].text, "\n")
print(parags[4].text, "\n")
print(parags[5].text, "\n")

data = [[title.text, parags[3].text, parags[4].text, parags[5].text]]
df = pd.DataFrame(data, columns=['Título', 'Parágrafo_1', 'Parágrafo_2', 'Parágrafo_3'])

nome_do_arquivo = 'Dia das mulheres.xlsx'
df.to_excel(nome_do_arquivo, index=False)

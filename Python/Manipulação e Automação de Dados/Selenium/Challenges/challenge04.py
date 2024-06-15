from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.common.keys
import pandas as pd
import time as t

tabela = pd.read_excel(r"C:\Users\carlens.oslin\Documents\Python\Selenium\Challenges\challenge04.xlsx")
print(tabela)

navegador = webdriver.Chrome()
navegador.get("https://forms.gle/GgiMoFKZHFWjUCkt5")
t.sleep(9)

for indice, coluna in tabela.iterrows():
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i1']").send_keys(coluna["Nome"])
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i5']").send_keys(str(coluna["Data de Nascimento"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i9']").send_keys(str(coluna["E-mail"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i13']").send_keys(str(coluna["Telefone"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i17']").send_keys(str(coluna["Profissão"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i21']").send_keys(str(coluna["Endereço"]))
    navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[0].click()


    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i1']").send_keys(str(coluna["Escolaridade"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i5']").send_keys(str(coluna["Instituição"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i9']").send_keys(str(coluna["Curso/Major"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i13']").send_keys(str(coluna["Certificação"]))
    navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[1].click()


    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i1']").send_keys(str(coluna["Cargo Atual"]))
    navegador.find_element(By.XPATH, "//input[@aria-labelledby='i9']").send_keys(str(coluna["Tempo na Posição"]))
    navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[1].click()
    
    
    navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i1']").send_keys(str(coluna["Descoberta do Produto"]))
    navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i5']").send_keys(str(coluna["Satisfação"]))
    navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i9']").send_keys(str(coluna["O que mais gostou"]))
    navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i13']").send_keys(str(coluna["O que poderíamos melhorar"]))
    navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i17']").send_keys(str(coluna["Recomendação"]))
    navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[1].click()


    navegador.find_element(By.XPATH,  "//label[@for='i5']").click()
    navegador.find_element(By.XPATH,  "//div[@class='Od2TWd hYsg7c']").click()
    navegador.find_element(By.XPATH,  "//label[@for='i34']").click()
    navegador.find_elements(By.XPATH,  "//span[@class='NPEfkd RveJvd snByac']")[-2].click()
    navegador.quit()
    print("-" * 200)

     
     
     
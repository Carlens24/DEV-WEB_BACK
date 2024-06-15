# Challenge de preenchimento de formulario automatico
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

tabela = pd.read_excel(r"C:\Users\carlens.oslin\Documents\Python\Selenium\Challenges\challenge01.xlsx")
print(tabela)

navegador = webdriver.Chrome()
navegador.get("https://rpachallenge.com/")

for index,item in tabela.iterrows():
     navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelCompanyName']").send_keys(item["Company Name"])
     navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelFirstName']").send_keys(item["First Name"])
     navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelPhone']").send_keys(item["Phone Number"])
     navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelAddress']").send_keys(item["Address"])
     navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelLastName']").send_keys(item["Last Name "])
     navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelEmail']").send_keys(item["Email"])
     navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelRole']").send_keys(item["Role in Company"])
     navegador.find_element(By.XPATH, "//input[@type='submit']").click()

print("-" * 200)
print("Automatização realizado com sucesso!")
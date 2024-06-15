from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/data-list-filter-demo.html")

lista = []

driver.find_element(By.CLASS_NAME, "form-control").send_keys("A")
t.sleep(4)

infos = driver.find_elements(By.XPATH, "//div[@class='info-block block-info clearfix']")

for info in infos:
    linha = []
    linha.append(info.find_element(By.TAG_NAME, "h5").text)
    linha.append(info.find_element(By.TAG_NAME, "h4").text)
    linha.append(info.find_element(By.TAG_NAME, "p").text)
    spanData = info.find_elements(By.TAG_NAME, 'span')
    linha.append(spanData[0].text)
    linha.append(spanData[1].text)
    lista.append(linha)

df = pd.DataFrame(lista)
df.to_excel("Data list filter - infos.xlsx")

   














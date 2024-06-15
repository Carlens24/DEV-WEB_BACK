import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get('https://carlens23.github.io/Projeto-cordel/')
t.sleep(5)

elements = driver.find_elements(By.TAG_NAME, "p")
list = [element.text for element in elements]

df = pd.DataFrame({"Cordel": list})
df.to_excel('Cordel.xlsx', index=False)

print("As informações foram salvas no arquivo 'Cordel.xlsx'.")

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://g1.globo.com/")

# Main news
Nws1 = driver.find_elements(By.CLASS_NAME, "bstn-hl-list")[0].text
print(Nws1 + "\n")

Nws2 = driver.find_elements(By.CLASS_NAME, "bstn-hl-list")[1].text
print(Nws2 + "\n")

# Others
# Exibição de alguns de uma unica vez, sem formato algum
Nwess = driver.find_elements(By.XPATH, "//div[@class='_evg']")[1].text
print(Nwess + "\n")


# Exibição gradual de alguns, formatados
"""Nws = driver.find_elements(By.XPATH, "//div[@class='feed-post bstn-item-shape type-materia']")[0].text
print(Nws + "\n")

Nws = driver.find_elements(By.XPATH, "//div[@class='feed-post bstn-item-shape type-materia']")[1].text
print(Nws + "\n")

Nws = driver.find_elements(By.XPATH, "//div[@class='feed-post bstn-item-shape type-materia']")[2].text
print(Nws + "\n")

Nws = driver.find_elements(By.XPATH, "//div[@class='feed-post bstn-item-shape type-materia']")[3].text
print(Nws + "\n")

Nws = driver.find_elements(By.XPATH, "//div[@class='feed-post bstn-item-shape type-materia']")[4].text
print(Nws + "\n")

Nws = driver.find_elements(By.XPATH, "//div[@class='feed-post bstn-item-shape type-materia']")[5].text
print(Nws + "\n")
"""
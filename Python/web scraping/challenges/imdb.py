from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.rottentomatoes.com/browse/movies_at_home/sort:popular")

catalogo = driver.find_element(By.XPATH, "//ul[@class='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base']")
print(catalogo.text)

nome = driver.find_elements(By.XPATH, "//span[@class='p--small']")

"""nota01 = driver.find_elements(By.XPATH, "//div[@class='wrap']")
nota02 = driver.find_elements(By.XPATH, "")"""


for i in range(3):
    n = nome[i].text
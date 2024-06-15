from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.mercadolivre.com.br/")

oferta = driver.find_elements(By.XPATH, "//div[@class='ui-recommendations-carousel-snapped new-carousel']")[0]
print(oferta.text, "\n")

ofertas = driver.find_elements(By.XPATH, "//div[@class='ui-recommendations-carousel-snapped new-carousel']")[1]
print(ofertas.text)
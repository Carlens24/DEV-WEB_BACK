from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/charts-mouse-hover-demo.html")

list = []
graphic = driver.find_elements(By.XPATH, "//div[@class='row']")

if len(graphic) > 3:
    element_text = graphic[3].text
    print(element_text)
else:
    print("Não há elementos suficientes na lista para acessar o índice 3.")
    
element_text = graphic[3].text
print(element_text)

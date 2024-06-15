from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


navegador = webdriver.Chrome()
navegador.get("file:///C:/Users/carlens.oslin/Downloads/Formul%C3%A1rio%20Social%20-%20SMADS%20_%20COVS.html")

navegador.find_element(By.XPATH,  "//button[@name='move']").click()
navegador.find_element(By.XPATH,  "//select[@class='form-select form-control list-question-select']").click()




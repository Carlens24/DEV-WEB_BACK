from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
navegador = webdriver.Chrome()
navegador.get("https://demo.seleniumeasy.com/bootstrap-progress-bar-dialog-demo.html")

navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button[1]').click()
t.sleep(5)
navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button[2]').click()
t.sleep(5)
navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/button[3]').click()
t.sleep(5)




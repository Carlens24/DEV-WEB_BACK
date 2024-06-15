from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.common.alert import Alert


navegador = webdriver.Chrome()
navegador.get("https://demo.seleniumeasy.com/javascript-alert-box-demo.html")

botoes = navegador.find_elements(By.XPATH, "//button[@class='btn btn-default btn-lg']")

navegador.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
t.sleep(4)
alerta = Alert(navegador)
alerta.accept()

botoes[0].click()
t.sleep(4)
alerta = Alert(navegador)
alerta.accept()

botoes[0].click()
t.sleep(4)
alerta = Alert(navegador)
alerta.send_keys("Carlens oslin")
alerta.accept()











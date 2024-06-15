from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

navegador = webdriver.Chrome()
navegador.get("https://demo.seleniumeasy.com/window-popup-modal-demo.html")

navegador.find_element(By.XPATH, "//a[@title='Follow @seleniumeasy']").click()
t.sleep(9)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://carlens23.github.io/Projeto-login/")

driver.find_element(By.ID, "ilogin").send_keys("Carlensoslin@gmail.com")
t.sleep(2)
driver.find_element(By.ID, "isenha").send_keys("Schneidine23")
t.sleep(2)
driver.find_element(By.XPATH, "//input[@type='submit']").click()
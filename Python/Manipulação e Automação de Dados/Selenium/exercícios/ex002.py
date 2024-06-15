import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.common.keys


navegador = webdriver.Chrome()
navegador.get("https://rpachallenge.com/")

navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelCompanyName']").send_keys("PUC, PR")
navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelFirstName']").send_keys("Carlens")
navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelPhone']").send_keys("(41)-997809090")
navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelAddress']").send_keys("Prado velho, PR")
navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelLastName']").send_keys("Oslin Henry")
navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelEmail']").send_keys("carlensoslin@gmail.com")
navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelRole']").send_keys("Jovem aprediz")
navegador.find_element(By.XPATH,  "//input[@ng-reflect-name='labelRole']").send_keys("Jovem aprediz")
navegador.find_element(By.XPATH, "//input[@type='submit']").click()

input("Olá, Mundo")





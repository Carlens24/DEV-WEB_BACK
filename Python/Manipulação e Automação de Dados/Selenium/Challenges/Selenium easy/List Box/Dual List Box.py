from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

navegador = webdriver.Chrome()
navegador.get("https://demo.seleniumeasy.com/bootstrap-dual-list-box-demo.html")
t.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="listhead"]/div[1]/div/input').send_keys("Dapi")
t.sleep(4)
navegador.find_element(By.XPATH, '//*[@id="listhead"]/div[2]/div/a').click()
t.sleep(2)
navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/button[2]/span').click()
t.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="listhead"]/div[2]/div/input').send_keys("Mor")
t.sleep(4)
navegador.find_element(By.XPATH, '//*[@id="listhead"]/div[1]/div/a').click()
t.sleep(2)
navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/button[1]').click()
t.sleep(2)





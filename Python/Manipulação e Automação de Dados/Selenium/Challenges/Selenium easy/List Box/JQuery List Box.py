from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/jquery-dual-list-box-demo.html")

driver.find_element(By.XPATH, "//option[@data-id='1']").click()
driver.find_element(By.XPATH, "//option[@data-id='14']").click()
t.sleep(2)
driver.find_element(By.XPATH, "//button[@class='pAdd btn btn-primary btn-sm']").click()
t.sleep(2)
driver.find_element(By.XPATH, "//option[@data-id='1']").click()
driver.find_element(By.XPATH, "//option[@data-id='14']").click()
t.sleep(2)
driver.find_element(By.XPATH, "//button[@class='pRemoveAll btn btn-primary btn-sm']").click()
t.sleep(2)
driver.find_element(By.XPATH, "//button[@class='pAddAll btn btn-primary btn-sm']").click()
t.sleep(2)
driver.find_element(By.XPATH, "//button[@class='pRemoveAll btn btn-primary btn-sm']").click()
t.sleep(2)
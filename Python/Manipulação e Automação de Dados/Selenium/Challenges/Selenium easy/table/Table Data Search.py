from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/table-search-filter-demo.html")

form00 = driver.find_element(By.CLASS_NAME, "form-control")
form00.click()
form00.send_keys("7")
t.sleep(6)

driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div/button').click()
t.sleep(6)

form01 = driver.find_element(By.XPATH, "//input[@placeholder='#']")
form01.click()
form01.send_keys("1")
t.sleep(6)
form02 = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
form02.click()
form02.send_keys("m")
t.sleep(6)
form03 = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
form03.click()
form03.send_keys("B")
t.sleep(6)
form04 = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
form04.click()
form04.send_keys("S")
t.sleep(6)




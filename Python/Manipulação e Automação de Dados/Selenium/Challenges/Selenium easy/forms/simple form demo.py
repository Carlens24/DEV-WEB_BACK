from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

element01 = driver.find_element(By.XPATH, "//input[@placeholder='Please enter your Message']")
element01.send_keys("Olodum, ilyê alyê")
button01 = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
button01.click()

value01 = driver.find_element(By.XPATH, "//input[@id='value1']")
value01.send_keys("22")

value02 = driver.find_element(By.XPATH, "//input[@id='value2']")
value02.send_keys("92")

button02 = driver.find_element(By.XPATH, '//*[@id="gettotal"]/button')
button02.click()
t.sleep(12)




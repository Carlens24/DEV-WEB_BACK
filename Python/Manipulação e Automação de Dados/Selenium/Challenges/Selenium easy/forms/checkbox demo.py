from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")

element01 = driver.find_element(By.ID, "isAgeSelected")
element01.click()

button = driver.find_element(By.ID, "check1")
button.click()

element02 = driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/div[4]/label/input')
element02.click()
t.sleep(12)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-radiobutton-demo.html")

element01 = driver.find_element(By.XPATH, "//input[@name='optradio']")
element01.click()
checkButton = driver.find_element(By.ID, "buttoncheck")
checkButton.click()
element02 = driver.find_element(By.XPATH, "//input[@name='gender']")
element02.click()
element03 = driver.find_element(By.XPATH, "//input[@value='5 - 15']")
element03.click()
valueButton = driver.find_element(By.XPATH, '//*[@id="easycont"]/div/div[2]/div[2]/div[2]/button')
valueButton.click()
t.sleep(12)
t.sleep(6)
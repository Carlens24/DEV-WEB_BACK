from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.find_element(By.ID, "downloadButton").click()
t.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/button').click()

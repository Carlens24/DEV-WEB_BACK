from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")

button = driver.find_element(By.ID, "cricle-btn")
button.click()
t.sleep(22)

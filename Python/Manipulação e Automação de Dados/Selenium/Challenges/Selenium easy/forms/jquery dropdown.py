from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/jquery-dropdown-search-demo.html")

driver.find_element(By.CLASS_NAME, "select2-selection__arrow").click()
t.sleep(2)
driver.find_element(By.CLASS_NAME, "select2-results__option select2-results__option--highlighted").click()
t.sleep(2)


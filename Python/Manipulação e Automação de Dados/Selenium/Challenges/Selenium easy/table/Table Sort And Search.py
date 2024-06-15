from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/table-sort-search-demo.html")


driver.find_element(By.XPATH, "//input[@type='search']").send_keys("junior")
t.sleep(6)
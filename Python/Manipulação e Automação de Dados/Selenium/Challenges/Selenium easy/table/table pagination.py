from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/table-pagination-demo.html")

next_link = driver.find_element(By.CLASS_NAME, "next_link")
next_link.click()
t.sleep(3)
next_link.click()
t.sleep(3)

prev_link = driver.find_element(By.CLASS_NAME, "prev_link")
prev_link.click()
t.sleep(3)
prev_link.click()
t.sleep(3)

table = pd.read_html("https://demo.seleniumeasy.com/table-pagination-demo.html")
print(table[0, 1, 2])


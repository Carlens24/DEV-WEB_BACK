"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/table-records-filter-demo.html")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[1]").click()
t.sleep(6)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[2]").click()
t.sleep(6)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[3]").click()
t.sleep(6)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[4]").click()
t.sleep(6)
"""
# Codigo melhorado em 100%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/table-records-filter-demo.html")

for i in range(1, 5):
    xpath = f"/html/body/div[2]/div/div[2]/section/div/div/div[2]/div[1]/div/button[{i}]"
    driver.find_element(By.XPATH, xpath).click()
    t.sleep(6)



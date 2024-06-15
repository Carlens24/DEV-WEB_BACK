"""from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html")

driver.find_element(By.ID, 'autoclosable-btn-success').click()
t.sleep(6)
driver.find_element(By.ID, 'normal-btn-success').click()
t.sleep(6)
driver.find_element(By.ID, 'autoclosable-btn-warning').click()
t.sleep(6)
driver.find_element(By.ID, 'normal-btn-warning').click()
t.sleep(6)
driver.find_element(By.ID, 'autoclosable-btn-danger').click()
t.sleep(6)
driver.find_element(By.ID, 'normal-btn-danger').click()
t.sleep(6)
driver.find_element(By.ID, 'autoclosable-btn-info').click()
t.sleep(6)
driver.find_element(By.ID, 'normal-btn-info').click()
t.sleep(6)"""

# Verão melhorada
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

def click_and_wait(driver, element_id):
    driver.find_element(By.ID, element_id).click()
    t.sleep(6)

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html")

click_and_wait(driver, 'autoclosable-btn-success')
click_and_wait(driver, 'normal-btn-success')
click_and_wait(driver, 'autoclosable-btn-warning')
click_and_wait(driver, 'normal-btn-warning')
click_and_wait(driver, 'autoclosable-btn-danger')
click_and_wait(driver, 'normal-btn-danger')
click_and_wait(driver, 'autoclosable-btn-info')
click_and_wait(driver, 'normal-btn-info')
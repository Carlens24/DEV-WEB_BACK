from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/bootstrap-date-picker-demo.html")


driver.find_element(By.CLASS_NAME, 'form-control').click()
driver.find_element(By.CLASS_NAME, 'today').click()

driver.find_element(By.XPATH, "//input[@placeholder='Start date']").click()
driver.find_element(By.CLASS_NAME, 'datepicker-switch').click()
driver.find_element(By.CLASS_NAME, 'month').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/table/tbody/tr[1]/td[2]').click()

driver.find_element(By.XPATH, "//input[@placeholder='End date']").click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/table/thead/tr[2]/th[2]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr/td/span[12]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/table/tbody/tr[6]/td[3]').click()
t.sleep(12)


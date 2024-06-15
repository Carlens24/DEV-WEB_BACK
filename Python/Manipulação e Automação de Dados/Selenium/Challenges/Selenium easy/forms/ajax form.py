from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/ajax-form-submit-demo.html")

driver.find_element(By.ID, "title").send_keys("Carlens oslin")
driver.find_element(By.ID, "description").send_keys("Passando pra dar um 'OI'!!!!!!!")
driver.find_element(By.ID, "btn-submit").click()
t.sleep(5)
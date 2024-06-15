from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/dynamic-data-loading-demo.html")

while True:
    botao = driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()
    t.sleep(4)
    img = driver.find_element(By.TAG_NAME, "img")
    print(img)

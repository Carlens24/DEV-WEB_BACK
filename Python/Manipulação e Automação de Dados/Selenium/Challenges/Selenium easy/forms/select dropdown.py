from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")

driver.find_element(By.CLASS_NAME, "form-control").click()

dias_da_semana = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for dia in dias_da_semana:
    driver.find_element(By.XPATH, f"//option[@value='{dia}']").click()
    t.sleep(1)

estados = ["California", "Florida", "New Jersey","New York" ,"Ohio", "Texas", "Pennsylvania", "Washington"]

for estado in estados:
     driver.find_element(By.XPATH, f"//option[@value='{estado}']").click()
     t.sleep(1)
     driver.find_element(By.ID, "printMe").click()
     t.sleep(1)

t.sleep(9)
print("-"*90)
driver.quit() 
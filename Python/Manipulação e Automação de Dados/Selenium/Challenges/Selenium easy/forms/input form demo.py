from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/input-form-demo.html")

driver.find_element(By.XPATH, '//input[@name="first_name"]').send_keys("João")
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name="last_name"]').send_keys("Silva")
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("joaosilva@example.com")
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("41 1234-5678")
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name="address"]').send_keys("Rua das Flores, 123")
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name="city"]').send_keys("Curitiba")
t.sleep(1)
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[7]/div/div/select/option[6]').click()
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name="zip"]').send_keys("96162")
t.sleep(1)
driver.find_element(By.XPATH, '//input[@name="website"]').send_keys("www.joaosilva.com.br")
t.sleep(1)
driver.find_element(By.XPATH, '//input[@value="yes"]').click()
t.sleep(1)
driver.find_element(By.XPATH, '//textarea[@name="comment"]').send_keys(" O SGPO é um sistema de gerenciamento de pedidos online.")
driver.find_element(By.XPATH, '//*[@id="contact_form"]/fieldset/div[13]/div/button').click()
t.sleep(12)
print("-" * 90)



"""from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/drag-drop-range-sliders-demo.html")

driver.find_element(By.XPATH, '//input[@value="10"]').click()
t.sleep(16)
driver.find_element(By.XPATH, '//input[@onchange="rangePrimary.value=value"]').click()
t.sleep(16)
driver.find_element(By.XPATH, '//input[@onchange="rangePrimary.value=value"]').click()
t.sleep(16)
driver.find_element(By.XPATH, '//input[@onchange="rangeInfo.value=value"]').click()
t.sleep(16)
driver.find_element(By.XPATH, '//input[@onchange="rangeWarning.value=value"]').click()
t.sleep(16)
driver.find_element(By.XPATH, '//input[@onchange="rangeDanger.value=value"]').click()"""


# Versão melhorada
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = Chrome()

driver.get('https://demo.seleniumeasy.com/drag-drop-range-sliders-demo.html')

elementos = driver.find_elements(By.XPATH, '//input[@type="range"]')


for i, v in zip(elementos, [50, 80, 60, 90, 2, 10]):
    driver.execute_script(f"arguments[0].value = arguments[1]", i, v)
input()


# Uso do "enumerate"
numeros = ['zero', 'um', 'dois', 'tres', 'quatro']

for i, v in enumerate(numeros):
     print(f"{i} - {v}")
     




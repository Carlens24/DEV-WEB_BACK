from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time as t

driver = webdriver.Chrome()
driver.get("https://www.google.com.br/")

driver.find_element(By.XPATH, "//textarea[@class='gLFyf']").send_keys('economia mundial wikipedia tabela' + Keys.ENTER)
t.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "wikipedia").click()
t.sleep(2)

PIB = pd.read_html(driver.current_url)
df = PIB[2]

df.to_excel("PIB.xlsx")
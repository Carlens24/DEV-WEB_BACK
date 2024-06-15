from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://g1.globo.com/")

feed_headers = driver.find_elements(By.XPATH, "//span[@class='bstn-hl-title gui-color-primary gui-color-hover gui-color-primary-bg-after']")
print("\n",feed_headers[0].text)
li1 = driver.find_elements(By.XPATH, "//a[@class='bstn-hl-link bstn-related']")
print("\n",li1[0].text)
li2 = driver.find_elements(By.XPATH, "//a[@class='bstn-hl-link bstn-related']")
print("\n",li1[1].text)



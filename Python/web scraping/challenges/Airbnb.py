from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.airbnb.com.br/")

catalogo = driver.find_element(By.XPATH, "//div[@class='f1l8mybd atm_j3_1371zjx atm_gw_1wugsn5 atm_lj_ke7zzc atm_li_ke7zzc atm_26_1hbpp16 atm_8w_wetwqu atm_vy_1osqo2v atm_gp_xwaa7j ft6862c atm_go_1ck42ei dir dir-ltr']")
print(catalogo.text)

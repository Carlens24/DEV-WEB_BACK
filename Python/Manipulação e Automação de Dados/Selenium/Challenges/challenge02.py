from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time as t

lista = []

navegador = webdriver.Chrome()
navegador.get("https://www.imdb.com/what-to-watch/fan-favorites/?ref_=hm_fanfav_sm") 
t.sleep(5)

img = navegador.find_elements(By.XPATH, "//img[@class='ipc-image']")
nota = navegador.find_elements(By.XPATH, "//span[@class='ipc-rating-star ipc-rating-star--baseAlt ipc-rating-star--imdb ipc-rating-star-group--imdb']")
name = navegador.find_elements(By.XPATH, "//span[@data-testid='title']")

for i in range(10):
     foto = img[i].get_attribute("src")
     avaliacao = nota[i].text
     nome = name[i].text
     lista.append([nome, avaliacao, foto])
     
pd.DataFrame(lista).to_excel("challenge02.xlsx")
     
     
     
     
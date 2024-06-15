from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

navegador = webdriver.Chrome()
navegador.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html#")

def click_wait(navegador, xpath):
     navegador.find_element(By.XPATH, xpath).click()
     t.sleep(6)

click_wait(navegador, '/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a')
click_wait(navegador, '//*[@id="myModal0"]/div/div/div[4]/a[2]')
click_wait(navegador, '/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/a')
click_wait(navegador, '//*[@id="myModal"]/div/div/div[3]/a')
click_wait(navegador, '//*[@id="myModal2"]/div/div/div[6]/a[2]')
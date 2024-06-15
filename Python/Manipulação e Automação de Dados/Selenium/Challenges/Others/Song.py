from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

youtube_bar = driver.find_element(By.XPATH, "//input[@name='search_query']").send_keys("Mount everest")
t.sleep(2)

buttons = driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']").click()
t.sleep(5)

video = driver.find_elements(By.XPATH, "//yt-formatted-string[@class='style-scope ytd-video-renderer']")
video[2].click()
t.sleep(19)

teste = driver.find_elements(By.XPATH, "//a[@class='yt-spec-button-shape-next yt-spec-button-shape-next--outline yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading']")
teste[0].click()
t.sleep(2)

search = driver.find_elements(By.XPATH ,"//input[@class='whsOnd zHQkBf']")
search[0].send_keys("Carlensoslin@gmail.com")








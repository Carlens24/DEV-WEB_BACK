from selenium import webdriver
import pandas as pd

navegador = webdriver.Chrome()
navegador.get("https://www.thesun.co.uk/sport/25689695/marcus-rashford-so-what-happened/")
container = navegador.find_elements(by="xpath", value='//div[@class="article__content"]/p').text
print(container)
pd.DataFrame(container).to_excel("teste.xlsx")
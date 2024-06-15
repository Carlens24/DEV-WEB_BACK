from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")

# Artigos em destaque
title01 = driver.find_elements(By.CLASS_NAME, "main-page-block-heading")[-4].text
print(title01)
parags01 = driver.find_elements(By.CLASS_NAME, "main-page-block-contents")[0].text
print(parags01)

# Eventos atuais
title02 = driver.find_elements(By.CLASS_NAME, "main-page-block-heading")[1].text
print(title02)
parags02 = driver.find_elements(By.CLASS_NAME, "main-page-block-contents")[1].text
print(parags02)

# 21 de março na história
title03 = driver.find_elements(By.CLASS_NAME, "main-page-block-heading")[2].text
print(title03)
parags03 = driver.find_elements(By.CLASS_NAME, "main-page-block-contents")[2].text
print(parags03)

# Sabia que...
title04 = driver.find_elements(By.CLASS_NAME, "main-page-block-heading")[3].text
print(title04)
parags04 = driver.find_elements(By.CLASS_NAME, "main-page-block-contents")[3].text
print(parags04)

#DataFrame
data = {
    "Title": [title01, title02, title03, title04],
    "Content": [parags01, parags02, parags03, parags04]
}

df = pd.DataFrame(data)

# Save DataFrame to Excel
df.to_excel("wikipedia_news.xlsx", index=False)
print("Os dados foram salvas com sucesso!!!!!!!!!!")

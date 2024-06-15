import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t

driver = webdriver.Chrome()
driver.get('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')

login = driver.find_element(By.ID, "pt-login-2").click()
nome = driver.find_element(By.ID, "wpName1")
nome.send_keys("carlens.os")
senha = driver.find_element(By.ID, "wpPassword1")
senha.send_keys("schneidine")
button = driver.find_element(By.XPATH, "//button[@id='wpLoginAttempt']").click()

search = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
search.send_keys("Lázaro Ramos" + Keys.ENTER)
t.sleep(2)

nome = driver.find_element(By.XPATH, "//h1[@id='firstHeading']")
print(nome.text)

bio = driver.find_elements(By.TAG_NAME, "p")
print(bio[1].text, "\n")
print(bio[2].text, "\n")
print(bio[3].text)

tables = pd.read_html(driver.current_url)
print(f"Tabela - 01: \n{tables[2]}\n")
print(f"Tabela - 02:\n{tables[3]}\n")
print(f"Tabela - 03:\n{tables[4]}\n")
print("Essas 3 tabelas foram salvas com sucesso nos arquivos 'web_scraping_table01.xlsx', 'web_scraping_table02.xlsx' e 'web_scraping_table03.xlsx'")

# Corrigindo a parte de salvamento das bios
bio_save01 = pd.DataFrame([bio[1].text], columns=['Bio'])
bio_save01.to_excel("Bio01.xlsx", index=False)

bio_save02 = pd.DataFrame([bio[2].text], columns=['Bio'])
bio_save02.to_excel("Bio02.xlsx", index=False)

bio_save03 = pd.DataFrame([bio[3].text], columns=['Bio'])
bio_save03.to_excel("Bio03.xlsx", index=False)

tabela_01 = tables[2]
tabela_01.to_excel("web_scraping_table01.xlsx", index=False)

tabela_02 = tables[3]
tabela_02.to_excel("web_scraping_table02.xlsx", index=False)

tabela_03 = tables[4]
tabela_03.to_excel("web_scraping_table03.xlsx", index=False)




""" Froma mais eficiente
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t

driver = webdriver.Chrome()
driver.get('https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal')

login = driver.find_element(By.ID, "pt-login-2").click()
nome = driver.find_element(By.ID, "wpName1")
nome.send_keys("carlens.os")
senha = driver.find_element(By.ID, "wpPassword1")
senha.send_keys("schneidine")
button = driver.find_element(By.XPATH, "//button[@id='wpLoginAttempt']").click()

search = driver.find_element(By.CLASS_NAME, "cdx-text-input__input")
search.send_keys("Lázaro Ramos" + Keys.ENTER)
t.sleep(2)

nome = driver.find_element(By.XPATH, "//h1[@id='firstHeading']")
print(nome.text)

bios = driver.find_elements(By.TAG_NAME, "p")

# Imprimir e salvar cada bio em um arquivo Excel separado
for i, bio in enumerate(bios[1:4], start=1):
    print(f"Bio - 0{i}: {bio.text}")
    bio_df = pd.DataFrame([bio.text], columns=['Bio'])
    bio_df.to_excel(f"Bio0{i}.xlsx", index=False)

tables = pd.read_html(driver.current_url)

# Salvar as tabelas em arquivos Excel
for i, table in enumerate(tables[2:5], start=1):
    table.to_excel(f"web_scraping_table0{i}.xlsx", index=False)

print("As bios e as tabelas foram salvas com sucesso nos arquivos 'Bio01.xlsx', 'Bio02.xlsx', 'Bio03.xlsx', 'web_scraping_table01.xlsx', 'web_scraping_table02.xlsx' e 'web_scraping_table03.xlsx'")

# Fechar o navegador após concluir
driver.quit()

"""
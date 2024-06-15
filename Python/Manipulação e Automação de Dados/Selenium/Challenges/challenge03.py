from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time as t

navegador = webdriver.Chrome()
navegador.get("https://forms.gle/GgiMoFKZHFWjUCkt5")
t.sleep(5)

lista = [["Carlens oslin", "18/08/2008", "carlensoslin@gmail.com", "41-997809090", "Programador - jovem aprendiz", "Curitiba PR - prado velho", "Ensino médio - cursando", "Colégio - Manoel ribas", "Não tenho", "Sim, mas não são tão importantes!!!", "Reconhecimento de processos - Jovem aprendiz", "Não!", "Alguns meses", "Sim", "Na internet", "Ótimo!!!", "A rapidez!!", "Nada eu acho!!", "SIM", "Boa", "NÃO", "Não",]]

navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i1']").send_keys(["Carlens oslin"])
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i5']").send_keys(["18/08/2008"])
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i9']").send_keys("carlensoslin@gmail.com")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i13']").send_keys("41-997809090")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i17']").send_keys("Programador - jovem aprendiz")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i21']").send_keys("Curitiba PR - prado velho")
navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[0].click()


navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i1']").send_keys("Ensino médio - cursando")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i5']").send_keys("Colégio - Manoel ribas")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i9']").send_keys("Não tenho")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i13']").send_keys("Sim, mas não são tão importantes!!!")
navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[1].click()


navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i1']").send_keys("Reconhecimento de processos - Jovem aprendiz")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i5']").send_keys("Não!")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i9']").send_keys("Alguns meses")
navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[1].click()


navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i1']").send_keys("Na internet")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i5']").send_keys("sim!!!")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i9']").send_keys("A rapidez!!")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i13']").send_keys("Nada eu acho!!")
navegador.find_element(By.XPATH,  "//input[@aria-labelledby='i17']").send_keys("sim!!!")
navegador.find_elements(By.XPATH,  "//span[@class='l4V7wb Fxmcue']")[1].click()


navegador.find_element(By.XPATH,  "//label[@for='i5']").click()
navegador.find_element(By.XPATH,  "//div[@class='Od2TWd hYsg7c']").click()
navegador.find_element(By.XPATH,  "//label[@for='i34']").click()
navegador.find_elements(By.XPATH,  "//span[@class='NPEfkd RveJvd snByac']")[-2].click()

pd.DataFrame(lista,columns=["Nome", "Data de Nascimento", "E-mail", "Telefone", "Profissão", "Endereço",	"Escolaridade", "Instituição", "Curso/Major", "Certificação", "Cargo Atual", "Certificação adicional", "Tempo na Posição",	"Avaliação do produto",	"Descoberta do Produto",	"Satisfação",	"O que mais gostou", "O que poderíamos melhorar",	"Recomendação", "Classificação Atendimento",	"Problemas com Produto",	"Resolução de Problemas"]).to_excel("challenge03.xlsx",index=False)

print("-" * 120)



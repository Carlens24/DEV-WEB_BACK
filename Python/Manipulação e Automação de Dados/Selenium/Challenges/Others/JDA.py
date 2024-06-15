# Importar módulos necessários
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as py
import time as t

# Inicializar o driver do Chrome
driver = webdriver.Chrome()
t.sleep(3)

# Abrir uma nova janela anônima
py.hotkey('ctrl', 'shift', 'n')
t.sleep(2)

# Mudar o controle para a nova janela
driver.switch_to.window(driver.window_handles[-1])

# Acessar a URL diretamente
driver.get('https://portal.jornadadoartista.com.br/users/sign_in')
t.sleep(3)

# JDA login
email = driver.find_element(By.XPATH, "//input[@class='form-control string sm:text-lg']").send_keys('carlensoslin@gmail.com')
senha = driver.find_element(By.XPATH, "//input[@class='form-control sm:text-lg']").send_keys('schneidine')
py.hotkey('enter')
t.sleep(5)

# Esperar até que o elemento do módulo esteja presente e clicar nele
try:
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@class='rounded-lg']")))
    modulo = driver.find_elements(By.XPATH, "//img[@class='rounded-lg']")[4]
    modulo.click()
    t.sleep(3)
except Exception as e:
    print(f"Um erro ocorreu ao clicar no módulo: {e}")

# Esperar até que os elementos das aulas estejam presentes e clicar no terceiro elemento
try:
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='lesson__title']")))
    aula = driver.find_elements(By.XPATH, "//a[@class='lesson__title']")[2]
    aula.click()
    t.sleep(5)
except Exception as e:
    print(f"Um erro ocorreu ao clicar na aula: {e}")

extensao = py.

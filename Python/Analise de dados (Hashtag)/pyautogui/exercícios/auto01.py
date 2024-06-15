from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/home/oslin/Documentos/webdrivers/chromedriver_linux64/chromedriver")
driver.get("https://www.google.com.br")
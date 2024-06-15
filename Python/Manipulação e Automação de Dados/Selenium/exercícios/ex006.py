from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://www.thesun.co.uk/sport/football/")

containers = navegador.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

for container in containers:
    title = container.find_element(by="xpath", value="./a/h2").text
    subtitle = container.find_element(by="xpath", value="./a/p").text

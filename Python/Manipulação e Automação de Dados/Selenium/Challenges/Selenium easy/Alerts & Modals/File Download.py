from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t

navegador = webdriver.Chrome()
navegador.get("https://demo.seleniumeasy.com/generate-file-to-download-demo.html")

navegador.find_element(By.ID, "textbox").send_keys("""In the vast digital universe, there existed a realm known as **CodeLand**. This realm was inhabited by various programming languages, each with its unique abilities and characteristics.

**Python**, the wise and friendly language, was known for its simplicity and readability. It was loved by beginners for its easy-to-understand syntax and by experts for its extensive libraries.

**Java**, the robust and reliable language, was the backbone of many large-scale systems. Its object-oriented nature and strong typing made it a favorite among enterprise developers.

**JavaScript**, the versatile and dynamic language, was the life of the web. It could be found in every corner of the internet, bringing interactivity to static web pages.

**C++**, the powerful and complex language, was respected and feared for its low-level capabilities. It was the language of choice for system-level programming and game development.

One day, a new language named **Rust** arrived in CodeLand. Rust was young and ambitious, promising memory safety without sacrificing performance. The other languages were intrigued and a bit apprehensive about this newcomer.

As time passed, Rust proved its worth and earned its place in CodeLand. It was adopted by developers for various projects, from operating systems to web servers.

The story of CodeLand is a testament to the diversity and evolution of programming languages. Each language has its strengths and weaknesses, and the choice of language depends on the problem at hand. The languages coexist and learn from each other, driving innovation and progress in the realm of CodeLand.
""")
t.sleep(5)

navegador.find_element(By.ID, "create").click()
t.sleep(5)

navegador.find_element(By.ID, "link-to-download").click()
t.sleep(6)

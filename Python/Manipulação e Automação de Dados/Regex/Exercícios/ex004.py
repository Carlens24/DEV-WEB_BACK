import re
texto = "Bem-vindo ao mundo do Python!"
palavras = re.findall(r'\\w+', texto)
print(palavras)

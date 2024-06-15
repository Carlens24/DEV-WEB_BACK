import re
# procurar a palavra "Python" na string
string = "Eu amo programar em Python!"
match = re.search("Python", string)

if match:
  print("Linguagem encontrado!!!!")
else:
  print("Linguagem não encontrado!!!!")

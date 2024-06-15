import re
# Vamos procurar a palavra "Python" na string
string = str(input("Digite a sua profissão: "))
match = re.search("programador", string)

if match:
  print("Profissão encontrado!")
else:
  print("Profissão não encontrado!")

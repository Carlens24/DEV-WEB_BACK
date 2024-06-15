import re

cpf = input("Digites seu email: ")
main = re.compile("[\w]+@[\w]+\.com")
x = re.fullmatch(main, cpf)
if x is None:
     print("Formato de email não aceito! (Tente novamente)")
else:
     print("Email registrado com sucesso!!")
print(x)

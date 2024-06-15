import re

senha = input("Digite a sua senha: ")
main = re.compile("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\W).{8,}$")
result = re.fullmatch(main, senha)
print(result)

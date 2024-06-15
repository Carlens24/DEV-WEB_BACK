import re

cpf = input("Digite seu cpf no padrão desejado / (000.000.000-00): ")
main = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}")
x = re.fullmatch(main, cpf)
if x is None:
    print("Formato de digitado não aceito!! (tente novamente)")
else:
    print("Formato de cpf digitado aceito!!!")
        
print(x)

# Leitura dos três números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Verificação
if numero1 > numero2 + numero3:
    print(f"{numero1} é maior que a soma de {numero2} e {numero3}.")
else:
    print(f"{numero1} não é maior que a soma de {numero2} e {numero3}.")

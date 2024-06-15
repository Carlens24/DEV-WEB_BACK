
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
meio = (numero1 + numero2 + numero3) - maior - menor
print("Os números em ordem decrescente são:", maior, meio, menor)
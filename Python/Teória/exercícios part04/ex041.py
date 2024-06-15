soma_pares = 0

print("Digite 4 números inteiros separados por espaço:")

entrada = input()
numeros = entrada.split()

for numero in numeros:
    if int(numero) % 2 == 0:
        soma_pares += int(numero)

print("A soma dos números pares é:", soma_pares)
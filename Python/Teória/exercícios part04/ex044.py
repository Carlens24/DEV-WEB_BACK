vLido = []
vPares = []
vImpares = []

for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    vLido.append(numero)

for numero in vLido:
    if numero % 2 == 0:
        vPares.append(numero)
    else:
        vImpares.append(numero)

print("vLido:", vLido)
print("vPares:", vPares)
print("vImpares:", vImpares)
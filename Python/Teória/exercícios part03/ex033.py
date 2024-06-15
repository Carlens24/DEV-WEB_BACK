numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

soma = sum(numeros)

media = soma / len(numeros)

print(f"A soma dos números é: {soma}")
print(f"A média aritmética dos números é: {media}")
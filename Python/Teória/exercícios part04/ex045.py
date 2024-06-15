vetor = []

for i in range(10):
    numero = int(input("Digite um número inteiro positivo: "))
    while numero <= 0:
        numero = int(input("Digite um número inteiro positivo: "))
    vetor.append(numero)

vetor = sorted(vetor, key=lambda x: x % 2 != 0)
print("Vetor antes da modificação:", vetor)
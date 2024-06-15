vetor = []

print("Digite 10 números inteiros separados por espaço:")

entrada = input()
numeros = entrada.split()

for numero in numeros:
    vetor.append(int(numero))

valor_maximo = max(vetor)
valor_minimo = min(vetor)
amplitude_amostral = valor_maximo - valor_minimo

print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("Amplitude amostral:", amplitude_amostral)
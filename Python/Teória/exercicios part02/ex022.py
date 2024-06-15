peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
soma = peso / (altura * altura)
print("De acordo com a altura", altura, "e peso", peso, "o IMC é", soma)
if soma >= 18.5 and soma <= 24.9:
    print("IMC é considerado normal")
elif soma >= 25:
    print("Peso acima da média")
else:
    print("Abaixo da média")
    while soma <= 25:
        peso = peso + 1
        soma = peso / (altura * altura)
    print(f"O peso maximo normal é {peso}")


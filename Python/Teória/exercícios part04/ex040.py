def calcular_soma_pares():
    soma = 0

    for _ in range(4):
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            soma += numero

    return soma

resultado = calcular_soma_pares()
print("A soma dos números pares é:", resultado)






     
     

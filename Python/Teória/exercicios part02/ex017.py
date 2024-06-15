contador = 0
while contador < 10:
    print("Contador = ", contador)
    contador = contador + 1


contador = 1
numero = int(input("Digite um valor para que possa ver a tabuada: "))
while contador <= 20:
    resultado = numero * contador
    print(contador, "x", numero, "=", resultado)
    contador = contador + 1
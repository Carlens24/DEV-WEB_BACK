"""
     for contador in range(10):
     print(contador)
"""
     

contador = 1
numero = int(input("Digite um valor para poder ver a tabuada: "))
while contador <= 10:
     
    resultado = numero * contador
    print(contador, "x", numero, "=", resultado)
    contador = contador + 1
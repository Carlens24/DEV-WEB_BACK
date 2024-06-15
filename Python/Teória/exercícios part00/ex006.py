# Repetições com uso do 'while'
'''
notas = []

contador = 1

while contador <= 5:
    codigo = input("Digite seu codigo: ")
    nota = float(input("Digite sua nota: "))
    resultado = [codigo, nota]
    notas.append(resultado)
    
    contador = contador + 1
    
    
    print ("A quantidade de notas: ", len(notas))
'''


# outro exemplo disso 
'''
contador = 10

while contador > 0:
    print(contador)
    contador -= 1
    
''' 

# O uso do 'breack' e 'continue'

contador = 0

while True:
    contador += 1
    
    
    if contador == 20:
        continue

    print(contador)

    if contador == 25:
        break
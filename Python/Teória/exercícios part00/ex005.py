# Repetições com uso do 'for'

notas = []
for x in range(4):
    nome = input ("Digite seu nome: ")
    codigo = input("Digite seu RNM: ")
    nota = float(input("Digite sua nota: "))
    resultado = [nome, codigo, nota]
    notas.append(resultado)
    

print ("Quantidade de notas: ", len(notas))

for n in notas:
    nome = n[0]
    codigo = n[1]
    nota = n[2]
    print("O aluno", nome, "Com o seguinte RNM", codigo, "tirou uma no de", nota)


# Repetições com uso do 'while'
"""
frutas = ["maça", "Uva", "Banana", 'Abacaxi']
for fruta in frutas:
    print(fruta)
"""
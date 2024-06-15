print("Tabela de Conversão: Polegadas para Centímetros")
print("----------------------------------------------")
print("Polegadas\tCentímetros")
print("----------------------------------------------")

for polegadas in range(1, 21):
    centimetros = polegadas * 2.54
    print(f"{polegadas}\t\t{centimetros:.2f}")
print("----------------------------------------------")
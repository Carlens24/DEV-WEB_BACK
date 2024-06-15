print("Tabela de Conversão: Metros para Milhas")
print("---------------------------------------")
print("Metros\t\tMilhas")
print("---------------------------------------")

for metros in range(20000, 160001, 10000):
    milhas = metros / 1609.344
    print(f"{metros} m\t\t{milhas:.3f} mi.")
print("---------------------------------------")
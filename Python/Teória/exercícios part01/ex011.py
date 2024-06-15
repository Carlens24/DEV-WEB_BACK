# Calculando o consumo médio 
# de acordo com a distancia percorrida 
# e a quantidade de combustivel gasto.
distancia = float(input("Digite a distância total em (KM): "))
combustivel = float(input("Digite a quantidade de combustível (Litros): "))
consumo_medio = int(distancia / combustivel)
print(f"O consumo médio foi de {consumo_medio}")

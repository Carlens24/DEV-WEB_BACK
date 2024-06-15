# A quantidade de latas de tintas 
# para pintar um tanque cilindro
altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

pi = 3.14159

area_base = pi * raio ** 2
area_lateral = 2 * pi * raio * altura
area_total = 2 * area_base + area_lateral

litros_tinta = area_total / 3
quantidade_latas = int(litros_tinta / 5) + 1
valor_total = quantidade_latas * 50

print("Quantidade de latas necessárias:", quantidade_latas)
print("Valor total em reais: R$", valor_total)
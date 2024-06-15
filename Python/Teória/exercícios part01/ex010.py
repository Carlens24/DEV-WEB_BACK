# O valor de um produto 
# e o calcule dele com parcelas e etc...
produto = float(input("Digite o valor do produto: "))
valor_vista = produto * 0.95
parcela_2x = produto / 2
parcela_3x_acrescimo = (produto * 1.05) / 3
print(f"o valor do produto a vista com 5% de desconto: {valor_vista}")
print(f"o valor com uma parcela em 2x {parcela_2x}" )
print(f"o valor com uma parcela em 3x, com acréscimo de 5% no valor total: {parcela_3x_acrescimo}")
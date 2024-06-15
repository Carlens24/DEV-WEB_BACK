# classe eleitoral

idade = float(input("Digite sua idade: "))
if idade > 16 and idade < 18 or idade > 65:
    print("Voto opcional")
elif idade >= 18 and idade < 65:
    print("o voto é obrigatório")
else:
    print("Não votante")
altura = float(input("Digite a sua altura: "))
genero = input("Digite seu gênero (M/F): ")
pm = (72.7 * altura) - 58
pf = (62.1 * altura) - 44.7
if genero == "masculino" :
    print(f"Peso ideal {pm}")
elif genero == "feminino" :
    print(f"Peso ideal Feminino {pf}")
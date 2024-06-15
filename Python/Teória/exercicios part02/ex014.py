# Carteira de motorista

ano = int(input("Digite o ano em que nasceu: "))
idade = 2023 - ano
if idade >= 18:
    print("Já pode fazer a carteira de motorista!!!!")
else:
    print("Não é permitido!!!")
print(f"Em 2025 você terá {idade} anos de idade")

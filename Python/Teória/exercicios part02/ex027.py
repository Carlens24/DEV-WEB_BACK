print("--------------------------------------------------------------------------------------------------")
print("opção 1 - à vista  \t opção 2 - 2 parcelas \t opção 3 - 3 parcelas \t opção 4 - 4 parcelas")
print("--------------------------------------------------------------------------------------------------")
opcao = int(input("Digite a sua opção: "))
preco = float(input("Digite o valor: "))
calc1 = preco - (preco * 0.08) 
calc2 = (preco - (preco * 0.04)) / 2
calc3 = preco / 3
calc4 = (preco + (preco * 0.04)) / 4
if opcao == 1:
     print(calc1)
elif opcao == 2:
     print(calc2)  
elif opcao == 3:
     print(calc3)
elif opcao == 4:
     print(calc4)
     
     
fluxo_caixa = []

print("-----------------")
print("Fluxo de caixa")
print("-----------------")
print("1- Adicionar receita")
print("2- Adicionar despessa")
print("/n# Digite outro numero para encerrar #n/")


def adicionar_transacao():
    nome = input("Nome: ")
    valor = float(input("valor: "))
    fluxo_caixa.append({
    "nome": nome,
    "valor": valor
    })
    
while True:
        
        opcao = int(input("Digite a opção entre 1 e 2: "))
        
        if opcao == 1:
            adicionar_transacao()
        elif opcao == 2:
            adicionar_transacao()
        else: 
            break
        
        
total = 0
for fc in fluxo_caixa:
    print("Nome", fc['nome'], ", valor: R$", fc['valor'])
    total = total + fc['valor']
        
print("Saldo atual: R$", total)    
        

        
        
        
        
        
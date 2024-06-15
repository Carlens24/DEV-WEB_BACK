# Basíco de 'FUNÇÔES'
'''
def minha_funcao(valor1, valor2): 
    return valor1 + valor2

resposta = minha_funcao(90, 10)

print("resposta", resposta)

'''

# Outro exemplo

def minha_funcao(valor1, valor2): 
    return valor1 + valor2

while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))
    
    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)
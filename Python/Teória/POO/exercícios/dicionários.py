# dicionários 01
conta = {}
conta["Numero"] = "10239045-5"
conta["Titular"] = "Oslin"
conta["Saldo"] = "12.000"
conta["Limite"] = "22.0000"

print(f"O titular da conta {conta["Numero"]} é {conta["Titular"]}")

# dicionários 02 
conta1 = {"numero":"10239054-5", 
          "titular":"Carlens",
          "saldo":"12.000", 
          "limite":"22.000"}
print(conta1)
# Uso do dict
conta2 = dict(numero="33686454-5",
              titular="Schneidine",
              saldo="55.000",
              limite="55.000" )
print(conta2)


# dicionários 03 - exercício 02
conta3 = dict(numero="95642353-9",
              titular="Darley",
              saldo="10.000",
              limite="1.000" )
print(conta3)

# dicionário 04
'''
def depositar(conta, valor):
     conta["saldo"] += valor
     
def sacar(conta, valor):
     conta["saldo"] -= valor 
     
depositar(conta1,200)    
print(conta1["saldo"])
depositar(conta2,600)
print(conta2["saldo"])    
sacar(conta1,1000)
print(conta["sacar"]) 
'''
# dicionário 05 - exercício 03
'''
def transferir(transfere, receber, valor):
     transfere["saldo"] -= valor
     receber["saldo"] += valor 
     
transferir(conta1, conta2, 6000)
print(f"O saldo da conta {conta1['numero']} é {conta1['saldo']}")
print(f"O saldo da conta {conta2['numero']} é {conta2['saldo']}")
'''


# dicionário 06 - exercício 04
def extrato(conta, saldo):
     print(f"O saldo da conta {conta} é {saldo}")
extrato("235678-6", 12_000)     
     




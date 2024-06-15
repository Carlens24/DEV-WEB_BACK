from banco import Banco

# Instanciando o banco
meu_banco = Banco(nome="Banco XYZ", codigo="123")

# Criando contas
conta1 = meu_banco.cria_conta("João")
conta2 = meu_banco.cria_conta("Maria", saldo=1000)

# Listando contas
print("Lista de Contas:")
meu_banco.lista_contas()

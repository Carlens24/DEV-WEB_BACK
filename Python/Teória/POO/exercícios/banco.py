from conta import Conta

class Banco:
    def __init__(self, nome, codigo):
        self.__nome = nome
        self.__codigo = codigo
        self.__contas = []

    def cria_conta(self, titular, saldo=0):
        nova_conta = Conta(titular, saldo)
        self.__contas.append(nova_conta)
        return nova_conta

    def lista_contas(self):
        for i, conta in enumerate(self.__contas, start=1):
            print(f"Conta {i}:")
            conta.extrato()
            print("-------------------------")

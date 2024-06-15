class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        self.transacoes = []

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -{valor}")
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +{valor}")
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def extrato(self):
        print(f"Extrato da conta de {self.nome_titular}:")
        print(f"Saldo: R${self.saldo}")
        print("Transações:")
        for transacao in self.transacoes:
            print(transacao)

# Exemplo de uso
conta = ContaBancaria("João", 1000)

conta.saque(500)
conta.extrato()

conta.deposito(200)
conta.extrato()

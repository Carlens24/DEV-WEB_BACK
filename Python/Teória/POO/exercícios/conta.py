class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

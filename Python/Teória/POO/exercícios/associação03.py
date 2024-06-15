# exercício 02 
import datetime

class Transacao:
    def __init__(self, tipo, valor):
        self.__horario = datetime.datetime.now()
        self.__tipo = tipo
        self.__valor = valor

    def get_detalhes(self):
        return {'Horário': self.__horario, 'Tipo': self.__tipo, 'Valor': self.__valor}


class Historico:
    def __init__(self):
        self.__transacoes = []

    def adicionar(self, transacao):
        self.__transacoes.append(transacao)

    def get_transacoes(self):
        return [transacao.get_detalhes() for transacao in self.__transacoes]


class Conta:
    def __init__(self, cliente, gerente):
        self.__cliente = cliente
        self.__gerente = gerente
        self.__historico = Historico()

    def get_cliente(self):
        return self.__cliente

    def get_gerente(self):
        return self.__gerente

    def get_historico(self):
        return self.__historico

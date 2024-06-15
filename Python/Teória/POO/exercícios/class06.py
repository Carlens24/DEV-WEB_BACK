class Escritor:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def Escrever(self):
        print("A caneta esta escrevendo")


class MaquinaEscrever:
    def escrever(self):
        print("A Maquina esta escrevendo")

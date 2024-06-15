# Permite que certas características ou
# propriedades dos objetos de uma classe não
# possam ser vistas ou modificadas externamente
# Ocultam-se as características internas do objeto.

# Encapsulamentos - public, protected, private
# _ weak private or protected - "Não pode ser acessado de fora da classe" mas de for dentro tá otimo
# ou seja é mais ou menos publico
# __ strong private - "atributo não pode ser acesado de jeito nenhum"
# mas dá pra acessar desta maneira " _NomeClase__NomeAtributo" fora da classe

class BaseDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if "Clientes" not in self.__dados:
            self.__dados["Clientes"] = {id: nome}
        else:
            self.__dados["Clientes"].update({id: nome})

    def lista_Clientes(self):
        for id, nome in self.__dados["Clientes"].items():
            print(id, nome)

    def apaga_Clientes(self, id):
        del self.__dados["Clientes"][id]

bd = BaseDados()
bd.inserir_cliente(2, "carlinhos")
bd.inserir_cliente(3, "Zé ganço")
bd.inserir_cliente(33, "Grilo seco")
bd.lista_Clientes()

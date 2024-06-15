from typing import Type
class Interuptor:
     def __init__(self, comodo:str):
          self.__comodo = comodo
          
     def acender(self):
          print("Acendendo {}".format(self.__comodo))
     
     
     def apagar(self):
          print("Apagando {}".format(self.__comodo))


class Pessoa:
     def acender_luz(self, interuptor: Type[Interuptor]):
          interuptor.acender()
          
     def apagar_luz(self, interuptor: Type[Interuptor]):
          interuptor.apagar()
          
     def dormir(self):
          print("Fui dormir...")     
          
oslin = Pessoa()
interuptor_banheiro = Interuptor("O banheiro") 
interuptor_cozinha = Interuptor("A cozinha") 
interuptor_quarto = Interuptor("O quarto") 


interuptor_quarto.acender()
oslin.acender_luz(interuptor_banheiro)
oslin.acender_luz(interuptor_cozinha)
oslin.apagar_luz(interuptor_quarto)
oslin.dormir()
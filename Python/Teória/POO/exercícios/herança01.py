class Pessoa:
     def __init__(self, nome, idade, genero):
          self.nome = nome
          self.idade = idade
          self.genero = genero
          self.nomeclasse = self.__class__.__name__
          
     def falar(self):
           print(f"{self.nomeclasse} falando..!!!")    
         
class Cliente(Pessoa):  
     def Comprar(self):              
          print(f"{self.nomeclasse} Comprando..!!!")

class Vendedor(Pessoa):  
     def Vender(self):              
          print(f"{self.nomeclasse} Vendendo..!!!")
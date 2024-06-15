# O uso do @staticmethod e a difernca de com o @staticmethod
'''

class Usuario:
     cargo = "Usuario"
     
     def __init__(self, nome, idade, altura):
          self.altura = altura
          
     @staticmethod
     def e_adulto(idade):
          if idade >= 18:
               print(True)
          else:
               print(False) 
                
Usuario.e_adulto(22)

'''

class Usuario:
     cargo = "Usuario"
     
     def __init__(self, nome, idade, altura):
          self.altura = altura
          
     @classmethod
     def teste(cls):
         return 1
    
     @staticmethod
     def e_adulto(idade):
         cls.teste()
         print(self.altura)

Usuario.e_adulto(12) 
                  
          
          
# O uso do "@classmethod" e a difernca de com o "@staticmethod""

class Usuario:
     cargo = "Usuario"
     
     def __init__(self, nome, idade, altura):
          self.altura = altura
          
     @classmethod
     def cargo_usuario(cls):
          cls.cargo = "Gerente"
          print(cls.cargo)
          
          
          
          
Usuario.cargo_usuario()
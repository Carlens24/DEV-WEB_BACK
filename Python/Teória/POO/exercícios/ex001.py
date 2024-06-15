# BASISO DE ORIENTAÇÕES A OBJETOS CLASSES
# SEM O USO DO "__INIT__"

'''

class Usuario:
     cargo = "Usuario"
     
     def logar(self):
          print("Logado com sucesso!!!")
   
     def sair(self):
          print("Saido com sucesso!!!")     

          
usuario1 = Usuario()
usuario2 = Usuario()

usuario1.logar()
usuario2.sair()

'''
# Com o udo do "__init__" nas classes 
class Usuario:
     cargo = "Gerente"
     
     def __init__(self, nome, idade, altura):
         self.altura = altura
    
     def retorna_altura(self):
          print(self.altura)
     
     
     def exibe_cargo(cls):
          print(cls.cargo)
          
          
usuario1 = Usuario("Carlens", "15", "189")

usuario2 = Usuario("Schneidine", "17", "160")

Usuario.cargo = "Gerente"

usuario1.exibe_cargo()
usuario2.exibe_cargo()

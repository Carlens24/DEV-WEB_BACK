# Exercício 01
class Cliente:
     def __init__(self, nome, cpf, mail):
          self.__nome = nome
          self.__cpf = cpf
          self.__mail = mail
          
     def get_nome(self):
        return self.__nome

     def get_cpf(self):
        return self.__cpf

     def get_email(self):
        return self.__mail   
                   
                   
class Gerente:
     def __init__(self, nome, cpf, mail):
          self.__nome = nome
          self.__cpf = cpf  
          self.__mail = mail  
                       
                       
     def get_nome(self):
          return self.__nome
     
     def get__cpf(self):
          return self.__cpf 
     
     def get__mail(self):
          return self.__mail                 
     
     
class Conta:
     def __init__(self, Cliente, Gerente):
         self.__Cliente = Cliente
         self.__Gerente = Gerente    

     
     def get_cliente(self):
          return self.__Cliente
     
     def get__gerente(self):
          return self.__Gerente 

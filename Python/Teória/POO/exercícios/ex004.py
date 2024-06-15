# Herança de classes
class pessoa:
     
     def __init__(self, nome, cpf, email):
          self.nome = nome
          self.cpf = cpf
          self.email = email
     

class secretaria(pessoa):
     def __init__(self, id, nome, cpf, email):
          super().__init__(nome, cpf, email)
          self.id = id
          
          
class vendedor(pessoa):
     def __init__(self, vendas, nome, cpf, email):
          super(pessoa).__init__(nome, cpf, email)
          self.vendas = vendas 
          
s1 = secretaria("4593575663", "douglas", "800.344.677-78", "dou@gmail.com")
v1 = vendedor("oslin", "000.944.765-08", "oslin@gmail.com")


s1.email
print(s1())     
# classes 00
class bolo():
     pass
bolo = bolo()

# classes 01
class classe():
     text: str
     boleano: bool
     float: float
     inteiro: int
Classe = classe()

Classe.text = "Olá, Mundo"
Classe.boleano = True
Classe.inteiro = 22
Classe.decimal = 2.10

# classes 02
class curso():
     nome: str
     data: str
     professor: str
     horas: int
     valor: float
     
Curso = curso()

Curso.nome = "Oslin"
Curso.data = "25/01/2024"
Curso.professor = "Miranda"
Curso.horas = "24hrs"
Curso.valor = "12.000"


#  numero, titular, saldo, limite, ativa
# classes exercício 01
class conta():
     
     def __init__(self, numero, titular, saldo, limite, ativa):
          self.numero =  numero
          self.titular =  titular
          self.saldo =  saldo
          self.limite =  limite
          self.ativa =  ativa
          
contas = conta()   
contas.numero = "2234567-9"
contas.titular = "oslin"
contas.saldo = "344.00"
contas.limite = "22.000"
contas.ativa = "0$R"
       
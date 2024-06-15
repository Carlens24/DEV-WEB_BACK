# função 01
def imprimir(nome):
     print(f"Olá, {nome}!!!")
     
imprimir("Carlens oslin")
imprimir("João")
imprimir("Mamadou")

# função 02
def horarios(disciplina="Programação", horario="13h30 ás 15h30"):
     print(f"O horário da disciplina '{disciplina}' é {horario}")
     
horarios()
horarios("Arte", "6h00 ás 12h30")   

# função 03
def matricula(curso="", disciplina="", periodo=0): 
     print(f"Realizando a matricula \n"
          f"\t- curso: {curso}\n"
          f"\t- disciplina: {disciplina}\n"
          f"\t- periodo: {periodo}")
          
matricula("ciência da computação", "RA", 2)
matricula(disciplina="RA", periodo="2", curso="Arte")

#função 04
def maior_30(*args):
     print(args)
     for num in args:
          if num > 30:
               print(num)
maior_30(10,20,30,40,50,60)               
               

def dadosPessoais(**kwargs):
     print(type(kwargs))
     for chave, valor in kwargs.items():
          print(f"{chave}: {valor}")
          
dadosPessoais(nome='João', idade=35, carreira='Professor Auxiliar')

# função 05
def operacao(val1, val2, operador):
     match(operador):
          case"+": return val1 + val2
          case"-": return val1 - val2
          case"*": return val2 * val2
          case"/": return val2 / val2
          case"_": return "operador inválido"    
valor = operacao(1,45, "/")
print(valor)
     
     
# função 06
def ValorMedia(valor1, valor2):
        soma = valor1 + valor2
        media = (valor1 + valor2)/2
        return soma, media
        
valor = ValorMedia(12, 22)
print(valor)
valorSoma, ValorMedia = ValorMedia(12, 22)
print(valorSoma, ValorMedia)


# funcao 07 
def myFunction():
     """ Do nothing, but document it.
     No, really, it doesn't do anything."""
     pass
print(myFunction.__doc__)

# funcao 08
def f(nome: str, cep: str="00000000")->str:
     print("Annotations: ",f.__annotations__)
     print("Argumentos: ", nome, cep)
     return nome + "e" + cep
f("Carlens")
print(valor)



import random
from random import choice

nomes = [
  "Aline Sarah Freitas de Andrade",
  "Cesar Cunha Ziobro",
  "Fernando Dias Ferreira",
  "Gabriel Ernesto Barboza Pereira",
  "Lucas Kreutzer de Jesus",
  "Matheus Henrique Rosa",
  "Rafael Schmitz Herdt",
  "Thiago Krügel",
  "Vitor Bianchini de Quadros",
  "Pedro Henrique Pichorz",
  "João Vitor Brandão",
  "Karen Ubial Pereira",
  "Antonio David Viniski",
  "Carlens Oslin"
]

escolhido = random.choice(nomes)
print(f"A pessoa escolhida como vencedora do sorteio é '{escolhido}'") 


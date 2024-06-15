#  Estruturas de Dados Principais
import pandas
import pandas as pd

# Linha unica
s = pd.Series(['Ana', 'daniel', 'samuel', 'rodrigo'])
#print(s)

# Table
data = {
    'nome': ['Rose', 'Ana', 'Rodrigo', 'Schneidine', 'Daniel'],
    'idades': [46, 19, 22, 18, 55],
    'filmes_favoritos': ['King Kong', 'Planeta dos macacos', 'Meu malvado favorito',
                         'Alice no paíse das maravilhas', 'The end']
}

df = pd.DataFrame(data)
# print(df)

# Leityra de dados

# CSV
file = pd.read_csv('file.csv')
# print(file)

data2 = {
    'id': [1, 2, 3, 4],
    'país': ['Brasil', 'Venezuela', 'Cuba', 'Haiti'],
    'população': ['203M', '28,30M', '11,21M', '11,58M']
}






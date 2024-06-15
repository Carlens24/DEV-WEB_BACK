# Documentação do - REGEX

# Identificação de padrões
# [] - um conjunto isolado de padrões definidos
# . - Entende qualquer valor exceto uma nova linha
# \. - Para buscar o caracter "."
# ^ - Irá testar o início da string
# $ - Irá testar o final da string
# [^] -Irá considerar todos os caracteres EXCETO o indicado
# \d - Qualquer caracter que SEJA um algarismo  de 0 a 9
# \D - Qualquer caracter que NÃO SEJA um algarismo de 0 a 9
# \s - Qualquer caracter que SEJA vazio
# \S - Qualquer caracter que NÃO SEJA vazio
# \w - Qualquer caracter que SEJA alfanumérico
# \W - Qualquer caracter que NÃO SEJA Alfanumérico

# Metodos do REGEX
'''

    re.match(pattern, string):
        Retorna um objeto de correspondência se o padrão ocorrer no início da string, senão retorna None.

    re.search(pattern, string):
        Retorna um objeto de correspondência se o padrão ocorrer em qualquer lugar da string, senão retorna None.

    re.findall(pattern, string):
        Retorna uma lista de todas as ocorrências não sobrepostas do padrão na string.

    re.finditer(pattern, string):
        Retorna um iterador de objetos de correspondência para todas as ocorrências não sobrepostas do padrão na string.

    re.sub(pattern, replacement, string):
        Substitui todas as ocorrências do padrão na string pelo texto de substituição e retorna a nova string resultante.

'''


# Repetição de padrão
# + Uma ou mais vezes
# * 0 ou mais
# ? 0 ou 1
# {x} x vezes
# {z, y} z minimo y maximo
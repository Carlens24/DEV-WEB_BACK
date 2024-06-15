# ^ - Irá testar o início da string
# ou seja uma string que comece com "a" e mais 6 carateres 
import re
txt = "ashborn"
pattern = re.compile("^a......")
x = re.fullmatch(pattern, txt)
print(x)


# $ - Irá testar o final da string
# A string tem que ter 3 caracteres e terminar com "n"
import re
txt = "born"
pattern = re.compile("...n$")
x = re.fullmatch(pattern, txt)
print(x)

# [^] -Irá considerar todos os caracteres EXCETO o indicado
# a strig terá que ser diferente de "o"
import re
txt = "Carlens baba Anha Marta"
pattern = re.compile("[^o]")
x = re.findall(pattern, txt)
print(x)

# \w - Qualquer caracter que SEJA alfanumérico - (Letras e numeros)
import re
txt = "Carlens344 #"
pattern = re.compile("\w")
x = re.findall(pattern, txt)
print(x)

# \W - Qualquer caracter que NÃO SEJA Alfanumérico - (Letras e numeros)
import re
txt = "Carlens344 #"
pattern = re.compile("\W")
x = re.findall(pattern, txt)
print(x)
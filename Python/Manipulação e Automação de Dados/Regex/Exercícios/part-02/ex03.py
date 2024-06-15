# \d - Qualquer caracter que SEJA um algarismo  de 0 a 9
import re
txt = "2 5"
pattern = re.compile("\d")
x = re.findall(pattern, txt)
print(x)

# \D - Qualquer caracter que NÃO SEJA um algarismo de 0 a 9
import re
txt = "2.5cm"
pattern = re.compile("\D")
x = re.findall(pattern, txt)
print(x)
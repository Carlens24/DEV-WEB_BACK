# \s - Qualquer caracter que SEJA vazio
# Ou seja o espaço entre carlens e 344
import re
txt = "Carlens344 #"
pattern = re.compile("\s")
x = re.findall(pattern, txt)
print(x)

# \S - Qualquer caracter que NÃO SEJA vazio
import re
txt = "Carlens344 #"
pattern = re.compile("\S")
x = re.findall(pattern, txt)
print(x)
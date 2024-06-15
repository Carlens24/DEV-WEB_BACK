# [] Conjunto separado
# De a-z minusculo
# De A-Z maiusculo
# De 0-10
import re
txt = "Carlens Oslin 8"
pattern = re.compile("[a-zA-Z0-9]")
x = re.findall(pattern, txt)
print(x)
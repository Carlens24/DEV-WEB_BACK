# Uso do método de "fullmatch"
# . - Entende qualquer valor exceto uma nova linha
import re
txt = "arara"
pattern = re.compile("ar...")
x = re.fullmatch(pattern, txt)
print(x)

# \. - Para buscar o caracter "."
import re
txt = "arara."
pattern = re.compile("ar...\.")
x = re.fullmatch(pattern, txt)
print(x)

# Uso do metodo "search"
import re
txt = "Hoje eu encontrei um belo arara"
pattern = re.compile("arara")
x = re.search(pattern, txt)
print(x)


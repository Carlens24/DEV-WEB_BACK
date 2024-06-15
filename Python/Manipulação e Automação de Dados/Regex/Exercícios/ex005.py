import re
# email
string = "Carlensoslin@gmail.com.br"
pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com\.[a-zA-Z]{0,3}")
x = re.fullmatch(pattern, string)
print(x)
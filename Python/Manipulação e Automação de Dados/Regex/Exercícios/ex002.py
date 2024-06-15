import re
# cpf
cpf = "900.800.899-00"
padrao = re.compile("[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}")
 
result = re.findall(padrao, cpf)
print(result)

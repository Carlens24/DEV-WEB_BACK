# Condição simples
# Com somente o uso do 'if' e 'else'

idade = int( input("Digite a sua idade: "))

if idade >= 18:
    print("Permitido a entrar")
else:
    print("Não permido a entrar")
    


# Vou chamar este de condição composto
# Por causa do uso do 'if', 'else' e 'elif'
# Não esquecendo do uso do 'and'

salario = float(input("Digite seu salario: ") )

if salario <= 3000:
    print ("Programador Jûnior")
elif salario > 3000 and 6000:
    print ("Programador plenor")
elif salario > 6000 and 15000:
    print ("Programador Sênior")
else: ("Gerente de projetos")
     
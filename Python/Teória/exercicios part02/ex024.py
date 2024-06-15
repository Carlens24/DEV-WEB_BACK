numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
if numero1 >= numero2 and numero1 >= numero3:
    maior_numero = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior_numero = numero2
else:
    maior_numero = numero3
print("O maior número é:", maior_numero)
def verificar_triangular(n):
    i = 1
    while i * (i + 1) * (i + 2) < n:
        i += 1
    if i * (i + 1) * (i + 2) == n:
        return True
    else:
        return False

numero = int(input("Digite um número não-negativo: "))

if verificar_triangular(numero):
    print(numero, "é um número triangular.")
else:
    print(numero, "não é um número triangular.")
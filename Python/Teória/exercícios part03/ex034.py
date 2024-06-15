li = int(input("Informe o limite inicial: "))
lf = int(input("Informe o limite final: "))

if li % 3 != 0:
    li = li + (3 - li % 3)

print("Números múltiplos de 3 entre", li, "e", lf, ":")
while li < lf:
    print(li)
    li = li + 3
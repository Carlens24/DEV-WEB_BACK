minutos = int(input("Digite a quantidade de minutos usados: "))
if minutos <= 60:
    valor = 8.00
    mensagem = "Valor mínimo, R$ 8,00"
else:
    horas = minutos // 60
    minutos_restantes = minutos % 60

    valor = 8.00 + (horas - 1) * 4.00  
    valor += minutos_restantes // 15 * 1.50  

    mensagem = "Valor fracionado, R$ {:.2f}".format(valor)
print(mensagem)
# Testando a função datetime em calculo de idade

import datetime
idade = int(input("Digite o ano em que vc nasceu: "))
data_atual = datetime.date.today().year
idade_atual = data_atual - idade
print("Atualmente vc tem ou terá",idade_atual,"anos de idade")




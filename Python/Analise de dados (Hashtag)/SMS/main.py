# Logíca do projeto
# Importando e visualisando os dados
# Verificando se algum valor na coluna de venda do arquivo é maior que 55.000
# Se for maior que 55.000 --> enviar um "SMS" no celular
# Com nome, mês e as vendas do vencedor
# Caso não for 55.000 não precisa fazer nada

import pandas as pd
import openpyxl as op
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACa5ffb96f333ec94d51de5db5360534f7"
auth_token = "995692d9ef04f339f4a41e7c27cd376f"
client = Client(account_sid, auth_token)

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in lista_meses:
  tabela_vendas = pd.read_excel(f"{mes}.xlsx")
  if (tabela_vendas["Vendas"] > 55000).any():
    vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
    vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas", ].values[0]
    print(f"No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas} ")
    message = client.messages.create(
        to="+5541998576674",
        from_="+12018906646",
        body=f"No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}")
    print(message.sid)


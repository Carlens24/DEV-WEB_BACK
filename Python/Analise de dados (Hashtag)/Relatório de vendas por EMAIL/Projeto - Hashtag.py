import pandas as pd
import win32com.client as win32


# Importando as bases de dados que é a "tabela_vendas"
tabela_vendas = pd.read_excel(r"C:\Users\carlens.oslin\Documents\Projetos de analise de dados\Relatório de vendas por EMAIL\Vendas.xlsx")

# Visualizar a base de dados sem nenhuma exeção
pd.set_option("display.max_columns", None)
print(tabela_vendas)
print("-" * 150)

# Faturamento por loja
# Agrupamento da coluna de "ID Loja" e a soma dos valores da coluna "Valor Final"
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento)
print("-" * 150)

# Quantidade vendida por loja
'''
quantidade_loja = tabela_vendas[["Produto", "Quantidade"]].groupby("Produto").sum()
print(quantidade_loja)
'''

quantidade_loja = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade_loja)
print("-" * 150)

# Ticket médio em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade_loja['Quantidade']).to_frame()
print(ticket_medio)
ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"})
print("-" * 150)

# Envio do relátorio por email
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'carlensoslin@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>
 
<p>Segue o relatório de vendas por cada loja em forma de tabela</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={"Valor Final": "R${:,.2f}".format})}

<p>Quantidade Vendida por cada loja:</p>
{quantidade_loja.to_html()}

<p>Ticket médio dos produtos em cada loja:</p>
{ticket_medio.to_html(formatters={"Ticket Médio": "R${:,.2f}".format})}

<p>Qualquer dúvida estou a disposição.</p>
<p>Att  ...</p>
<p>Carlens Oslin</p>
'''
mail.Send()
print("email_enviado")



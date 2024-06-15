import pandas as pd

tabela = pd.read_html("https://br.investing.com/currencies/exchange-rates-table")
print(tabela)
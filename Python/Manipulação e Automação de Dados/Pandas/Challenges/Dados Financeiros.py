import pandas as pd

print("-" * 90)
print("\tBOLSA DE VALORES \n\tBVSP BOVESPA IND")

table = pd.read_html("https://economia.uol.com.br/cotacoes/bolsas/")
print(f"""Mais altas  \n{table[1]}\n
          Mais baixas  \n{table[2]}\n
          Mais negociados  \n{table[3]}\n""")

save = pd.DataFrame(table)
save.to_excel('Análise de dados finançeiros.xlsx', index=False)  

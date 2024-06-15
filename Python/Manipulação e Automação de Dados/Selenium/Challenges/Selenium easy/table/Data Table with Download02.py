import pandas as pd

table = pd.read_html("https://demo.seleniumeasy.com/table-data-download-demo.html")
print(table)
table[0].to_excel("table02.xlsx")
import pandas as pd

file = pd.read_excel(r"C:\Users\carlens.oslin\Documents\Python\Selenium\exercícios\extracts.xls")
rename = file.rename(columns={"Sexo e finalidade do acesso à Internet":"Sexo e finalidade de acesso",
                           "2008":"Ano de 2008"}, inplace=True)
print(rename)
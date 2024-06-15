import pandas as pd

venda_df = {
    "data": ["13/02/2024", "20/02/2024", "25/02/2024",
            "03/03/2024", "10/03/2024", "17/03/2024"],
    "valor": [500, 300, 450, 600, 250,400],
    "produto": ["feijão", "arroz", "macarrão", "açúcar", "farinha", "óleo"],
    "Qtde": [50, 70, 40, 60, 30, 45]
}

data_frame01 = pd.DataFrame(venda_df)

data_frame02 = pd.read_excel("Vendas.xlsx")
print(data_frame02)

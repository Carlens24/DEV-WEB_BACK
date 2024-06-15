produtos = ["BanaNa", "abAcaXI", "MaMãO", "bArBoSa", "GriLHO"]

def tratar_texto (texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto


texto = "BanaNa"
texto = tratar_texto(texto)
print(texto)

for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)

print(produtos)
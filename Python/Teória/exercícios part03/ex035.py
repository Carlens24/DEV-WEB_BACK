# Definição das cotações e comissões
cotacoes = {
    'USD': 5.25,  
    'GBP': 6.10,   
    'EUR': 5.80    
}

comissao_menor_1000 = 0.05  
comissao_maior_1000 = 0.03   

codigo_moeda = input("Digite o código da moeda (USD, GBP ou EUR): ").upper()
montante = float(input("Digite o montante a ser adquirido: "))

# Cálculo do valor em reais
cotacao = cotacoes.get(codigo_moeda)
if cotacao:
    valor_reais = montante * cotacao
   
    if valor_reais < 1000:
        comissao = valor_reais * comissao_menor_1000
    else:
        comissao = valor_reais * comissao_maior_1000
   
    valor_total = valor_reais + comissao
   
    print("Valor a ser pago em reais: R$", valor_total)
else:
    print("Código de moeda inválido. Por favor, tente novamente.")
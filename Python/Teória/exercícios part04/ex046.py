def gerar_aposta():
    aposta = []
    numero = 1
    while len(aposta) < 6:
        aposta.append(numero)
        numero += 1
        if numero > 60:
            numero = 1
    return aposta

def obter_aposta_usuario():
    aposta = []
    while len(aposta) < 6:
        numero = int(input("Digite um número entre 1 e 60: "))
        if numero < 1 or numero > 60:
            print("Número inválido. Tente novamente.")
        elif numero in aposta:
            print("Número repetido. Tente novamente.")
        else:
            aposta.append(numero)
    return sorted(aposta)

def verificar_acertos(aposta_gerada, aposta_usuario):
    acertos = 0
    for numero in aposta_usuario:
        if numero in aposta_gerada:
            acertos += 1
    return acertos

aposta_gerada = gerar_aposta()
print("Aposta gerada:", aposta_gerada)

aposta_usuario = obter_aposta_usuario()
print("Sua aposta:", aposta_usuario)

num_acertos = verificar_acertos(aposta_gerada, aposta_usuario)
print("Número de acertos:", num_acertos)
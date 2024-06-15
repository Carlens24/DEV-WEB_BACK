from random import choice

while True:
    try:
        n = int(input('Desejas inserir quantos nomes no sorteio? '))
        if n <= 1:
            print('\033[31mValor INVÁLIDO! Digite valores maiores que "1"!\033[m')
        else:
            break
    except:
        print('\033[31mValor INVÁLIDO! Digite apenas números inteiros!\033[m')

nomes = list()
for c in range(1, n + 1):
    nome = input(f'Digite o {c}º nome: ')
    nomes.append(nome)

sorteado = choice(nomes)
print(f'\033[32mO nome sorteado é: {sorteado}\033[m')
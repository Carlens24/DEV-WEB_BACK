def selecao_direta(vetor):
    n = len(vetor)
    
    for i in range(n - 1):
        # Encontrar o índice do menor elemento no resto do vetor
        indice_menor = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_menor]:
                indice_menor = j
        
        # Trocar o elemento encontrado com o primeiro elemento não ordenado
        vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]

# Função para exibir o vetor
def exibir_vetor(vetor):
    for elemento in vetor:
        print(elemento, end=' ')
    print()

# Leitura do vetor de 20 posições
vetor = []
for i in range(20):
    valor = int(input(f"Digite o valor para a posição {i + 1}: "))
    vetor.append(valor)

# Chama a função de ordenação por seleção direta
selecao_direta(vetor)

# Exibe o vetor ordenado
print("Vetor ordenado:")
exibir_vetor(vetor)

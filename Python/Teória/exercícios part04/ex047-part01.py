n = [int(input("Digite um numero: ")) for _ in range (5)]
contador = 0
index = 0
atual = 0
print(n)
while contador <= len(n) - 1:
     menor = 999
     for numero in range(contador, len(n)):
          if n[numero] < menor:
               menor = n[numero]  
               index = numero 
               atual = n[contador]      
     n[contador] = menor
     n[index] = atual
     contador += 1
print(n)

               
print("--------------------------------------------------------------------------------------------------")
print("Peso pessado \t\t cruzador \t\t meio-pesado \t\t super-médio")
print("--------------------------------------------------------------------------------------------------")
massa = float(input("Digite a sua massa corporal (KG): "))
massalb = massa * 2.20462262 
if massalb > 161 and massalb < 168:
     print("Super médio") 
elif massalb > 169 and massalb < 175:
     print("Meio pesado")
elif massalb > 176 and massalb < 200:
     print("Cruzador")
elif massalb >= 201 :
     print("super pesado")
else:
       print("Categoria inferior a Super-médio")   
          
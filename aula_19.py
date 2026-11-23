distancia = int(input("Determine a distancia em km ")) 

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f"Preço de passagem é {preço} ")        
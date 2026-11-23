velocidade = int(input("Qual é a velocidade do carro (km/h?) "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5

    print("Foi multado")
    print(f"Valor de multa: €, {multa}")
else:
    print("Nao foi multado ")    
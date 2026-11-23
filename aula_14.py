nome = input("Qual é o seu nome ")
idade = int(input("Qual é a sua idade "))

if idade < 18:
    print(f"{nome},voce nao pode derigir nem beber ")
elif idade> 18 <= 65:
    print(f"{nome},bebida liberada! So nao vale dirigir ")
else: 
    print(f"{nome},beba com muita moderaçao ")
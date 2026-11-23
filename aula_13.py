aluguel = int(input("Qual é o valor de aluguel"))
energia = int(input("Qual é o valor de energia"))
agua = int(input("Qual é valor de agua"))
gas = int(input("Qual é valor de gas"))
internet = int(input("Qual é valor de internet"))
combustivel = int(input("Qual é valor de combustivel"))
alimentos = int(input("Qual é valor de alimentos"))
outros = int(input("Qual é valor de outros"))

total = (aluguel + energia + agua + gas + internet + combustivel + alimentos + outros)

print(f"o custo total mensal de residencia é {total} euros")
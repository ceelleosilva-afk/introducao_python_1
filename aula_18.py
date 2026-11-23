salario = int(input("Determine salario do funcionario "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"valor do aumento é {aumento}")
print(f"novo salario é {novo_salario}")

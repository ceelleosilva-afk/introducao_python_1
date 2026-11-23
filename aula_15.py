horas = int(input("Determine horas trabalhadas ")) 
taxa = int(input("Determine valor por hora "))

if horas <= 40:
    pagamento = horas * taxa 
else:
    pagamento = 40 * taxa + (horas - 40) * taxa * 1.5
print(f"o pagamento total é {pagamento}, euros")    
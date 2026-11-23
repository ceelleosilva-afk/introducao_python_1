num_1 = float(input("Qual é o numero "))
num_2 = float(input("Qual é o numero "))
num_3 = float(input("Qual é o numero "))

if num_1 >= num_2 and num_1 <= num_3:
   maior = num_2
elif num_2 >= num_1 and num_2 >= num_3:
   maior = num_2 
else:
   maior = num_3

if num_1 <= num_2 and num_1 <= num_3: 
    menor = num_1
elif num_2 <= num_1 and num_2 <= num_3:
    menor = num_2
else:
    menor = num_3

print(f"o maior numero é {maior} ")   
print(f"menor numero é {menor} ")

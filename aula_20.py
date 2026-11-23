num_1 = int(input("Determine o primeiro numero "))
num_2 = int(input("Determine o segundo numero "))
operaçao = input("Qual opereçao deseja realizar (+ - * / ) ")

if operaçao == "+":
    resultado = num_1 + num_2
    print(f"O resultado foi de {resultado}")
elif operaçao == "-":
    resultado = num_1 - num_2
    print(f"O resultado foi de {resultado}")
elif operaçao == "*":
    resultado = num_1 * num_2
    print(f"O resultado foi de {resultado}")
else:
    operaçao == "/"
    resultado = num_1 / num_2  
    print(f"O resultado foi de {resultado}")                 
          
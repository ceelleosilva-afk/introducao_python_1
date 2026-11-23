total_segundos = int(input("mostre o valor em segundos"))

horas = total_segundos//3600 
resto_segundos = total_segundos%3600
minutos = resto_segundos//60
segundos = resto_segundos%60


print (f"{horas}hora(s), {minutos}minutos e {segundos} segundos")
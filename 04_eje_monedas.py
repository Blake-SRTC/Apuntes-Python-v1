pesos = input("Cuantos Bolivianos tienes?: ")
pesos = float(pesos)
valor_dolar = 6.97
dolares = pesos / valor_dolar
dolares = round(dolares, 2) #Limitamos la cantidad de decimales
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")
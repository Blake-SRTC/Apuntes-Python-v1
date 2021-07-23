#En ciertos casos usar listas y estas al ser dinamicas consumen mucha memoria y eso resulta ser ineficiente
#Para solucionar ese problema es cuando entran las tuplas

#Tuplas elementos de tipo estatico - no se pueden modificar
#Mas eficientes en los recorridos -  estructura de datos mas rapida

#Inmutabilidad - no puede cambiar

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)

for numero in mi_tupla:
    print(numero)

# Tupla de un solo valor
my_tuple = (1,)

# Desempaquetando una tupla
my_tuple = (1, 2, 3)
x, y, z = my_tuple
# Con funciones
def coordenadas():
    return (5, 4)

x, y = coordenadas()
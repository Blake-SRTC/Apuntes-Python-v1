#En ciertos casos usar listas y estas al ser dinamicas consumen mucha memoria y eso resulta ser ineficiente
#Para solucionar ese problema es cuando entran las tuplas

#Tuplas elementos de tipo estatico - no se pueden modificar
#Mas eficientes en los recorridos -  estructura de datos mas rapida

#Inmutabilidad - no puede cambiar

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 4, 5)

for numero in mi_tupla:
    print(numero)

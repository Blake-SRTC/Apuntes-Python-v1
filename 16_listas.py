#Lista
vacia = []
lista = [1,2,"Cadena",4.5,True, [1,False]]

#Suma (+) Concatena dos o más listas:
a=[1,2]
b=[3,4]
#a + b --> [1,2,3,4]

#Multiplicación (*) Repite la misma lista:
a=[1,2]
#a * 2 —> [1,2,1,2]

#Cuenta la cantidad de veces que el elemento aparece en la lista
a = [1,2,3,4,1,2,5,6,7,1]
veces = a.count(1)
#veces =  3

#Devuelve el indice del elemento indicado la primera vez que aparece
a = [1,2,3,4,1,2,3,4]
indice = a.index(2)
#indice = 1

#Añadir elemento al final de la lista:
a=[1]
a.append(2)
#a=[1,2]

#Inserta un elemento en la posicion indicada (posicion , elemento)
a = [1,2,3]
a.insert(1,5)
#a = [1,5,2,3]

#Devuelve el elemento y lo elimina del final de la lista:
a=[1,2]
b=a.pop()
#b=[2]
#a=[1]

#Devuelve el elemento y lo elimina dado un indice:
a=[1,2,3,4]
b=a.pop(1)
#b=[2]
#a=[1,3,4]

#Ordenar lista de menor a mayor, esto modifica la lista inicial
a=[3,8,1]
a.sort()
#a=[1,3,8]

#Ordenar lista de menor a mayor, esto NO modifica la lista inicial y se crea una nueva lista
a=[3,8,1]
b=sorted(a)

#Eliminar elementos de lista Elimina el elemento de la lista dado su indice
a = [1,2,3]
del a[0]
#a[2,3]

#Eliminar elementos de lista Elimina, el elemento de la lista dado su valor
a = [0, 2, 4, 6, 8]
a.remove(6)
#a = [0, 2, 4, 8]

#Range creacion de listas en un rango determinado
a = (list(range(0,10,2))) #crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
#a = [0,2,4,6,8]

#Devuelve el valor del tamaño de la lista:
a = [0,2,4,6,8]
longitud = len(a)
#longitud = 5

#Invierte la lista
a = [1,2,3,4,5,6]
a.reverse()
#a = [6,5,4,3,2,1]

#Recorrer una lista con for
lista_1 = [1, True, 4.5, 1]
for i in lista_1:
    print(i)


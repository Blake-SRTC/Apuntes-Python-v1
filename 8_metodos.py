#Uso de metodos
#Un metodo es una funcion de uso especial para un tipo de dato en particular

nombre = input("Ingresa tu nombres: ")

nombre.upper() #Todo a mayusculas
nombre.capitalize() #Primera letra a mayusculas
nombre.strip() #Elimina espacios basura al inicio o al final
nombre.lower() #Todo a minusculas
nombre.replace('o', 'a') #Reemplaze todas las letras 'o' por letras 'a'
nombre[0] #Busca el elemento de la posicion indicada

#Funciones build in (que van dentro de python)
len(nombre) #Devuelve la cantidad de caracteres - numero

#Rebanada - termina antes del ultimo valor indicado ([0:3] - 0,1,2)
nombre[0:3]
nombre[:3]
nombre[3:]
nombre[2:5]
nombre[1:7:2] #De 1 a 7 pero en pasos de 2 en 2
nombre[::] #Trae el nombre completo
nombre[1::3] #Del incide 1 hasta el final en pasos de 3 en 3
nombre[::-1] #Pasos inversos - Vamos del final al inicio

#slices

#Concatenar (+ concatenacion) (* repeticion)
michis = "gato" + "michi"

#Concatenar tipo formato
nombre = 'manuel'
f'Hola {nombre}'

#Obtener longitud
palabra = "edificio"
longitud_palabra = len(palabra)

#Posicion de caracter
posicion = palabra[0]

#Rebanada de string (slice [comienzo : final : pasos])
rebadana = "the boys"[2:6]

#Mostrar datos
print("impresion en consola")

#Salida multiple
print("hola","mundo") #agrega un espacio entre palabras

#Lectura entrada de consola (regresa cadenas)
nombre = input("Ingresa tu nombre")

#Entrada a numero
edad = int(input("Ingresa tu edad"))

#---------------------------------------------------------
#Comando Help de ayuda para saber que hace una funcion correctamente documentada
def suma(a, b):
    """
    Suma dos valores a y b
    Param init a cualeuir entero
    Param int b cualquien entero
    Returns la sumatoria de a y b
    """
    total = a + b
    return total
help(suma)
#Funciones Void
# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones!')


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# Utilziando parametro "mensaje" un input que recibe la funcion que se utiliza como variable local con un valor
# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estás')
#     print(mensaje)
#     print('Adios')


#Utilizando argumentos es el valor que se le envia a las funciones para que despues le funcion la reciba como parametro
# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1')
# elif opcion == 2:
#     conversacion('Elegiste la opción 2')
# elif opcion == 3:
#     conversacion('Elegiste la opción 3')
# else:
#     print('Escribe la opción correcta')


#Funciones con retorno
def suma(a, b): #parametros
    print('Se suman dos números')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4) #argumentos
print(sumatoria)

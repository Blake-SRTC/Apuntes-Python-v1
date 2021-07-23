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


#------------------------------------------------------------------------
def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

nombre_completo('juan', 'perez')
nombre_completo('juan', 'perez', inverso=True)
nombre_completo(apellido='perez', nombre='juan')

#--------------------------------------------------------------------------
#Funciones como objetos
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

# >>> nums = [1, 2, 3]
# >>> aplicar_operacion(multiplicar_por_dos, nums)
# [2, 4, 6]

# >>> aplicar_operacion(sumar_dos, nums)
# [3, 4, 5]

#-----------------------------------------------------------------------
#Funciones en Expresiones
sumar = lambda x, y: x + y

# >>> sumar(2, 3)
# 5

#------------------------------------------------------------------------
#Funciones en estructuras de datos
def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

# >>> aplicar_operaciones(-2)
# [2, -2.0]
#Dejando 2 espacios entre funciones es una buena practica
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

#Funcion principal - Estandar run o main
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')

#Entry point - Punto de entrada de un programa de python
if __name__ == '__main__':
    run()

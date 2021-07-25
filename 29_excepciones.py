
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))


# Excepciones comunes:
# ImportError : una importación falla;
# IndexError : una lista se indexa con un número fuera de rango;
# NameError : se usa una variable desconocida ;
# SyntaxError : el código no se puede analizar correctamente
# TypeError : se llama a una función en un valor de un tipo inapropiado;
# ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado

# ---------------------------------------------------------------------------------------------------------
# En este momento ya debes estar familiarizado con las estructuras de control flujo que ofrece Python (if... elif...else); 
# entonces, ¿por qué es necesaria otra modalidad para controlar el flujo? Una razón muy específica: el principio EAFP 
# (easier to ask for forgiveness than permission, es más fácil pedir perdón que permiso, por sus siglas en inglés).

# El principio EAFP es un estilo de programación común en Python en el cual se asumen llaves, 
# índices o atributos válidos y se captura la excepción si la suposición resulta ser falsa. 
# Es importante resaltar que otros lenguajes de programación favorecen el principio LBYL (look before you leap, revisa antes de saltar) 
# en el cual el código verifica de manera explícita las precondiciones antes de realizar llamadas.

# def busca_pais(paises, pais):
#     &quot;&quot;&quot;
#     Paises es un diccionario. Pais es la llave.
#     Codigo con el principio EAFP.
#     &quot;&quot;&quot;
    
#     try:
#         return paises[pais]
#     except KeyError:
#         return None
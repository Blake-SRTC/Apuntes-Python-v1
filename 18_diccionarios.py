# Diccionarios no tienen un orden interno y osn mutables

def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario)
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    # Imprime un valor
    # print(poblacion_paises['Bolivia'])

    #Imprime las llaves
    # for pais in poblacion_paises.keys():
    #     print(pais)

    #Imprime los valores
    # for pais in poblacion_paises.values():
    #     print(pais)

    #Imprime los items, 2 datos (llave, valor)
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()

# -----------------------------------------------------------------------------
# Busqueda
my_dict = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50,
}

#Comprobamos si existe un valor
my_dict.get('juan', 30)
# Respuesta 30 porque juan no exite

my_dict.get('David', 30)
# Respuesta 35 porque David si existe

# Reasiganar nuevos valores
my_dict['Jaime'] = 20
# Asignar nueva llave
my_dict['Pedro'] = 70
# Borrar items (llave y valor)
del my_dict['Jaime']

# Busqueda 
'David' in my_dict
#True
'Tom' in my_dict
#False
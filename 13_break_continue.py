def run():
    #Continue se salta la vuelta del ciclo for y va a la siguiente vuelta, no ejecuta lo que se encuentra debajo por el salto
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    #Break corta el ciclo for en el limite indicado
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()

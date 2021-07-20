# La secuencia de Fibonacci es una función matemática que se define recursivamente.
# En el año 1202, el matemático italiano Leonardo de Pisa, también conocido como Fibonacci, 
# encontró una fórmula para cuantificar el crecimiento que ciertas poblaciones experimentan.

# Imagina que una pareja de conejos nace, un macho y una hembra, y luego son liberados.
# Imagina, también, que los conejos se pueden reproducir hasta la edad de un mes y que tienen un periodo de gestación también de un mes.
# Por último imagina que estos conejos nunca mueren y que la hembra siempre es capaz de producir una nueva pareja (un macho y una hembra).
# ¿Cuántos conejos existirán al final de seis meses?

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Ingrese un cantidad de meses'))

print(f'{fibonacci(n)} Conejos al final de {n} meses')
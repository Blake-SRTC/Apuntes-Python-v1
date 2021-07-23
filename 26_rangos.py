
# range(comienzo, final, pasos)
# no inclusivo, no incluye el valor final

my_range = range(1, 5)

#caso
range1 = range(0, 7, 2)
range2 = range(0, 8, 2)
# Value equality
range1 == range2
# True, ambos terminan en 6

#Direccion en memoria
id(range1)
id(range2)
#object equality
range1 is range2
# False, son objetos diferentes

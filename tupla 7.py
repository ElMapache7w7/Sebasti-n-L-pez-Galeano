#ejercicio Tuplas 7
#Ordenar una tupla de tuplas por el segundo elemento
#Dado:
#tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# Salida esperada:
#(('c', 11), ('a', 23), ('d', 29), ('b', 37))
tuple1 = (("a", 23),("b", 37),("c", 11),("d", 29))
print(tuple1)
a, b, c, d = tuple1
#revolver
a, b , c, d = c, a, d, b
print(a, b, c, d)
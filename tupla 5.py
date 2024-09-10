#Copiar elementos específicos de una tupla a una nueva tupla
#Escribe un programa para copiar los elementos 44 y 55 de la siguiente tupla en una nueva tupla.
#Dado:
#tuple1 = (11, 22, 33, 44, 55, 66)

#Salida esperada:
#tuple2: (44, 55)
tuple1 = (11, 22, 33, 44, 55, 66)
print(tuple1)
tuple2 = tuple1[3:5]
print(tuple2)
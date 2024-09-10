#Intercambiar dos tuplas en Python
#Dado:
#tuple1 = (11, 22)
#tuple2 = (99, 88)

#Salida esperada:
#tuple1: (99, 88)
#tuple2: (11, 22)
tuple1 = (11, 22)
tuple2 = (99, 88)
print("tuple1:", tuple1)
print("tuple2:", tuple2)
print("------------")
tuple1, tuple2 = tuple2, tuple1
print("tuple1:", tuple1)
print("tuple2:", tuple2)

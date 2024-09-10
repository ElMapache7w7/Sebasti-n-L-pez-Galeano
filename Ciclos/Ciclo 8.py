#Escriba un programa para hacer un patrón como una pirámide con números aumentados en 1.
#   1
#  2 3
# 4 5 6
#7 8 9 10

n = int(input("Ingrese el numero de filas de la piramide: "))
num = 1

for i in range(1, n + 1 ):
    print(" " * (n - i), end=' ')
    for j in range(i):
        print(f"{num}", end=' ')
        num += 1
    print()
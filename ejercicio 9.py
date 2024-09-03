#Escriba un programa para calcular el factorial de un número dado.

num = int(input("Ingrese el numero"))
fac = 1

for i in range(1, num + 1):
    fac *= i
print(f"El factorial de {num} es {fac}")
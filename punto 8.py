# Solicitar los números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Crear una lista con los números ingresados
numeros = [num1, num2, num3]

# Ordenar la lista en orden ascendente
numeros_ascendente = sorted(numeros)

# Ordenar la lista en orden descendente
numeros_descendente = sorted(numeros, reverse=True)

# Imprimir los resultados
print("El orden ascendente es:", numeros_ascendente)
print("El orden descendente es:", numeros_descendente)

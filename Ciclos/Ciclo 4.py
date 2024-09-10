#Escribe un programa para leer 10 números del teclado y encontrar su suma y promedio.
suma = 0
for i in range(10):
    numero = float(input("Ingrese un número: "))
    suma += numero
    promedio = suma / 10
print("La suma de los números ingresados es:", suma)
print ("El promedio de los números ingresados es:", promedio)
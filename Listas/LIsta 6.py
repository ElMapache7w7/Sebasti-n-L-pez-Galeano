#Dada una lista de números. Escribe un programa para convertir cada elemento de una lista en su cuadrado. Ejemplo dado: numbers = [1, 2, 3, 4, 5, 6, 7]Resultado esperado: numbers = [1, 4, 9, 16, 25, 36, 49]
numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros)
for i in range(len(numeros)):
  numeros[i] = numeros[i]**2
print(numeros)

#Escriba una función para sumar todos los números de una lista. Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20. (Usando funciones)
def suma(lista):
  suma=0
  for i in lista:
    suma+=i
  return suma
lista=[8,2,3,0,7]
print(lista)
print("La suma de los numeros de la lista es: ",suma(lista))
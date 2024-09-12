#Escriba una función para multiplicar todos los números de una lista. Lista de muestra: (8, 2, 3, -1, 7)Resultado esperado: -336
def multiplicar(lista):
  resultado=1
  for i in lista:
    resultado=resultado*i
  return resultado
lista=[8,2,3,-1,7]
print(lista)
print("El resultado de la multiplicacion es: ",multiplicar(lista))
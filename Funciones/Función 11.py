#Escriba un programa para imprimir los números pares de una lista determinada
def num_pares(lista):
  for i in lista:
    if i % 2 == 0:
      print(i)
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
num_pares(lista)

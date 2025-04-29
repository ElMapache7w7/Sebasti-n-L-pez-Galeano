#Escriba un programa para eliminar duplicados de una lista.
lista = [1,2,3,4,5,6,7,8,9,10,4,5,6,7,8,9,10,1,2,3,4,5,6,7]
print(lista)
lista_no_duplicados = []
for i in lista:
  if i not in lista_no_duplicados:
    lista_no_duplicados.append(i)
print("Lista sin duplicados: ", lista_no_duplicados)
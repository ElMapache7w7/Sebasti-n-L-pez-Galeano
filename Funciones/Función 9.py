#Escriba una función que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista. 
def unique_list(list):
  unique_list = []
  for i in list:
    if i not in unique_list:
      unique_list.append(i)
  return unique_list
lista = [1,2,3,3,3,3,4,5]
print(lista)
print(unique_list(lista))
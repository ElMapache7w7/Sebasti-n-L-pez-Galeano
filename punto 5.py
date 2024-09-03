#Escriba un programa para mostrar la tabla de multiplicar de un entero dado
#Entrada: un entero
#Salida: la tabla de multiplicar del entero dado
n = int(input("Ingrese un numero: "))
for i in range(1,11):
  print(n,"x",i,"=",n*i)
  
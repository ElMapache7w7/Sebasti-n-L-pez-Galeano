#Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir el resultado.
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
if numero1 > numero2:
  print ("El numero mayor es: ", numero1)
elif numero1 < numero2:
  print("El numero mayor es: ", numero2)
else:
  print("Ingrese un numero valido")
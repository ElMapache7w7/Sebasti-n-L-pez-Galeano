#Solicitar número al usuario y determinar si es par, impar o es cero. 
#solicitar numero
num = int(input("Ingrese un número: "))
#determinar si es par, impar o es cero
if num == 0:
  print("El número es cero")
elif num % 2 == 0:
  print("el numero es par")
else:
  print("El numero es impar")
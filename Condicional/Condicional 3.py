#Solicitar número al usuario y determinar si es negativo, positivo o cero.
numero = int(input("Ingrese un número: "))
if numero > 0:
  print("El número es positivo.")
elif numero < 0:
  print("El número es negativo.")
elif numero == 0:
  print(numero, "El número es cero.")

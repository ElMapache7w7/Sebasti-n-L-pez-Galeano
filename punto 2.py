#Preguntar al usuario el nombre y la edad, si es mayor o igual a 18 años mostrar el mensaje "Usted es mayor de edad", de lo contrario "Usted es menor de edad". Si el número ingresado es negativo o la edad ingresada es mayor a 100 años, mostrar al usuario un mensaje de ingresar una edad válida.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad <= 18 and edad <= 100:
  print("Ingrese una edad válida")
elif edad >= 0 and edad <= 17:
  print("Usted es menor de edad")
else:
  print("Ingrese una edad válida")
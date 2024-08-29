#Conversión de temperaturas. Crear un menú de opciones. 
#preguntar que conversión quiere hacer
#pedir los datos necesarios
#mostrar el resultado
print("Conversión de temperaturas")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
print("3. Celsius a Kelvin")
print("4. Kelvin a Celsius")
print("5. Fahrenheit a Kelvin")
print("6. Kelvin a Fahrenheit")
print("7. farenheit a reanumur")
print("8. reanumur a farenheit")
print("9. rakine a celsius")
print("10. celsius a rakine")
print("11. rakine a farenheit")
print("12. farenheit a rakine")
print("13. celsius a reanumur")
print("14. reanumur a celsius")
print("15. celsius a rankine")
print("16. rankine a celsius")
print("17. salir")

opcion = int(input("Elige una opción: "))
if opcion == 1:
  celsius = float(input("Introduce la temperatura en grados Celsius: "))
  fahrenheit = (celsius * 1.8) + 32
  print("La temperatura en grados Fahrenheit es:", fahrenheit)
elif opcion == 2:
  fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
  celsius = (fahrenheit - 32) / 1.8
  print("La temperatura en grados Celsius es:", celsius)
elif opcion == 3:
  celsius = float(input("Introduce la temperatura en grados Celsius: "))
  kelvin = celsius + 273.15
  print("La temperatura en grados Kelvin es:", kelvin)
elif opcion == 4:
  kelvin = float(input("Introduce la temperatura en grados Kelvin: "))
  celsius = kelvin - 273.15
  print("La temperatura en grados Celsius es:", celsius)
elif opcion == 5:
  fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
  kelvin = (fahrenheit + 459.67)/1.8
  print("La temperatura en grados Kelvin es:", kelvin)
elif opcion == 6:
  kelvin = float(input("Introduce la temperatura en grados Kelvin: "))
  fahrenheit = (kelvin * 1.8) - 459.67
  print("La temperatura en grados Fahrenheit es:", fahrenheit)
elif opcion == 7:
  farenheit = float(input("Introduce la temperatura en grados Farenheit: "))
  reanumur = (farenheit - 32) / 2.25
  print("La temperatura en grados Reanumur es:", reanumur)
elif opcion == 8:
  reanumur = float(input("Introduce la temperatura en grados Reanumur: "))
  farenheit = (reanumur * 2.25) + 32
  print("La temperatura en grados Farenheit es:", farenheit)
elif opcion == 9:
  rakine = float(input("Introduce la temperatura en grados Rakine: "))
  celsius = (rakine - 32 - 491.67) / 1.8
  print("La temperatura en grados Celsius es:", celsius)
elif opcion == 10:
  celsius = float(input("Introduce la temperatura en grados Celsius: "))
  rakine = (celsius * 1.8) + 32 + 491.67
  print("La temperatura en grados Rakine es:", rakine)
elif opcion == 11:
  rakine = float(input("Introduce la temperatura en grados Rakine: "))
  farenheit = (rakine - 459.67)
  print("La temperatura en grados Farenheit es:", farenheit)
elif opcion == 12:
  farenheit = float(input("Introduce la temperatura en grados Farenheit: "))
  rakine = (farenheit + 459.67)
  print("La temperatura en grados Rakine es:", rakine)
elif opcion == 13:
  celsius = float(input("Introduce la temperatura en grados Celsius: "))
  reanumur = (celsius * 0.8)
  print("La temperatura en grados Reanumur es:", reanumur)
elif opcion == 14:
  reanumur = float(input("Introduce la temperatura en grados Reanumur: "))
  celsius = (reanumur * 1.25)
  print("La temperatura en grados Celsius es:", celsius)
elif opcion == 15:
  celsius = float(input("Introduce la temperatura en grados Celsius: "))
  rankine = (celsius * 1.8) + 32 + 491.67
  print("La temperatura en grados Rankine es:", rankine)
elif opcion == 16:
  rankine = float(input("Introduce la temperatura en grados Rankine: "))
  celsius = (rankine - 32 - 491.67) / 1.8
  print("La temperatura en grados Celsius es:", celsius)
elif opcion == 17:
  print("Hasta luego")
else:
  print("Opción inválida")
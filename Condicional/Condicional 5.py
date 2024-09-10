#Solicitar cinco (5) notas de 0.0 a 5.0 a un estudiante y calcular promedio.  Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0. 
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))
nota5 = float(input("Ingrese la quinta nota: "))
#sumar todas las notas
suma = nota1 + nota2 + nota3 + nota4 + nota5
#calcular promedio de notas
promedio = suma / 5
#mostrar promedio
print("El promedio de las notas es: ", promedio)
#condicional promedio
if promedio >= 3.0:
  print("Aprobó")
else:
  print("No aprobó")
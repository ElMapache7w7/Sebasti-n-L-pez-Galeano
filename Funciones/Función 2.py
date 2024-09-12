#Escriba un programa para calcular las áreas de las figuras geométricas utilizando una función para cada área.  (con funciones)
#definir figuras

def area_cuadrado(lado):
  area = lado * lado
  return area
def area_rectangulo(base, altura):
  area = base * altura
  return area
def area_triangulo(base, altura):
  area = (base * altura) / 2
  return area
def area_circulo(radio):
  area = 3.1416 * (radio ** 2)
  return area
def paralelogramo(base,altura):
  area = base * altura
  return area
def trapecio(base_mayor, base_menor, altura):
  area = ((base_mayor + base_menor) * altura) / 2
  return area
def rombo(diagonal_mayor, diagonal_menor):
  area = (diagonal_mayor * diagonal_menor) / 2
  return area
#menu de opciones 
print("Selecione la figura que desea calcular su area")
print("1. Cuadrado")
print("2. Rectangulo")
print("3. Triangulo")
print("4. Circulo")
print("5. Paralelogramo")
print("6. Trapecio")
print("7. Rombo")
opcion = int(input("Seleccione una opcion: "))
#area cuadrado
if opcion == 1:
  lado1 = float(input("Ingrese el lado 1 del cuadrado:"))
  lado2 = float(input("Ingrese el lado 2 del cuadrado:"))
  area = lado1 * lado2
  print("El area del cuadrado es:", area)
#area rectangulo
elif opcion == 2:
  base = float(input("Ingrese la base del rectangulo: "))
  altura = float(input("Ingrese la altura del rectangulo: "))
  area = area_rectangulo(base, altura)
  print("El area del rectangulo es:", area)
#area triangulo
elif opcion ==3:
  base = float(input("Ingrese la base del triangulo: "))
  altura = float(input("Ingrese la altura del triangulo: "))
  area = area_triangulo(base, altura)
  print("El area del triangulo es:", area)
#area circulo
elif opcion ==4:
  radio = float(input("Ingrese el radio del circulo: "))
  area = area_circulo(radio)
  print("El area del circulo es:", area)
#area paralelogramo
elif opcion ==5:
  base = float(input("Ingrese la base del paralelogramo: "))
  altura = float(input("Ingrese la altura del paralelogramo: "))
  area = paralelogramo(base, altura)
  print("El area del paralelogramo es:", area)
#area trapecio
elif opcion ==6:
  base_mayor = float(input("Ingrese la base mayor del trapecio: "))
  base_menor = float(input("Ingrese la base menor del trapecio: "))
  altura = float(input("Ingrese la altura del trapecio: "))
  area = trapecio(base_mayor, base_menor, altura)
  print("El area del trapecio es:", area)
#area rombo
elif opcion ==7:
  diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
  diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
  area = rombo(diagonal_mayor, diagonal_menor)
  print("El area del rombo es:", area)
else:
  print("Opcion invalida")
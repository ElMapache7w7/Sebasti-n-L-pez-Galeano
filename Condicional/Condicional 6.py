# Menú de opciones para calcular áreas de figuras geométricas
print("Elija la figura geométrica para calcular el área:")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Paralelogramo")
print("5. Rombo")
print("6. Trapecio")
print("7. Triángulo equilátero")
print("8. Triángulo rectángulo")
print("9. Polígono regular")

# Solicitar al usuario que ingrese la figura que desea calcular
figura = input("Ingrese el nombre de la figura: ").strip().lower()

# Calcular el área según la figura seleccionada
if figura == "cuadrado":
    lado = float(input("Ingrese el valor del lado: "))
    area = lado * lado
    print("El área del cuadrado es:", area)
elif figura == "rectangulo":
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = base * altura
    print("El área del rectángulo es:", area)
elif figura == "triangulo":
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = (base * altura) / 2
    print("El área del triángulo es:", area)
elif figura == "paralelogramo":
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = base * altura
    print("El área del paralelogramo es:", area)
elif figura == "rombo":
    diagonal1 = float(input("Ingrese el valor de la diagonal1: "))
    diagonal2 = float(input("Ingrese el valor de la diagonal2: "))
    area = (diagonal1 * diagonal2) / 2
    print("El área del rombo es:", area)
elif figura == "trapecio":
    base1 = float(input("Ingrese el valor de la base1: "))
    base2 = float(input("Ingrese el valor de la base2: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = ((base1 + base2) * altura) / 2
    print("El área del trapecio es:", area)
elif figura == "triangulo equilatero":
    lado = float(input("Ingrese el valor del lado: "))
    area = (math.sqrt(3) / 4) * (lado**2)
    print("El área del triángulo equilátero es:", area)
elif figura == "triangulo rectangulo":
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    area = (base * altura) / 2
    print("El área del triángulo rectángulo es:", area)
elif figura == "poligono regular":
    perimetro = float(input("Ingrese el valor del perímetro: "))
    apotema = float(input("Ingrese el valor del apotema: "))
    area = (perimetro * apotema) / 2
    print("El área del polígono regular es:", area)
else:
    print("La figura ingresada no es válida")

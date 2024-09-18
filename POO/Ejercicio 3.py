#Escriba una clase llamada Circle construida por un radio y dos métodos 
# que calcularán el área y el perímetro de un círculo.

import math

class Circle:
    def __init__(self, radio):
        self.radio = radio

    def area_circle(self):
        resultado_area = math.pi * (radio1 ** 2)
        return resultado_area
    def perimetro_circle(self):
        resultado_perimetro = 2 * math.pi * radio1
        return resultado_perimetro

radio1 = float(input("Ingrese el radio del circulo: "))
circleuwu = Circle(radio1)

area = circleuwu.area_circle()
perimetro = circleuwu.perimetro_circle()

print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

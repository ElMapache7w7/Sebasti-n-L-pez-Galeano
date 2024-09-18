#Escriba una clase llamada Rectangle construida por una longitud y anchura y un método que calculará el área de un rectángulo.

class Rectangle:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def area_rectangulo(self):
        Resultado = longitud1 * anchura1
        return Resultado

longitud1 = int(input("Ingrese la longitud del rectangulo: "))
anchura1 = int(input("Ingrese la anchura del rectangulo: "))

rectangle_la = Rectangle(longitud1, anchura1)

area = rectangle_la.area_rectangulo()
print(f"El área del rectangulo es: {area}")
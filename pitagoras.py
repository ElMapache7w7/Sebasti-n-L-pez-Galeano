#Calcular la hipotenusa con el Teorema de Pitágoras (sin usar funciones).
#solicitar cateto 1
cateto1 = float(input("Ingrese el cateto 1:"))
#solicitar cateto 2
cateto2 = float(input("Ingrese el cateto 2:"))
#calcular hipotenusa
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 2
#imprimir resultado
print(f"La hipotenusa es {hipotenusa}:")
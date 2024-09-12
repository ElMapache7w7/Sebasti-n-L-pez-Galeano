#Escriba una función para comprobar si un número cae en un rango determinado. Defina como parámetros rango de inicio, número y rango final.  
def rango(inicio,numero,fin):
  if inicio<=numero<=fin:
    print("El numero esta dentro del rango")
  else:
    print("El numero no esta dentro del rango")
inicio=int(input("Ingrese el inicio del rango: "))
numero=int(input("Ingrese el numero: "))
fin=int(input("Ingrese el final del rango: "))
rango(inicio,numero,fin)

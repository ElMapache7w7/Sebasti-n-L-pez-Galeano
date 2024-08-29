#14. El número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico se calcula con la fórmula:
# Ingresar la edad
edad = int(input("Ingrese la edad: "))

# Ingresar el género
print("Seleccione el género:")
print("1. Femenino")
print("2. Masculino")
genero = int(input("Ingrese el número correspondiente al género (1 o 2): "))

# Condicionales para calcular las pulsaciones
if genero == 1:
    pulsaciones = (220 - edad) / 10
    print(f"El número de pulsaciones para una persona femenina es: {pulsaciones}")
elif genero == 2:
    pulsaciones = (210 - edad) / 10
    print(f"El número de pulsaciones para una persona masculina es: {pulsaciones}")
else:
    print("Ingrese un género válido (1 para femenino o 2 para masculino).")

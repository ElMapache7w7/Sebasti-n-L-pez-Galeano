# Precios según el tamaño de la pizza
precios_pizza = {1: 15000, 2: 24000, 3: 36000}
precio_ingrediente_adicional = 4000

# Seleccionar el tamaño de la pizza
print("Tamaño de pizza:")
print("1. Tamaño 1 - $15.000")
print("2. Tamaño 2 - $24.000")
print("3. Tamaño 3 - $36.000")
pizza = int(input("Seleccione el tamaño de la pizza (1-3): "))

# Validar el tamaño seleccionado
if pizza not in precios_pizza:
    print("Ingrese un tamaño de pizza válido.")
else:
    # Solicitar el número de ingredientes adicionales
    ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales (cada uno cuesta $4.000): "))

    # Calcular el precio total
    precio_total = precios_pizza[pizza] + (ingredientes_adicionales * precio_ingrediente_adicional)

    # Mostrar el precio total al cliente
    print(f"El precio total a pagar es: ${precio_total}")

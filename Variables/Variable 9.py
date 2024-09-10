#solicitar el producto 

producto = input("Ingrese el producto: ")

#precio unitario del producto

precio_unitario = float(input("Ingrese el precio unitario: "))

#cantidad de productos comprados

cantidad = int(input("Ingrese la cantidad de productos: "))

#precio final

precio_final = precio_unitario * cantidad

#adicion del iva

iva = precio_final * 0.16

#precio final con iva

precio_final_con_iva = precio_final + iva

#mostrar el precio final con iva

print("El precio final con iva es: ", precio_final_con_iva)


#Un local vende sus productos con la siguiente promoción. Si compra hasta 5 artículos, no hay descuento. Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%. Si compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y el valor del precio unitario original. Calcule y muestre el valor total a pagar.
#cantidad de productos
cantidad = int(input("Ingrese la cantidad de articulos: "))
#valor del producto
valor = int(input("Ingrese el valor del producto: "))
#condicionales
if cantidad <= 5:
  print("No hay descuento")
elif cantidad > 5 and cantidad < 10:
  print("El precio unitario se reduce en 5%")
elif cantidad >= 10:
  print("El precio unitario se reduce en 8%")
#calculo
total = cantidad * valor
print("El total a pagar es: ", total)

#Leer el número de llantas de una compra y mostrar el valor que debe pagarse. El almacén las vende con la siguiente política: Si se compran menos de 6 llantas, el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000, y si se compran más de 7 llantas, el precio unitario es $180000.
#numero de llantas
llantas=int(input("ingrese el numero de llantas:"))
#condicionales
if llantas < 6:
  print("el precio unitario es de $240000")
elif llantas==6 or llantas==7:
  print("el precio unitario es de $221000")
elif llantas>7:
  print("el precio unitario es de $180000")
else:
  print("no se puede realizar la compra")
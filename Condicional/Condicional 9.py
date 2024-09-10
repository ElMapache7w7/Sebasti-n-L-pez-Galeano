#Programa que permita a un usuario tomar una decisión del tipo de pago a usar. Si la cuenta es menor a $150000 pago en efectivo. Si no, si es de $150000 hasta $300000 pago con el celular (dinero electrónico). Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Todos los valores superiores a $6000000, pago con la tarjeta de crédito.
#valor de la cuenta
cuenta = int(input("Ingrese el valor de la cuenta: "))
#condicionales
if cuenta < 150000:
  print("Pago en efectivo")
elif cuenta >= 150000 and cuenta <= 300000:
  print("Pago con el celular (dinero electrónico)")
elif cuenta > 300000 and cuenta <= 600000:
  print("Pago con la tarjeta de débito")
else:
  print("Pago con la tarjeta de crédito")
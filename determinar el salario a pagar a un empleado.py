#Programa que permita determinar el salario a pagar a un empleado, teniendo como entradas el salario diario y el número de días trabajados. Tenga en cuenta que al empleado se le debe descontar el 10% por concepto de pensión y 15% por concepto de salud.

#Entradas

salario_diario = float(input("Ingrese el salario diario: "))

#dias trabajados

dias_trabajados = int(input("Ingrese los dias trabajados: "))

#descuento del 10%

descuento_pension = 0.10

#descuento del 15% salud

descuento_salud = 0.15

#salario restante

salario_restante = salario_diario * dias_trabajados

#descuento de pension y salud
descuento = descuento_pension+descuento_salud

#salario total

salario_total = salario_restante - (salario_restante*descuento)

#su salario es de

print("Su salario es de: ", salario_total)
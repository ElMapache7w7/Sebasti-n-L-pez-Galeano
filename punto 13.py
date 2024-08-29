#Un reporte de salud muestra una tabla diferente del índice de masa corporal IMC de una persona que se calcula con la fórmula IMC=P/(E*E) en donde P es el peso en Kg. y E es la estatura en metros. Lea un valor de P y de E, calcule el IMC y muestre su estado según la siguiente tabla:
#IMC	Estado
#Menos de 18.5	desnutrido
#18.5 a 25	normal
#25.0 a 30	sobrepeso
#30.0 a 35	obesidad grado 1
#35.0 a 40	obesidad grado 2
#40.0 a 50 más	obesidad grado 3
#>=50	obesidad grado 4
#ingresar el peso en kilogramos
peso=float(input("ingrese el peso en kilogramos: "))
#ingresar la estatura en metros
estatura = float(input("ingrese su estatura en metros"))
#calcular el IMC
imc = peso / (estatura * estatura)
#imprimir el IMC
print("su imc es:", imc)
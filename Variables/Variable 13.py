#Solicitar tiempo en segundos y transformar a horas y minutos.
#pedir segundos
segundos = int(input("Ingrese el tiempo en segundos: "))
#transformar a horas
horas = segundos // 3600
#transformar a minutos
minutos = (segundos % 3600) // 60
#imprimir
print (f"El tiempo en horas es: {horas} horas y {minutos} minutos")
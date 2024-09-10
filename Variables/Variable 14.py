#Solicitar al usuario una distancia en metros y transformar a km., cm. y mm. 
#solicitar distancia en metros
metros = float(input("Ingrese la distancia en metros: "))
#transformar a km., cm. y mm.
kilometros = metros / 1000
centimetros = metros * 100
milimetros = metros * 1000
#imprimir
print(f"La distancia en kilometros es: {kilometros} km:")
print(f"La distancia en centimetros es: {centimetros} cm:")
print(f"La distancia en milimetros es: {milimetros} mm:")
#solicitar al usuario la velocidad en km/h

velocidad_kmh = float(input("Ingrese la velocidad en km/h: "))

#solicitar el tiemppo en horas

tiempo_horas = float(input("Ingrese el tiempo en horas: "))

#calcular la distancia recorrida
distancia_km = velocidad_kmh * tiempo_horas

print(f"La distancia recorrida es: {distancia_km} km")
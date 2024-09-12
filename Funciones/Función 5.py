#Escriba un programa para invertir una cadena. Cadena de ejemplo: "1234abcd" Resultado esperado: "dcba4321" (usando funciones)
def invertir(cadena):
  return cadena[::-1]
cadena = "1234abcd"
print(cadena)
print(invertir(cadena))
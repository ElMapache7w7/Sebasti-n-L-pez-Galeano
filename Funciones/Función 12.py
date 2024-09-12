#Escriba una función que compruebe si una cadena frase o palabra pasada es palíndromo o no. Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo: Ana, Anita lava la tina. 
def palindromo(frase):
  frase=frase.lower()
  frase=frase.replace(" ","")
  if frase==frase[::-1]:
    return True
  else:
    return False
frase=input("Ingrese una frase: ")
print(palindromo(frase))

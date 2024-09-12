#Escriba una función que acepte una cadena y calcule el número de letras mayúsculas y minúsculas. 
def contar_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0
    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
    return mayusculas, minusculas
cadena = input("Ingrese una cadena: ")
mayusculas, minusculas = contar_mayusculas_minusculas(cadena)
print("Número de letras mayúsculas:", mayusculas)
print("Número de letras minúsculas:", minusculas)

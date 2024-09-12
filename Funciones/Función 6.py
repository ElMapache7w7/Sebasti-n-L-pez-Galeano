#Escriba una función para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = 7

print(f"Factorial de {numero}:", factorial(numero))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = 9

print(f"Factorial de {numero}:", factorial(numero))
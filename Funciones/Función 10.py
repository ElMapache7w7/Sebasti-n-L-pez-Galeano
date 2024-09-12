#Escriba una función que tome un número como parámetro y verifique que el número sea primo o no. Un número primo (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo.
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


numero = int(input("Ingrese un numero: "))
print(f"¿Es {numero} primo?:", es_primo(numero))
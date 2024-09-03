# Solicita al usuario el número de términos que desea ver en la serie de Fibonacci
n = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
a = 0  
b = 1  
suma = 0  
for i in range(n):
    print(a)  
    suma = a  
    a_ = b 
    b_ = a + b 

    a = a_
    b = b_

print(f"La suma de los {n} términos de la serie de Fibonacci es: {suma}")

#Escriba una clase para implementar pow(x, n).

class Pow:
    def __init__(self, x, n):
        self.x = x
        self.n = n 
    def procedimiento(self):
        resultado = numx ** numn
        return resultado
    
numx = float(input("Ingrese el numero: "))
numn = float(input("Ingrese la potencia: "))
powu = Pow (numx, numn)

p = powu.procedimiento()
print(f"{numx} elevado a {numn} es : {p}")

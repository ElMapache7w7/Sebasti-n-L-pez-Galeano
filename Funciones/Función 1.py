#Escriba una función para encontrar el máximo de tres números. 
def maximo(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  elif c>a and c>b:
    return c
print("1,2,3")
print("El máximo de los tres números es: ",maximo(1,2,3))

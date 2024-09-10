#Escriba un programa para mostrar un patrón como Z con asteriscos. 
#*******
#     *
#    *
#   *
#  *
# *
#*******

n = 7
for i in range(n):
    if i == 0 or i == n - 1:
            
        print('*' * n)
    else:
            
        print(' ' * (n - i - 1) + '*')

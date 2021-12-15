import sys

n = int(sys.argv[1])

if n > 0:
    pot = 0
    suma = 0
    for i in range(n,1 , -1):
        pot = i * n
        suma = pot * suma
        break
    print(suma)
else:
    print('El numero no es valido') 
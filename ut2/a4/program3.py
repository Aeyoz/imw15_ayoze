import sys

k = int(sys.argv[1])

cadena = str(sys.argv[2])

string = cadena.split()

cont = 0
if k > 0:
    for i in string:
        long = len(i)
        contador = (long == k)
        if contador == True:
            cont = cont + 1

print(f'Hay {cont} palabras de longitud {k}')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero
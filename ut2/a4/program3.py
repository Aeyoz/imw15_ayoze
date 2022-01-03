# Importamos datos por linea de comandos y definimos variables.
import sys
k = int(sys.argv[1])
cadena = str(sys.argv[2])
string = cadena.split()
cont = 0

# Definimos el programa

if k > 0:
    for i in string:
        long = len(i)
        contador = (long == k)
        if contador == True:
            cont = cont + 1

# Devolvemos los resultados por pantalla.

    print(f'Hay {cont} palabras de longitud {k}')
else:
    print(f'El caracter {k} no es válido porque no es un número o no es un número positivo')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero
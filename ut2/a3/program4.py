# Importamos datos por linea de comandos

import sys

# Definimos variables

n = int(sys.argv[1])

# Elaboramos el programa

def factoriales(n):
    if (n==0):
        return 1
    else:
        return n * factoriales(n-1)

# Devolvemos el resultado

print(f'El factorial de {n} es {factoriales(n)}')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero

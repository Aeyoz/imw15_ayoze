# Importamos datos por linea de comandos y definimos variables.

import sys

n = int(sys.argv[1])

#~Elaboramos el programa

if n > 0:
    j = 0
    sum = 0
    for i in range(1, n + 1):
        j = i**2
        sum = j + sum
# Devolvemos por pantalla los resultados
    print(f'La suma de cada uno de los terminos de {n} es {sum}')
else:
    print('El número no es válido')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero

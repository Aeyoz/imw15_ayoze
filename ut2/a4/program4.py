# Importamos datos por linea de comandos y definimos variables.

import sys

# Entry registra todas las entradas desde el índice 1 hasta el último que se registre

entry = list(sys.argv[1:])

# Se convierten todos los datos de entry (str) a flotantes (float)

lista = [float(i) for i in entry]

# Definimos variables.

media = 0
notas_positivas = 0
total_items = 0
notas_negativas = 0

# Elaboramos el programa que recuenta las notas de los alumnos

for i in lista:
    if i < 0 or i > 10:
        notas_negativas = notas_negativas + 1
        print(f'La nota {i} es inválida, por lo que no se tendrá en cuenta para la media')
    else:
        notas_positivas = notas_positivas + i
        total_items = total_items + 1
        media = notas_positivas / total_items

print(f'La media de las notas es de: {media}')
if notas_negativas > 0:
    print(f'Hay una cantidad de {notas_negativas} suspendidos')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero

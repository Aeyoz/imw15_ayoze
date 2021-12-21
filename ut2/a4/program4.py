import sys

entry = list(sys.argv[1:])

lista = [float(i) for i in entry]

media = 0
notas_positivas = 0
total_items = 0
notas_negativas = 0
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

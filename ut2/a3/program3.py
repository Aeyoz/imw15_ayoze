# Importamos datos por linea de comandos y definimos variables.
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])

# Definimos el programa y devolvemos los resultados.

if x > 0 and y > 0:
    if x > y:
        min = y
        max = x
    else:
        min = x
        max = y
    for i in range(min,1-1,-1):
        if min % i == 0:
            if max % i == 0:
                print(f'El MCD de {x} y {y} es {i}')
                break
else:
    print('El número no es valido')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero

# Hacemos los imports necesarios.

import sys

# Importamos los datos del sistema.

nota = float(sys.argv[1])

# Definimos que hace el programa y mostramos los resultados por pantalla.

if nota < 5.0:
    print('Suspenso')
elif nota >= 5.0 and nota < 7.0:
    print('Aprobando')
elif nota >= 7.0 and nota < 9.0:
    print('Notable')
elif nota >= 9.0 and nota < 10.0:
    print('Sobresaliente')
elif nota == 10.0:
    print('Matricula de honor')
elif nota > 10.0 or nota < 0:
    print('Nota no válida.')
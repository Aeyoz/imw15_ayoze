# Importamos datos por linea de comandos

import sys

n = int(sys.argv[1])

#~Elaboramos el programa

if n > 0:
    for i in range(2, n):
        if n%i==0:
            print('El numero no es primo')
            break
    else:
        print(f'El numero {n} es primo')
else:
    print(f'El numero {n} no es valido')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero

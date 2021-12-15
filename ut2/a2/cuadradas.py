# Hacemos los imports necesarios.

import sys

# Importamos los datos del sistema.

a = float(sys.argv[1]);b = float(sys.argv[2]);c = float(sys.argv[3])

# Definimos que tiene que hacer el programa según los valores que se otorgue mediante linea de comando.
rz = (b**2-4*a*c)
if a == 0:
    x = -c/b
    print(f'La solución de X es: {x}')                                # Mostramos en pantalla una de las soluciones.
else:
    if rz>=0:
        x1 = (-b + (rz**0.5))/2*a
        print(f'La solución de X1 es: {x1}')                               # Mostramos en pantalla una de las soluciones.
        x2 = (-b - (rz**0.5))/2*a
        print(f'La solución de X2 es: {x2}')                               # Mostramos en pantalla otra de las soluciones.
    else:
        print('La solución no es un número real')                          # Mostramos en pantalla que no hay soluciones reales. 
# Hacemos los imports necesarios.

import sys
from math import sqrt

# Importamos los datos del sistema.

x1 = float(sys.argv[1]); y1 = float(sys.argv[2]); x2 = float(sys.argv[3]); y2 = float(sys.argv[4]); x3 = float(sys.argv[5]); y3 = float(sys.argv[6])

# Definimos los puntos y los términos que los componen.

punto1 = x1,y1; punto2 = x2,y2; punto3 = x3,y3

# Definimos operaciones matemáticas estándar para el programa.

xs1 = pow((x1-x2),2); ys1 = pow((y1-y2),2); xs2 = pow((x1-x3),2); ys2 = pow((y1-y3),2)

# Definimos la formula para cada uno de los casos.

sumadist1 = sqrt(xs1+ys1); sumadist2 = sqrt(xs2+ys2)

# Mostramos en pantalla las soluciones según cual esté más cerca del punto 1.

if sumadist1<sumadist2:
    print(f'El punto más cercano a {punto1} es {punto2} con una distancia de {sumadist1}')
else:
    print(f'El punto más cercano a {punto1} es {punto3} con una distancia de {sumadist2}')
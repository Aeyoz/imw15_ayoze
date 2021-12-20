import sys
n = int(sys.argv[1])
def factoriales(n):
    if (n==0):
        return 1
    else:
        return n * factoriales(n-1)
print(f'El factorial de {n} es {factoriales(n)}')

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero

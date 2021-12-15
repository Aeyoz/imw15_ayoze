import sys

n = int(sys.argv[1])


if n > 0:
    j = 0
    sum = 0
    for i in range(1, n + 1):
        j = i**2
        sum = j + sum
    print(f'La suma de cada uno de los terminos de {n} es {sum}')
else:
    print('El número no es válido')
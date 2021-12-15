import sys

x = int(sys.argv[1])

y = int(sys.argv[2])

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
    print('El numero no es valido')
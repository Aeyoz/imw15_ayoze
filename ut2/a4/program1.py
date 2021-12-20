import sys

dni = int(sys.argv[1])

div = dni % 23

def id(dni):
    if len(str(dni)) == 8 and dni > 0:
        if div == 0:
            print(f'Su DNI es {dni}T')
        elif div == 1:
            print(f'Su DNI es {dni}R') 
        elif div == 2:
            print(f'Su DNI es {dni}W') 
        elif div == 3:
            print(f'Su DNI es {dni}A') 
        elif div == 4:
            print(f'Su DNI es {dni}G') 
        elif div == 5:
            print(f'Su DNI es {dni}M') 
        elif div == 6:
            print(f'Su DNI es {dni}Y') 
        elif div == 7:
            print(f'Su DNI es {dni}F') 
        elif div == 8:
            print(f'Su DNI es {dni}P') 
        elif div == 9:
            print(f'Su DNI es {dni}D') 
        elif div == 10:
            print(f'Su DNI es {dni}X') 
        elif div == 11:
            print(f'Su DNI es {dni}B') 
        elif div == 12:
            print(f'Su DNI es {dni}N') 
        elif div == 13:
            print(f'Su DNI es {dni}J') 
        elif div == 14:
            print(f'Su DNI es {dni}Z') 
        elif div == 15:
            print(f'Su DNI es {dni}S') 
        elif div == 16:
            print(f'Su DNI es {dni}Q') 
        elif div == 17:
            print(f'Su DNI es {dni}V') 
        elif div == 18:
            print(f'Su DNI es {dni}H') 
        elif div == 19:
            print(f'Su DNI es {dni}L') 
        elif div == 20:
            print(f'Su DNI es {dni}C') 
        elif div == 21:
            print(f'Su DNI es {dni}K') 
        elif div == 22:
            print(f'Su DNI es {dni}E') 
    else:
        print(f'El formato de {dni} no es válido porque no tiene 8 caracteres o es negativo')
id(dni)

# Programa elaborado por: Ayoze Hernández, Angel David y David Quintero
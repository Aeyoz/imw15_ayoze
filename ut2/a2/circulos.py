# Hacemos los imports necesarios

import sys
from math import pi

# Definimos las operaciones matemáticas

r = float(sys.argv[1])                  # Importamos los datos del sistema
d = 2*r                                 # Función matemática del diámetro
p = 2*pi*r                              # Función matemática del perímetro
a = pi * r**2                           # Función matemática del área

# Construimos el menú de opciones llamado options.

def options():
    exit = False
    while not exit:
        print('''
        ¿Qué acción desear realizar?
        1. Calcular diámetro de la circunferencia.
        2. Calcular perímetro de la circunferencia.
        3. Calcular el área del circulo.
        4. Salir
        ''')

# Definimos las acciones que se pueden realizar dentro del menú

        accion = input('')
        if accion == '1':
            print(f'El diámetro de la circunferencia es de: {d}')
        elif accion == '2':
            print(f'El perímetro de la circunferencia es de: {p}')
        elif accion == '3':
            print(f'El área de la circunferencia es de: {a}')
        elif accion == '4':
            print('Que tenga un buen día!')
            exit = True
        else:
            print('Error')

# Hacemos un llamado al menu predefinido para su ejecución.

options()
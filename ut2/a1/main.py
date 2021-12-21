# Importamos datos de entrada desde la linea de comando

import sys                          
n = int(sys.argv[1])

# Definimos una funcion que nos da el cambio.

def cambios(a,b):                   
    return(a//b)

# Definimos una funcion que nos devuelve el resto.

def restos(a,b):                    
    return(a%b)

if n>=50:                           # Devuelve los billetes de 50€
    cambio1 = cambios(n,50);      resto = restos(n,50);      n = resto     ;print(f'Le corresponden {cambio1} billetes de 50€')

if n >= 20:                         # Devuelve los billetes de 20€
    cambio2 = cambios(n,20);      resto = restos(n,20);      n = resto     ;print(f'Le corresponden {cambio2} billetes de 20€')

if n >= 10:                         # Devuelve los billetes de 10€
    cambio3 = cambios(n,10);      resto = restos(n,10);      n = resto     ;print(f'Le corresponden {cambio3} billetes de 10€')

if n >= 5:                          # Devuelve los billetes de 5€
    cambio4 = cambios(n,5);       resto = restos(n,5);       n = resto     ;print(f'Le corresponden {cambio4} billetes de 5€')

if n<=5 and n>=2:                   # Devuelve las monedas de 2€
    cambio5 = cambios(n,2);       resto = restos(n,2);       n = resto     ;print(f'Le corresponden {cambio5} monedas de 2€')

if n!=0:                            # Devuelve las monedas de 1€
    print(f'Le corresponden {n} monedas de 1€')
# Programa desarrollado por Ayoze Hernández Díaz

# Importamos la libreria de sys para poder pasar datos al programa desde la línea de comandos
import sys 

# Definimos una lista con las vocales

list = ["a","e","i","o","u","A","E","I","O","U"]

# Función para contar vocales

def num_vowels(cadena):
    count = 0
    for i in cadena:
        if i in list:
            count = count + 1
    return(count)

# Función para contar los espacios en blanco    

def num_whitespaces(cadena):
    spaces = 0
    for i in cadena:
        if i.isspace():
            spaces = spaces + 1
    return(spaces)

# Función para contar los dígitos

def num_digits(cadena):
    digits = 0
    for i in cadena:
        if i.isdigit():
            digits = digits + 1
    return(digits)

# Función para contar las palabras

def num_words(cadena):
    words = 0
    splitting = cadena.split()
    for i in splitting:
        if i.isalpha():
            words = words + 1
    return(words)

# Función para devolver la frase al revés

def reverse(cadena):
    return(cadena[::-1])

# Función para ver la longitud de la frase

def length(cadena):
    return(len(cadena))

# Función para partir la frase en 2

def halfs(cadena):
    ini = cadena[:len(cadena)//2]
    end = cadena[len(cadena)//2:]
    phrase = f"{ini} | {end}"
    return(phrase)

# Función para convertir las vocales en mayúsculas

def upper_vowels(cadena):
    string2 = ""
    for i in cadena:
        if (i.islower() == True) and i in list:
            string2 = string2 + (i.upper())
        else:
            string2 = string2 + i
    return(string2)

# Función para ordenar las palabras alfabeticamente

def sorted_by_words(cadena):
    lista = cadena.split()
    lista.sort()
    transform = (str(lista)[1:-1])
    ordenados = transform.replace(",","")
    return(ordenados.replace("'",""))

# Función para contar la longitud de cada palabra

def length_of_words(cadena):
    string3 = cadena.split()
    longs = []
    for i in string3:
        longs.append(len(i))
    transform = (str(longs)[1:-1])
    return(transform.replace(",",""))


if __name__ == '__main__':
    cadena = str(sys.argv[1])
    print('Number of vowels:', num_vowels(cadena))
    print('Number of whitespaces:', num_whitespaces(cadena))
    print('Number of digits:', num_digits(cadena))
    print('Number of words:', num_words(cadena))
    print('Reverse of text:', reverse(cadena))
    print('Length of text:', length(cadena))
    print('Halfs of text:', halfs(cadena))
    print('Text with uppercased vowels:', upper_vowels(cadena))
    print('Sorted by words:', sorted_by_words(cadena))
    print('Length of words:', length_of_words(cadena))
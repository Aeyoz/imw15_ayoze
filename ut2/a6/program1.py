import sys

cadena = str(sys.argv[1])

def count_words(cadena):
    sumary = {}
    string = cadena.split()
    for i in string:
        valor = i
        veces = 1
        if sumary.get(valor) == 1:
            veces = veces + 1
            sumary[i] = veces    
        else:
            sumary[i] = veces
    phrase = str(sumary).replace("'","").replace("{"," ").replace("}","").replace(",","\n")
    return(phrase)        

print(count_words(cadena))
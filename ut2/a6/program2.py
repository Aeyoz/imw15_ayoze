# Elaborado por Ayoze Hernández Díaz 2º ASIR
# Definimos un menu que albergue las opciones que se puedan ejecutar en el diccionario
def menu():
# Definimos el diccionario phone_book
    phone_book = {}
    exit = False
    while not exit:
# Mostramos las opciones por pantalla
        print('''
        1.- Mostrar contactos.
        2.- Añadir contacto.
        3.- Borrar contacto.
        4.- Salir
        ''')
# Definimos un metodo de entrada para las opciones
        accion = input('¿Qué desea hacer?: ')
# Definimos cada opción
# Opción 1: Muestra los contactos        
        if accion == '1':
            phrase = str(phone_book)
# Si el diccionario esta vacio muestra la frase "No hay contactos"            
            if phone_book == {}:
                print("No hay contactos")
# Si el diccionario tiene algun elemento muestra todos los elementos                
            else:
                print(phrase.replace("'","").replace("{","").replace("}","").replace(",","\n"))
# Opción 2: Añadir contactos
        elif accion == '2':
# Definimos nombre de contacto y numero            
            contact_name = input("Nombre del contacto: ")
            contact_number = input("Numero del contacto: ")
# Un usuario solo puede tener un número y un número solo puede pertenecer a un usuario
# Comprueba que el usuario o el numero existen, en caso de que una de las condiciones sea positiva no añade al usuario            
            if phone_book.get(contact_name) or phone_book.get(contact_number):
                print("Ese usuario ya existe")
# Añadimos el usuario y numero
            else:
                phone_book[contact_name] = contact_number
# Opción 3: Borra contactos
        elif accion == '3':
# Definimos un metodo de entrada para elegir el usuario a borrar
            contact_name = input("¿Que contacto quiere borrar? ")
# Comprueba que el usuario exista            
            if phone_book.get(contact_name) == None:
                print("Ese contacto no existe")
# Borra el usuario            
            else:
                del(phone_book[contact_name])
                print("Usuario borrado con exito")
# Sale del programa        
        elif accion == '4':
            print('Que tenga un buen día!')
            exit = True
# Si se introduce cualquier cosa que no sea una de las cuatro opciones imprime error por pantalla        
        else:
            print('Error')
# Llamamos al menú            
menu()
def añadir(lista):
    nombre=input("Introduzca el nombre: ")
    telefono=input("Introduzca el telefono: ")
    telefono=int(telefono)
    contacto={
        "nombre": nombre,
        "telefono": telefono
    }
    lista.append(contacto)


def buscar(lista):
    nombre=input("Introduzca el nombre: ")
    telefono=input("Introduzca el telefono: ")
    contacto={
        "nombre": nombre,
        "telefono": telefono
    }
    if contacto not in lista:
        print(contacto)
    else:
        print("El contacto no existe...")


def editar(lista):
    cont=0
    nombre=input("Introduzca el nombre: ")
    telefono=input("Introduzca el telefono: ")
    contacto={
        "nombre": nombre,
        "telefono": telefono
    }
    if contacto not in lista:
        nombre2=input("Introduzca el nuevo nombre: ")
        telefono2=input("Introduzca el nuevo telefono: ")
        contacto2={
            "nombre": nombre2,
            "telefono": telefono2
        }
        if contacto==contacto2:
            lista[cont].update(contacto2)
            print("El contacto fue actualizado")
        cont+=1
    else:
        print("El contacto no existe...")

def eliminar(lista):
    nombre=input("Introduzca el nombre: ")
    telefono=input("Introduzca el telefono: ")
    contacto={
        "nombre": nombre,
        "telefono": telefono
    }
    if contacto not in lista:
        lista.remove(contacto)
        print("el contacto se ha eliminado")
    else:
        print("El contacto no existe...")

def mostrar(lista):
    for aux in lista:
        print(aux)

def menu():
    print("-----MENU-----")
    print("1. Añadir un contacto")
    print("2. Buscar un contacto")
    print("3. Editar un contacto")
    print("4. Eliminar un contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")
    eleccion=input("Elija una opcion: ")
    return int(eleccion)

def switch(lista):
    eleccion=0
    while eleccion != 6:
        eleccion=menu()
        if(eleccion==1):
            añadir(lista)
        elif(eleccion==2):
            buscar(lista)
        elif(eleccion==3):
            editar(lista)
        elif(eleccion==4):
            eliminar(lista)
        elif(eleccion==5):
            mostrar(lista)
        elif(eleccion==6):
            print("Saliendo del sistema...")
        else:
            print("Opcion inexistente...")

lista=[]
switch(lista)
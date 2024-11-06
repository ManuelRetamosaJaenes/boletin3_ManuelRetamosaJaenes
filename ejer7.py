def añadirLibro(libro):
    archivo = open('libros.txt', 'r')
    libros = archivo.read().splitlines()
    archivo.close()
    libros.append(libro)
    archivo = open('libros.txt', 'w')
    for l in libros:
        archivo.write(l + '\n')
    archivo.close()
    return libros

def primerLibro(lista):
    if lista:
        return lista[0]
    else:
        return "No hay libros en la lista."

def datos():
    nuevoLibro = input("Introduce el título del nuevo libro que has leído: ")
    lista = añadirLibro(nuevoLibro)
    print("Lista completa de libros leídos:")
    for libro in lista:
        print(libro)
    primerLibro = primerLibro(lista)
    print(primerLibro)

datos()

def revisar_coleccion(coleccion):
    lista={} 
    lista2=[]
    lista=set(coleccion)
    lista2=list(lista)
    return lista2

coleccion=['Mona Lisa', 'El Grito', 'Mona Lisa', 'La Noche Estrellada', 'Las Meninas', 
'Guernica', 'La Última Cena', 'La Creación de Adán', 'La Persistencia de la Memoria', 
'La Libertad guiando al pueblo', 'El Beso', 'Nacimiento de Venus', 
'El Jardín de las Delicias', 'La Joven de la Perla', 'El David', 
'Los Girasoles', 'La Gran Ola de Kanagawa', 'La Ronda Nocturna', 'American Gothic', 
'Los Jugadores de Cartas', 'La Noche Estrellada', 'La Última Cena', 'Guernica', 
'Las Meninas', 'La Persistencia de la Memoria', 'Mona Lisa']
print("\n"+"Colección antes de la revisión:"+"\n")
print(coleccion)
print("\n"+"Colección después de la revisión:"+"\n")
print(revisar_coleccion(coleccion))
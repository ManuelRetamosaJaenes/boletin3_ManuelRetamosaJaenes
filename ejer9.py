def agregar_experiencia(perfil_laboral, nueva_experiencia):
    perfil_laboral.get("experiencias").append(nueva_experiencia)
    return perfil_laboral


def generar_cv_reducido(perfil_laboral):
    print("CV de "+perfil_laboral.get("nombre")+" "+perfil_laboral.get("apellido"))
    print("Edad: "+str(perfil_laboral.get("edad"))+", Ciudad: "+perfil_laboral.get("ciudad"))
    print("Experiencia: "+str(perfil_laboral.get("experiencias")))


nombre=input("Introduzca el nombre: ")
apellido=input("Introduzca el apellido: ")
edad=input("Introduzca la edad: ")
edad=int(edad)
ciudad=input("Introduzca la ciudad: ")
experiencias=[]
perfil_laboral={
    "nombre": nombre,
    "apellido": apellido,
   "edad": edad,
    "ciudad": ciudad,
    "experiencias": experiencias
}


agregar_experiencia(perfil_laboral, "hola")
generar_cv_reducido(agregar_experiencia(perfil_laboral, "mundo"))

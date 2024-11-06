def gestionarInformacion(datosPersonales):
    nombre, edad, ciudad=datosPersonales

    print("El nombre es "+nombre+", la edad es "+str(edad)+" y la ciudad de residencia es "+ciudad)

def calcularAño(datosPersonales):
    año=2024-datosPersonales[1]
    return año

def datosModificados(datosPersonales):
    nombre, nacimiento, ciudad=datosPersonales

    print("El nombre es "+nombre+", el año de nacimiento es "+str(nacimiento)+" y la ciudad de residencia es "+ciudad)


datosPersonales=("pepe", 19,"sevilla")
gestionarInformacion(datosPersonales)
datosPersonales=("pepe", calcularAño(datosPersonales),"sevilla")
datosModificados(datosPersonales)
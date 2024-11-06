texto=input("Introduzca un texto de 10 palabras: ")
numCaracteres=len(texto)
numCaracteresSinEspacios=0
lista=texto.split(" ")
numVocales=0
cambio=""
resultado=" ".join(lista[1:])
for aux in texto:
    if aux!=" ":
        numCaracteresSinEspacios+=1
    if aux=="a" or aux=="e" or aux=="i" or aux=="o" or aux=="u":
        numVocales+=1
    if aux == aux.upper():
        cambio+=aux.lower()
    if aux==aux.lower():
        cambio+=aux.upper()
print("El numero de caracteres es "+str(numCaracteres))
print("El numero de caracteres sin espacios es "+str(numCaracteresSinEspacios))
print("El numero de vocales es "+str(numVocales))
print("El numero de palabras es "+str(len(lista)))
print("El texto sin la primera palabra es "+resultado)
print("El texto con guiones en lugar de espacios es "+texto.replace(" ","-"))
print("El texto cambiado es "+cambio)
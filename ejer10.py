def crear_codigo_secreto(mensaje):
    repr_bin=""
    repr_bin_primero=mensaje[0]
    repr_bin_ultimo=mensaje[len(mensaje-1)]
    cont=0
    while(cont<len(mensaje)):
        if(cont%2==0):
            repr_bin+=str(mensaje[cont])
        cont+=1
    repr_hex=repr_bin.encode('utf-8')    
    repr_hex=repr_hex.hex()
    repr_bin_primero=bin(repr_bin_primero)
    repr_bin_ultimo=bin(repr_bin_ultimo)
    print(str(repr_bin_primero)+str(repr_bin)+str(repr_bin_primero)+str(repr_bin_ultimo))
    


crear_codigo_secreto(b'Este es un mensaje secreto')
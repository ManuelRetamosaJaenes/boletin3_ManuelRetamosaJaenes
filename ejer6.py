palabra_adivinar="pepe"


def adivinar_palabra(letra_prueba, palabra_intento, palabra_adivinar):
    acierto=False
    acierto2=False
    for aux in palabra_adivinar:
        if letra_prueba == aux:
            acierto=True

    print("¿La letra de prueba se encuentra en la palabra? ["+acierto+"]")
    if palabra_intento == palabra_adivinar:
        acierto2=True
    print("El jugador gana: ["+acierto2+"]")


letra=input("Introduzca una letra: ")
letra=str(letra)
palabra_intento=input("Introduzca una palabra: ")
adivinar_palabra(letra, palabra_intento, palabra_adivinar)

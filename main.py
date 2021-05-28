#Llevar  a  cabo  un  programa  completo Toque & Fama en  el  lenguaje  Python
# utilizando  todos  los elementos básicos que provee el lenguaje
# y sus tipos de datos básicos y compuestos (Condicionales, Ciclos, E/S).

import random

#SE CREAN VARIABLES IGUAL A 0 PARA QUE CUENTEN LAS GANADAS LAS PERDIDAS Y LAS JUGADAS TOTALES

jugando = 0  #ESTA VARIABLE SIRVE PARA QUE EL VOLVER A JUGAR INICIE EN 0
Ganadas = 0  #ESTA VARIABLE CONTARA DE 0 LAS GANADAS
Perdidas = 0  #ESTA VARIABLE CONTARA DE 0 LAS PERDIDAS
Jugadas_Totales = 0  #ESTA VARIABLE CONTARA DE 0 LAS JUGADAS TOTALES

while jugando == 0:  #ESTE CICLO WHILE SERIVARA PARA VOLVER A JUGAR Y SE ADJUNTARA EL CODIGO DEL JUEGO
    jugando -= 1
    Jugadas_Totales += 1

    print("BIENVENIDO AL JUEGO TOQUE & FAMA")
    print("______________________________________________")
    print(
        "El juego toque y fama consiste en que el computador elige aleatoriamente una secuencia"
    )
    print(
        "de n dígitos. El jugador, en cada turno, intenta adivinar dicha secuencia. El computador,"
    )
    print(
        "responde el número de toques y famas que el intento tuvo, sin decir a qué dígitos"
    )
    print(
        "corresponden, de esta manera, el jugador podrá ir intuyendo la secuencia hasta adivinarla"
    )
    #print("__________________________________________________")
    print("")
    print(
        "EL NUMERO RANDOM PUEDE VARIAR ENTRE 4 y 9 DIGITOS,SI NO TE PREGUNTARA DE NUEVO!!"
    )
    print("")

    usuario = 0
    while usuario < 4 or usuario > 9:  #SE GENERA ESTE CICLO PARA QUE EL USUARIO NO PONGA NUMEROS MENOR 4 NI NUMEROS MAYOR 9
        usuario = int(input("Ingrese la cantidad de numeros que tendra: "))
        numero_incongito = ""  #Generamos una variable como incognita que se usara mas adelante para insertar los numeros random
        for i in range(
                usuario
        ):  #Se crea este ciclo que generara un rango de numeros en el numero random
            numero_random = random.randint(
                1, 9
            )  #creamos la variable adjunto a la funcion de la libreria random que me generara un rango del 1 al 9
            while str(numero_random) in numero_incongito:
                numero_random = random.randint(1, 9)
            numero_incongito += str(
                numero_random
            )  #Se le suma el numero random converitdo en string al numero incongnito
    print(" ")
    print("AHORA INGRESARAS LA CANTIDAD DE INTENTOS")
    print(" ")
    ingresar_intentos = int(input("Ingrese intentos: "))

    print(" ")
    intentos = 0
    intentos_usuario = 1  #CONTARA LA CANTIDAD DE INTENTOS DEL USUARIO

    while intentos < ingresar_intentos:
        ingresar_adivinanza = input(f"Intento {intentos_usuario}:  ")
        fama = 0  #CONTARA LAS FAMAS QUE LLEVA EL JUGADOR
        toque = 0  #CONTARA LOS TOQUES
        if len(ingresar_adivinanza) != len(
                numero_incongito
        ):  #ESTO VA A COMPROBAR SI EL NUMERO ES IGUAL AL LARGO DEL NUMERO
            print("ERROR")
        else:
            for contador in range(usuario):
                if ingresar_adivinanza[contador] == numero_incongito[
                        contador]:  #SI EL NUMERO ES IGUAL A LA POSICION Y NUMERO ENTONCES SERA FAMA
                    fama += 1
                elif ingresar_adivinanza[
                        contador] in numero_incongito:  #SI EL NUMERO ES IGUAL AL NUMERO INGRESADO PERO NO AL DE LA POSICON SERA TOQUE
                    toque += 1
            print(f'Toques:{toque}-Famas:{fama}')
        intentos += 1  #SE LE SUMA EL INTENTO

        if numero_incongito == ingresar_adivinanza:  #SI EL NUMERO ES IGUAL NUMERO INGRESADO ENTONCES GANARA
            print("Felicidades ! has acertado en", intentos_usuario,
                  "intentos")
            Ganadas += 1
            break  #SE USA EL BREAK PARA QUE NO SIGA GENERANDO INTENTOS Y PASE AL A SIGENTE PREGUNTA PARA VOLVER A JUGAR
        if ingresar_intentos == intentos:  #SI EL INTENTO LLEGA A IGUAL AL INTENTO INGRESADO ENTONCES TERMINARA EL JUEGO
            print("Fin del Juego")
            print("La secuencia era:", numero_incongito)
            Perdidas += 1
            break
        intentos_usuario += 1
    pregunta = int(input("¿Desea jugar nuevamente? 0:NO & 1:SI: "))
    jugando += 1
    if pregunta == 0:  #SI ES IGUAL 0 MOSTRARA LAS ESTADISTICAS
        print("Muchas Gracias por jugar")
        print(
            f"Jugadas:{Jugadas_Totales}-Ganadas:{Ganadas}-Perdidas:{Perdidas}"
        )  #MOSTRARA LOS ESTADISTICA DE LAS PARTIDAS !
        break
    elif pregunta == 1:  #SI ES IGUAL A 1 SE REPETIRA EL CODIGO !
        print(" ")
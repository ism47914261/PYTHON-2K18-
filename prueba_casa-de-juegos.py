# coding=utf8

from random import randint
from os import system
system('clear')

# Inicializaciones
salir = "N"
num_aleatorio=randint(1,10)
acierto=0
oportunidades=0
num_repetido= 0

while ( salir=="N" ):
    # Hago cosas
    adivina1=input("Introduzca el numero que cres que es del 1 al 10: ")
    if (adivina1 == num_aleatorio):
        print "Muy bien has ganado a la primera 100€"
        acierto= acierto + 1
    else:
        print "Has gastado un acierto"
        oportunidades= oportunidades + 1
        adivina2=input("Introduzca el numero que cres que es del 1 al 10: ")
        
        if (adivina2 == num_aleatorio):
            print "Has acertado a la segunda has ganado 100€"
            acierto= acierto + 1
        else:
            oportunidades= oportunidades + 1
            print "Has gastado otro acierto"
            adivina3=input("Introduzca el numero que cres que es del 1 al 10: ")
           
            if (adivina3 == num_aleatorio):
                print "Has acertado a la tercera, has ganado 100€"
                acierto= acierto + 1
                
            else:
                print "Has gastado todas tus oportunidades, por lo tanto friegas los platos"
                oportunidades= oportunidades + 1

 

    # Incremento

    
     # Activo indicador de salida si toca
    if (acierto == 1) or (oportunidades == 3): # Condición de salida
        salir = "S"



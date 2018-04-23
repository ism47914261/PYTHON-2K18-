# coding=utf8

from random import randint
from os import system
system('clear')

# Inicializaciones
salir = "N"
importe=100
contador=0

def menu():
    print ("\t1 - Jugar")
    print ("\t2 - Salir")


menu()

while ( salir=="N" ):
    # Hago cosas
    opcion_menu=input("Introduzca una opcion: ")
    if (opcion_menu == 1):
        cara_random=randint(1,2)
        cara_cruz=cara_random
        apuesta=input("Introduzca cuanto dinero quieres apostar el minimo es 10€ y el maximo es tu saldo: ")
        cara_o_cruz=input("Introduzca que quiere cara (1) cruz (2): ")
        
        if (apuesta >= 10) and (apuesta <= importe):
            if (cara_o_cruz == cara_cruz):
                if (cara_cruz == 1):
                    print "Ha salido cara has acertado, por lo tanto GANAS"
                    importe= importe - apuesta
                    apuesta= apuesta*2
                    importe= importe + apuesta
                    print "Has ganado: ", apuesta, "su imoporte ahora es de: ", importe

                elif (cara_cruz == 2):
                    print "Ha salido cruz, has GANADO"
                    importe= importe - apuesta
                    apuesta= apuesta*2
                    importe= importe +  apuesta
                    print "Has ganado: ", apuesta, "su imoporte ahora es de: ", importe

            else:
                if (cara_cruz == 1):
                    importe= importe - apuesta
                    print "Ha salido cara, has PERDIDO"
                    print "Has perdido: ", apuesta, "su imoporte ahora es de: ", importe

                elif (cara_cruz == 2):
                    importe= importe - apuesta
                    print "Ha salido cruz, has PERDIDO"
                    print "Has perdido: ", apuesta, "su imoporte ahora es de: ", importe
                
    # Incremento
    contador= contador + 1
    
     # Activo indicador de salida si toca
    if (opcion_menu == 2) or (importe <=9): # Condición de salida
        salir = "S"


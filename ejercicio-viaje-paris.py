# coding=utf8

"""Desde su casa en Barcelona a París hay 1033 Km. 
1- Visualiza por pantalla el cuenta Kilómetro del ferrari de  Neymar  hasta que llega a París.
2- Cada  246 Km tiene que parar a repostar en una gasolinera. ¿Cuántas veces tendrá que parar?
3- Cada vez que llena el depósito se gasta  93€. ¿Cuánto dinero le cuesta volver a París?
"""


# Inicializaciones
salir = "N"
recorrido= 1033
contador_km= 246
viaje_gasolineras= 0
contador_dinero=0
coste_gasolinera= 93
km_que_quedan= 0

while ( salir=="N" ):
    # Hago cosas
    if (recorrido >= 246):
        recorrido= recorrido - contador_km
        viaje_gasolineras= viaje_gasolineras + 1
        contador_dinero= contador_dinero + coste_gasolinera


   
    # Incremento
    
    
     # Activo indicador de salida si toca
    if (recorrido < 246): # Condición de salida
        salir = "S"
print "El numero de veces que ha parado a repostar gasolina es :", viaje_gasolineras
print "El dinero que se ha gastado en volver a París es :", contador_dinero 


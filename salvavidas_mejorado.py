# coding=utf8


# Inicializaciones
salir = "N"
personas=60
botes=2
ida= 0
vuelta= 0
personas_restantes=780
personas_isla=0
total_personas=780

while ( salir=="N" ):
    # Hago cosas
    if (personas_restantes > 61):
        personas_restantes= personas_restantes - personas
        personas_isla= personas_isla + 60
        ida= ida + 2
        vuelta= vuelta + 2
        print "N. pasajeros barco: ", personas_restantes, "\n"
        
        print "pasajeros isla: ", personas_isla, "viajes de ida: ", ida, "viajes de vuelta: ", vuelta 
   
    elif (personas_restantes == 60):
        personas_restantes= personas_restantes - personas
        ida= ida + 2
        print "Quedan por salvar: ", personas_restantes, "VIAJES DE IDA: ", ida
   
    # Incremento
    
    
     # Activo indicador de salida si toca
    if (personas_restantes <= 0): # Condición de salida
        salir = "S"
        
viajes= ida + vuelta
print "Ya se han salvado todas las personas en un total de viajes de: ", viajes

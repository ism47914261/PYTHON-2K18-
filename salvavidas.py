# coding=utf8


# Inicializaciones
salir = "N"
personas=60
botes=2
total_personas=780
viajes=0
personas_restantes=780

while ( salir=="N" ):
    # Hago cosas
    if (personas_restantes >= 60):
        personas_restantes= personas_restantes - personas
        viajes= viajes + 1
        print "Quedan por salvar: ", personas_restantes, "NUMERO VIAJE: ", viajes

        
    # Incremento
    
    
     # Activo indicador de salida si toca
    if (personas_restantes <= 0): # Condición de salida
        salir = "S"
print "Ya se han salvado todas las personas en un total de viajes de: ", viajes

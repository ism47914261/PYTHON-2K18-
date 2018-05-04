import sense_hat

sense = sense_hat.SenseHat()
sense.clear()


def my_range(inici, fi, increment=1):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment
        
        
        
# Edit these variables to change key game parameters
green_color = (0,255,0)      # RGB color of column pixels

vuelta
x=0
y=0

"""
def my_range(inici, fi, increment=1):
    if (inici<=fi):  # seqüència ascendent
        while inici <= fi:
            #Retorna l'element actual del rang (llista)
            yield inici
            inici = inici + increment
    else:  # seqüència descendent
        while inici+1 != fi:
            #Retorna l'element actual del rang (llista)
            yield inici
            inici = inici + increment
"""


import sense_hat

sense = sense_hat.SenseHat()
sense.clear()
        
        
# Edit these variables to change key game parameters
green_color = (0,255,0)      # RGB color of column pixels

salir="N"
vuelta=0
x=0
y=0
max=7

while (salir=="N"):
  sense.set_pixel(y,x,green_color)
  x= x + 1
  
  if(x > max):
    salir="S"
    
salir="N"
vuelta=0
x=0
y=7
max=7

while (salir=="N"):
  sense.set_pixel(x,y,green_color)
  x= x + 1
  
  if(x > max):
    salir="S"


salir="N"
vuelta=0
x=0
y=7
max=0



while (salir=="N"):
  sense.set_pixel(x,y,green_color)
  y= y - 1
  
  if(y < max):
    salir="S"
    

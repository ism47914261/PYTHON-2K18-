import sense_hat

sense = sense_hat.SenseHat()
sense.clear()

# Edit these variables to change key game parameters
green_color = (0,255,0)      # RGB color of column pixels

x=0
y=0



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
x=7
y=7
max=0


while (salir =="N"):
  sense.set_pixel(y,x,green_color)
  x= x - 1
  
  if(x < max):
    salir="S"

salir="N"
vuelta=0
x=0
y=7
max=0


while (salir =="N"):
  sense.set_pixel(y,x,green_color)
  y= y - 1
  
  if(y < max):
    salir="S"
    

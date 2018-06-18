#Liam Collins
#graphing functions

from ggame import *
from math import sin, cos, tan

#Graphics
red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

blackCircle = CircleAsset(5,blackOutline,red)
blackLine = LineAsset(1000,0,blackOutline) 
blackVertLine = LineAsset(0,600,blackOutline)
text = TextAsset('Literature',fill=green, style='bold 40pt Times') 
blackXValues = LineAsset(0,15,blackOutline)
blackYValues = LineAsset(15,0,blackOutline)

Sprite(blackLine, (0,255))
Sprite(blackVertLine, (355,0))

X = 20
Y = 20

for i in range(-16,31):
    Sprite(blackXValues, (355+i*X,255))
    text = TextAsset(str(i),fill=black, style='bold 8pt Times')
    Sprite(text, (355+i*X,270))

for i in range(-30,30):
    Sprite(blackYValues, (350, 255+i*Y))
    text = TextAsset(str(-i),fill=black, style='bold 8pt Times')
    Sprite(text, (370,255+i*Y))

#user input values
f = '3*x+(x)**2'
for i in range(-100,100):
    Sprite(blackCircle, (350+i*X,250-Y*eval(f.replace('x',str(i)))))


App().run()

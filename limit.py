#Liam Collins
#limit.py

from ggame import *
from math import sin, cos, tan

#Graphics
red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

blackCircle = CircleAsset(5,blackOutline,black) 
blackLine = LineAsset(1000,0,blackOutline) 
blackVertLine = LineAsset(0,500,blackOutline)
text = TextAsset('Literature',fill=green, style='bold 40pt Times') 
blackPlaceHolder = LineAsset(0,15,blackOutline)

Sprite(blackLine, (0,255))
Sprite(blackVertLine, (355,0))

X = 20
Y = 10

for i in range(-16,31):
    Sprite(blackPlaceHolder, (355+i*X,255))
    text = TextAsset(str(i),fill=black, style='bold 8pt Times')
    Sprite(text, (355+i*X,270))

f = str(input('f(x) = '))
for i in range(-100,100):
    Sprite(blackCircle, (350+i*X,250-Y*eval(f.replace('x',str(i)))))


App().run()

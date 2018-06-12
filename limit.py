#Liam Collins
#limit.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

#redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blackCircle = CircleAsset(5,blackOutline,black) #radius, outline, fill
blackLine = LineAsset(600,0,blackOutline) #x_endpoint, y_endpoint, lineStyle
blackVertLine = LineAsset(0,500,blackOutline)
text = TextAsset('Literature',fill=green, style='bold 40pt Times') #text, other options

X = 5
Y = 5

f = '(x)**2 + 5'
for i in range(-100,100):
    Sprite(blackCircle, (250+i*X,250-eval(f.replace('x',str(i)))))
    print(eval(f.replace('x',str(i*X))))

Sprite(blackLine, (0,250))
Sprite(blackVertLine, (255,0))


App().run()
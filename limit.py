#Liam Collins
#limit.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(75,75), (100,100), (50,100)],blackOutline,red) #endpoint, outline, fill
text = TextAsset('Literature',fill=green, style='bold 40pt Times') #text, other options

Sprite(redRectangle, (100,300))
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,50))
Sprite(blackLine)
Sprite(redTriangle, (175,200))
Sprite(text, (200,400))

App().run()

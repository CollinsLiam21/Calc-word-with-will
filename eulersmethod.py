#Liam Collins
#Euler's Method

def euler(x,y,finalx,n):
    fderiv = '2y + x'
    dx = (finalx - x)/n
    for i in range(0,n):
        fderiv.replace('y',str(y))
        fderiv.replace('x',str(x))
        dy = eval(fderiv)*dx
        x += dx
        y += dy
        print(x,y)
    
euler(1,2,3,4)

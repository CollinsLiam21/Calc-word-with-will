#Liam Collins
#Euler's Method

def euler(x,y,finalx,n):
    fderiv = '-1*(y) + 2*(x)'
    dx = (finalx - x)/n
    for i in range(0,n):
        fderiv.replace('y',str(y))
        fderiv.replace('x',str(x))
        dy = eval(fderiv)*dx
        x += dx
        y += dy
        print('(',round(x,4),',',round(y,4),')')
        
#user input
euler(2,3,1.5,10)

#Liam Collins
#Euler's Method

def euler(x,y,finalx,n):
    fderiv = '2*(y) + 1*(x)'
    dx = (finalx - x)/n
    for i in range(0,n):
        fderiv.replace('y',str(y))
        fderiv.replace('x',str(x))
        dy = eval(fderiv)*dx
        print(dy)
        x += dx
        y += dy
        print('(',round(x,4),',',round(y,4),')')
    
euler(2,0,3,5)

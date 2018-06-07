#Liam Collins
#newton's method

def newtonMethod(x0):
    f = 'x**2 + x**1 + 5'
    h = 0.00001
    fn = f.replace('x',str(x0))
    fderiv = (f.replace('x',str(x0 + h))-f.replace('x',str(x0)))/h
    
    print(eval(fderiv))
    
    #xn = x0 - eval(f)/
    
    #print('f(x) = ',a,'x^',b,' + ',c,'x^',d,' + ',e,'     x0 =',x0)
    
    
    
    
    
newtonMethod(2)

#Liam Collins
#newton's method

def newtonMethod(x0):
    f = 'x**2 + x**1 + 5'
    h = 0.00001
    for i in range(0,10):
        fn = f.replace('x',str(x0))
        defderiv = x0 + h
        fderiv = (eval(f.replace('x',str(defderiv)))-eval(f.replace('x',str(x0))))/h
        x0 = fderiv
    
    
    #xn = x0 - eval(f)/
    
    #print('f(x) = ',a,'x^',b,' + ',c,'x^',d,' + ',e,'     x0 =',x0)
    
    
    
    
    
newtonMethod(2)

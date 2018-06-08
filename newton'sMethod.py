#Liam Collins
#newton's method

import math

def newtonMethod(x0):
    f = '0*(x)**4 + (.5*x)**3 + 2*(x)**2 + (x)**1 + 3'
    h = 0.00001
    xvalues = []
    for i in range(0,40):
        fn = eval(f.replace('x',str(x0)))
        defderiv = x0 + h
        fderiv = (eval(f.replace('x',str(defderiv)))-eval(f.replace('x',str(x0))))/h
        x0 = x0 - fn/fderiv
        xvalues.append(x0)
    if round(xvalues[-1],7) == round(xvalues[-2],7):
        print('zero at x =',round(x0,7))
    else:
        print('No Zero')
    
newtonMethod(0)

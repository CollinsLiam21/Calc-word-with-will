#Liam Collins
#newton's method

from math import sin, cos, tan

def newtonMethod(x0):
    #f = '0*(x)**4 + 0*(.5*x)**3 + 1*(x)**2 + 0*(x)**1 + 0'
    f = 'sin(x)'
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
    
newtonMethod(0.2)

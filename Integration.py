import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import integrate

def rectanglerule(f, a, b, rectangles):
    total_area = 0
    a = float(a)
    b = float(b)
    rectangles = float(rectangles)
    i = (b-a)/rectangles
    trailing_x = a
    leading_x = a+i
    while (a <= leading_x <= b) or (a >= leading_x >= b):
        area = f((trailing_x+leading_x)/2)*i
        total_area += area

        leading_x += i
        trailing_x += i

    return total_area

# defined function
def f(x):
    return x**2

if __name__ == "__main__":

    # default number of intervals for rectangle rule
    Nint = 100

    # default number of points for gaussian quadrature
    Npoints = 1

    # bounds
    a = 1
    b = 2
    
    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    if '-Nint' in sys.argv:
        p = sys.argv.index('-Nint')
        Nint = int(sys.argv[p+1])
    if '-Npoints' in sys.argv:
        p = sys.argv.index('-Npoints')
        Npoints = int(sys.argv[p+1]) 
    if '-Ubound' in sys.argv:
        p = sys.argv.index('-Ubound')
        a = int(sys.argv[p+1])
    if '-Lbound' in sys.argv:
        p = sys.argv.index('-Lbound')
        a = int(sys.argv[p+1]) 
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-Nint] number of intervals" % sys.argv[0])
        print
        sys.exit(1)  

    quadval, quaderr = integrate.fixed_quad(f, a, b, n = Npoints)

    print(quadval)

    recval = rectanglerule(f, a, b, Nint)

    print(recval)





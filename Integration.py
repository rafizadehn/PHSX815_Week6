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
    return 2*x*np.sin(x**2)

# analytical integral of defined function
def intf(x, a, b):
    return -np.cos(b**2) + np.cos(a**2)

if __name__ == "__main__":

    # default number of intervals for rectangle rule
    Nint = 100

    # default number of points for gaussian quadrature
    Npoints = 1

    # bounds
    a = 0
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
    
    # find the area using quadratures for desired number of evalutaion points
    quadval, quaderr = integrate.fixed_quad(f, a, b, n = Npoints)

    print(f"method by quadratures: {quadval}")

    # find the area using the rectangular rule for desired number of subintervals
    recval = rectanglerule(f, a, b, Nint)

    print(f"rectangle rule: {recval}")

    # analytical evaluation of the integral
    anval = intf(f, a, b)

    print(f"analytical solution: {anval}")

    ####################
   
    ## Quadratures vs Analytical Solution
    quads = []

    intervals = np.arange(1, 10, 1)

    for i in intervals:
        quadval, quaderr = integrate.fixed_quad(f, a, b, n=i)
        analy_val = intf(f, a, b)
        diff_quadval = ((quadval - analy_val)/analy_val)*100
        quads.append(diff_quadval)

    plt.figure()
    plt.scatter(intervals, quads)
    plt.xlim([0, max(intervals)])
    plt.xlabel("Number of Evaluation Points", fontsize = 15)
    plt.ylabel("% Error", fontsize = 15)
    plt.title("Quadratures compared to Analytical Solution", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.show()
   
    ## Rectangular Rule vs Analytical Solution
    recs = []

    intervals = np.arange(1, 500, 10)
    for i in intervals:
        recval = rectanglerule(f, a, b, i)
        analy_val = intf(f, a, b)
        diff_recval = ((recval - analy_val)/analy_val)*100
        recs.append(diff_recval)

    plt.figure()
    plt.scatter(intervals, recs)
    plt.xlim([0, max(intervals)])
    plt.xlabel("Number of Sub-Intervals", fontsize = 15)
    plt.ylabel("% Error", fontsize = 15)
    plt.title("Rectangle Rule compared to Analytical Solution", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.show()
 
    ## Rectangular Rule vs Quadratures
    recs1 = []
    recs2 = []

    intervals = np.arange(1, 500, 10)
    for i in intervals:
        recval = rectanglerule(f, a, b, i)
        quad_val1 = integrate.fixed_quad(f, a, b, n=1)[0]
        diff_recval1 = recval - quad_val1
        recs1.append(diff_recval1)
        
        quad_val2 = integrate.fixed_quad(f, a, b, n=2)[0]
        diff_recval2 = recval - quad_val2
        recs2.append(diff_recval2)

    plt.figure()
    plt.scatter(intervals, recs1)
    plt.xlim([0, max(intervals)])
    plt.xlabel("Number of Sub-Intervals", fontsize = 15)
    plt.ylabel("Rectangle Rule - Quadratures", fontsize = 15)
    plt.title("Methods Comparison (n=1)", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.show()
    
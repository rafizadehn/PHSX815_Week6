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
    Nquads = 1

    # bounds
    a = 0
    b = 2
    
    # MC points
    Npoints = 1000

    # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    if '-Nint' in sys.argv:
        p = sys.argv.index('-Nint')
        Nint = int(sys.argv[p+1])
    if '-Npoints' in sys.argv:
        p = sys.argv.index('-Npoints')
        Npoints = int(sys.argv[p+1]) 
    if '-Nquads' in sys.argv:
        p = sys.argv.index('-Nquads')
        Nquads = int(sys.argv[p+1])
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
    quadval, quaderr = integrate.fixed_quad(f, a, b, n = Nquads)

    print(f"method by quadratures: {quadval}")

    # find the area using the rectangular rule for desired number of subintervals
    recval = rectanglerule(f, a, b, Nint)

    print(f"rectangle rule: {recval}")

    ####################
   
    #### Monte Carlo Integration

    ar = np.zeros(Npoints)
    
    for i in range(len(ar)):
        ar[i] = np.random.uniform(a,b)

    integral = 0.0

    for i in ar:
        integral += f(i)

    ans = (b-a)/float(Npoints)*integral

    print(f"monte carlo solution: {ans}")

    # analytical evaluation of the integral
    anval = intf(f, a, b)

    print(f"analytical solution: {anval}")

    ar10 = ar[0:int(0.1*len(ar))]
    ar20 = ar[0:int(0.2*len(ar))]
    ar30 = ar[0:int(0.3*len(ar))]
    ar40 = ar[0:int(0.4*len(ar))]
    ar50 = ar[0:int(0.5*len(ar))]
    ar60 = ar[0:int(0.6*len(ar))]
    ar70 = ar[0:int(0.7*len(ar))]
    ar80 = ar[0:int(0.8*len(ar))]
    ar90 = ar[0:int(0.9*len(ar))]
    percents = np.multiply(Npoints, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

    integral10 = 0.0
    integral20 = 0.0
    integral30 = 0.0
    integral40 = 0.0
    integral50 = 0.0
    integral60 = 0.0
    integral70 = 0.0
    integral80 = 0.0
    integral90 = 0.0

    for i in ar10:
        integral10 += f(i)

    for i in ar20:
        integral20 += f(i)

    for i in ar30:
        integral30 += f(i)

    for i in ar40:
        integral40 += f(i)

    for i in ar50:
        integral50 += f(i)

    for i in ar60:
        integral60 += f(i)

    for i in ar70:
        integral70 += f(i)

    for i in ar80:
        integral80 += f(i)

    for i in ar90:
        integral90 += f(i)

    tot_int = [integral10, integral20, integral30, integral40, integral50, integral60, integral70, integral80, integral90, integral]
    analy_sol = intf(f, a, b)
    
    area10 = (b-a)/float(Npoints*0.1)*tot_int[0]
    area20 = (b-a)/float(Npoints*0.2)*tot_int[1]
    area30 = (b-a)/float(Npoints*0.3)*tot_int[2]
    area40 = (b-a)/float(Npoints*0.4)*tot_int[3]
    area50 = (b-a)/float(Npoints*0.5)*tot_int[4]
    area60 = (b-a)/float(Npoints*0.6)*tot_int[5]
    area70 = (b-a)/float(Npoints*0.7)*tot_int[6]
    area80 = (b-a)/float(Npoints*0.8)*tot_int[7]
    area90 = (b-a)/float(Npoints*0.9)*tot_int[8]
    
    areas = [area10, area20, area30, area40, area50, area60, area70, area80, area90, ans]


    int_err = (areas-analy_sol)/analy_sol * 100

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

    plt.figure()
    plt.scatter(percents, int_err)
    plt.xlim([0, Npoints])
    plt.ylim([-100, 100])
    plt.xlabel("Number of Monte Carlo Points", fontsize = 15)
    plt.ylabel("% Error", fontsize = 15)
    plt.title("Monte Carlo method compared to Analytical Solution", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.show()



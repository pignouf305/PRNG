from PRNG import *
import matplotlib.pyplot as plt
import numpy as np
import inspect


def mc_area(f,a,b, minY=None, maxY=None, N = 10**4, plot=False, integExact=None):
    # Init
    if minY == None:
        minY = f(a)
    if maxY == None:
        maxY = f(b)
    xc, yc, xs, ys, integrals = [], [], [], [], []
    pointsInSquare = 0
    pointsBelow = 0
    squareArea = (maxY-minY) * (b-a)
    prng = prng_bbs()

    # Take N points in integral rectangular area and count above/below-curve points
    for i in range(N):
        x=randToInterval(prng(), a, b)
        y=randToInterval(prng(), minY, maxY)
        if y <= f(x):
            pointsBelow = pointsBelow+1
            xc.append(x); yc.append(y)
        else :
            xs.append(x); ys.append(y)
        pointsInSquare = pointsInSquare + 1    
        integral = squareArea * pointsBelow / pointsInSquare
        integrals.append(integral)

    if plot:
        # Get function description from source code
        try:
            lines = inspect.getsource(f)
            funcDesc = lines[lines.find("return ")+7:len(lines)]
        except Exception:
            funcDesc = "f(x)"

        # Plot curve
        fig = plt.figure()
        ax = fig.add_subplot()
        plt.plot(xc, yc,'.r')
        plt.plot(xs, ys,'.b')
        plt.title('Approximation of the integral of '+ funcDesc)
        plt.show()
        
        plt.plot(integrals, 'b--')
        if integExact:
            pi_exact = np.ones(len(integrals))*integExact;
            plt.plot(pi_exact, 'r-')    
        plt.title('Convergence')
        plt.grid(True)
        plt.show()


    return integral


if __name__ == '__main__':
    def foo(x) : return x**2

    integral = mc_area(foo, 0, 1, plot=True, N=10**4, integExact=1/3)
    print("Integral value of f : %.5f"% (integral))
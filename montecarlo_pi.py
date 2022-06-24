from PRNG import *
import matplotlib.pyplot as plt
import numpy as np

def main():
    prng = prng_bbs()

    xc, yc, xs, ys, pi = [], [], [], [], []
    N = int(1e4)
    pointsInSquare = 0
    pointsInCircle = 0
    for i in range(N):
        x=randToInterval(prng(), -1, 1)
        y=randToInterval(prng(), -1, 1)
        if x**2+y**2 < 1:
            pointsInCircle = pointsInCircle+1
            xc.append(x); yc.append(y)
        else :
            xs.append(x); ys.append(y)
        pointsInSquare = pointsInSquare + 1    
        pi.append(4*pointsInCircle/pointsInSquare)
        
    fig = plt.figure()
    ax = fig.add_subplot()
    plt.plot(xc, yc,'.r')
    plt.plot(xs, ys,'.b')
    plt.title('2D Random Distribution')
    ax.set_aspect('equal', adjustable='box')
    plt.show()

    pi_exact = np.pi*np.ones(len(pi));
    plt.plot(pi, 'b--')    
    plt.plot(pi_exact, 'r-')    
    plt.title('Pi convergence')
    plt.grid(True)
    plt.show()
    
    print(np.mean(pi[len(pi)//2:len(pi)]))

if __name__ == '__main__':
    main()
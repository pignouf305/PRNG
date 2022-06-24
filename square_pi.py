from PRNG import *
import matplotlib.pyplot as plt
import numpy as np

def main():
    #prng = prng_bbs()
    xc, yc, xs, ys, pi, n = [], [], [], [], [], []
    pointsInSquare = 0
    pointsInCircle = 0
    for N in range(10,1000,10):
        for i in range(N):
            x=randToInterval(i/N, -1, 1)
            for j in range(N):
                y=randToInterval(j/N, -1, 1)
                if x**2+y**2 < 1:
                    pointsInCircle = pointsInCircle+1
                    xc.append(x); yc.append(y)
                else :
                    xs.append(x); ys.append(y)
                pointsInSquare = pointsInSquare + 1    
        pi.append(4*pointsInCircle/pointsInSquare)
        n.append(N**2)

    pi_exact = np.pi*np.ones(len(pi));
    plt.plot(n,pi, 'b--')    
    plt.plot(n,pi_exact, 'r-')    
    plt.title('Pi convergence')
    plt.grid(True)

    print(np.mean(pi[len(pi)//2:len(pi)]))
        
    
    plt.show()

if __name__ == '__main__':
    main()
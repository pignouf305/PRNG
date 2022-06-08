from PRNG import *
import matplotlib.pyplot as plt
import time

#####  Algo choice & initialization  #####
# prng = prng_defaultPython()
# prng = prng_lcg()
prng = prng_bbs()

#####  Test with plots ##### 
## Histogram
a = [];
startTime = time.time()
for i in range(10000):
    a.append(prng());
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
plt.hist(a, bins=50);
plt.xlabel('Random outputs')
plt.ylabel('# of outputs')
plt.title('Random Distribution')
plt.show();

## 2D-Plot
x = [];y = [];
for i in range(10000):
    x.append(prng());
    y.append(prng());
    
plt.plot(x, y,'.')
plt.title('2D Random Distribution')
plt.show()
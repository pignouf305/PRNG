import time
import math
import random

### Toolbox
def seed_time():
    t = round(time.time_ns()/100)
    seed = int(t - math.floor(t/1e6)*1e6)
    return seed

def randToInterval(randFloat, mini, maxi):
    return mini + randFloat*(maxi-mini)

### Mersenne Twister Algorithm https://www.semanticscholar.org/paper/Mersenne-twister%3A-a-623-dimensionally-uniform-Matsumoto-Nishimura/098d5792ffa43e9885f9fc644ffdd7b6a59b0922
class prng_defaultPython(object):
    def __init__(self):
        self.x = 0
        
    def __call__(self):
        return random.random()
    
### Linear Congruential Generator Algorithm - https://en.wikipedia.org/wiki/Linear_congruential_generator
class prng_lcg(object):
    def __init__(self, x0 = seed_time(), M =  2**31-1, a = 16807, c = 0):
        self.a = a
        self.c = c
        self.x = x0
        self.M = M
        
    def __call__(self):
        self.x = ((self.x * self.a)+self.c) % self.M
        return (self.x)/(self.M)

### Blum Blum Shub Algorithm - https://fr.wikipedia.org/wiki/Blum_Blum_Shub
class prng_bbs(object):
    def __init__(self, x0 = seed_time(), M =  275604547*633910111):
        self.x = x0
        self.M = M
        
    def __call__(self):
        self.x = ((self.x)**2) % self.M
        return (self.x)/(self.M)


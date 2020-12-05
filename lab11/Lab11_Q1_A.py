"""taken from salesman.py in newman"""

from math import sqrt,exp
import numpy as np
from random import random,randrange, seed
import matplotlib.pyplot as plt

N = 25
R = 0.02
Tmax = 10.0
Tmin = 1e-3
tau = 1e4
seed(10)

# Function to calculate the magnitude of a vector
def mag(x):
    return sqrt(x[0]**2+x[1]**2)

# Function to calculate the total length of the tour
def distance():
    s = 0.0
    for i in range(N):
        s += mag(r[i+1]-r[i])
    return s

# Choose N city locations and calculate the initial distance
r = np.empty([N+1,2],float)
for i in range(N):
    r[i,0] = random()
    r[i,1] = random()
r[N] = r[0]
D = distance()

# Main loop
t = 0
T = Tmax
seed(2)
while T>Tmin:

    # Cooling
    t += 1
    T = Tmax*exp(-t/tau)

    # Choose two cities to swap and make sure they are distinct
    i, j = randrange(1,N),randrange(1,N)
    while i==j:
        i,j = randrange(1,N),randrange(1,N)
        
        # Swap them and calculate the change in distance
        oldD = D
        r[i,0],r[j,0] = r[j,0],r[i,0]
        r[i,1],r[j,1] = r[j,1],r[i,1]
        D = distance()
        deltaD = D - oldD
        
    
        # If the move is rejected, swap them back again
        if random()>exp(-deltaD/T):
            r[i,0],r[j,0] = r[j,0],r[i,0]
            r[i,1],r[j,1] = r[j,1],r[i,1]
            D = oldD
            
plt.scatter(r[:, 0], r[:, 1], c= "k", marker="s")
for i in range(N):
    plt.plot(r[i:i+2, 0], r[i:i+2, 1], "k-")
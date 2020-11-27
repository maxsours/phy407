"""
Modifying Brownian motion code given in the lab manual
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from random import randint

# the function to turn on interactive mode 
plt.ion()

# given values
Lp = 101  # size of domain
Nt = 5000  # number of time steps


# determining the centerpoints
centre_point = (Lp-1)//2  # middle point of domain
xp = centre_point
yp = centre_point

# arrays to record the trajectory of the particle
x = [xp]
y = [yp]

# function that generates random motion
def nextmove(x, y):
    """ randomly choose a direction
    0 = up, 1 = down, 2 = left, 3 = right"""
    direction = randint(0, 3) # generates random numbers to between 0 and 3
    
    if direction == 0:  # move up
        y += 1
    elif direction == 1:  # move down
        y -= 1
    elif direction == 2:  # move right
        x += 1
    elif direction == 3:  # move left
        x -= 1
    else:
        print("error: direction isn't 0-3")

    return x, y


font = {'family': 'DejaVu Sans', 'size': 14}  # adjust fonts
rc('font', **font)

# main loop for the motion of the particle
for i in range(Nt):
    xpp, ypp = nextmove(x[i], y[i])
    print (xpp, ypp)
    # if statments to check the walls
    if xpp == 0: # when the particle gets to 0 it moves in the opposite direction
        x[i] = x[i] + 1
    elif xpp == Lp: # when the particle hits the wall at Lp it t moves in the opposite direction
        x[i] = x[i] - 1
    elif ypp == 0: # when the particle gets to 0 it moves in the opposite direction
        y[i] = y[i] + 1
    elif ypp == Lp: # when the particle hits the wall at Lp it t moves in the opposite direction
        y[i] = y[i] - 1
    else: #if the praticles dont hit the wall the loop continues
        x.append(xpp)
        y.append(ypp)
    
print (x, y)
# plotting the brownian motion
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Brownian Motion')
plt.show()

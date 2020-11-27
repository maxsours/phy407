"""
This program simulates diffusion limited aggregation on an LxL grid.
Particles are initiated until the centre point is filled.
Author: Nico Grisouard, University of Toronto
Based on Paul J Kushner's DAL-eample.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from random import randint

def nextmove(x, y):
    """ randomly choose a direction
    1 = up, 2 = down, 3 = left, 4 = right"""
    direction = randint(0, 3) # generates random numbers to between 0 and 3
    
    if direction == 1:  # move up
        y += 1
    elif direction == 2:  # move down
        y -= 1
    elif direction == 3:  # move right
        x += 1
    elif direction == 4:  # move left
        x -= 1
    #else:
        #print("error: direction isn't 1-4")

    return x, y


font = {'family': 'DejaVu Sans', 'size': 14}  # adjust fonts
rc('font', **font)


plt.ion()

Lp = 101  # size of domain
N = 100  # number of particles
# array to represent whether each gridpoint has an anchored particle
anchored = np.zeros((Lp, Lp), dtype=int)
# list to represent x and y positions of anchored points
#anchored_points = [[], []]
anchoredx = []
anchoredy = []
#print (anchored)
centre_point = (Lp-1)//2  # middle point of domain

xp = centre_point
yp = centre_point
x = xp
y = yp
xpoints = []
ypoints = []
# set up animation of anchored points
plt.figure(1)
plt.title('DLA run for {} particles'.format(N))
plt.plot(centre_point, centre_point, '.y', markersize=10)
plt.xlim([-1, Lp])
plt.ylim([-1, Lp])
plt.xlabel('$x$ []')
plt.ylabel('$y$ []')

# set up animation of anchored points
animation_interval = 50  # how many moves to make before updating plot of
found_particle = False
found_edge = False

for i in range(N):
# while loop to check if the particle reached the edge
    while found_edge == False: 
        i = i+1
        # next step of the particle
        xpp, ypp = nextmove(x, y)
        x = xpp
        y = ypp
        xpoints.append(x) #stores the value of x in the list
        ypoints.append(y) #stores the value of y in the list
        if x == 0:
            found_edge = True
            anchoredx.append(x)
            anchoredy.append(y)
        elif x == Lp:
            found_edge = True
            anchoredx.append(x)
            anchoredy.append(y)
        elif y == 0:
            found_edge = True
            anchoredx.append(x)
            anchoredy.append(y)
        elif y == Lp:
            found_edge = True
            anchoredx.append(x)
            anchoredy.append(y)
            break #stops the process when the particle reaches the edge


# plotting DLA, path of the particles

plt.plot(xpoints, ypoints)
plt.show()
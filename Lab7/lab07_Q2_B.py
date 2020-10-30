# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:22:00 2020

Anntara Khan (1002321891)
Max Sours(1003816579)
"""

# LAB  7 Q2(B)
import numpy as np
import matplotlib.pyplot as plt

G = 6.6738e-11 * (2173440 * 60 * 60) ** 2 # [m3/kg], Gravitational constant, multiplying with 1 year(for pluto that is 90,560 Earth days) in seconds to get rid of the time unit
M = 1.9891e30 # [kg]
PH = 4.4368e12  # [m] perihelion of pluto
VP = 6.1218e3 * (2173440 * 60 * 60)  # [m] velocity of pluto at perihelion, multiplying with 1 year in seconds to get rid of the time unit
#r^2 = x^2+y^2


H = 1/12937      # Size of "big steps", one year in pluto has 12937 weeks
delta = 1000     # Required position accuracy per unit time

#using the function from newman excersise 8.12
def f(r):
    x = r[0]
    y = r[1]
    dx = r[2]
    dy = r[3]
    rad = np.sqrt((x**2 + y**2))
    f_x = ((-G * M * x) / rad**3) 
    f_y = ((-G * M * y) / rad**3) 
    return np.array([dx, dy, f_x, f_y])

##for the Bulirsch-Stoer method, we are modifying the code in example 8.7##


xpoints = []
ypoints = []

r = np.array([PH, 0.0, 0.0, VP],float)

# Do the "big steps" of size H
for t in range(13030): #since one year in pluto is not exactly 12937 weeks, adding an arbitrary number to approximate one full rotation around the sun

    xpoints.append(r[0])
    ypoints.append(r[1])

    # Do one modified midpoint step to get things started
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)

    # The array R1 stores the first row of the
    # extrapolation table, which contains only the single
    # modified midpoint estimate of the solution at the
    # end of the interval
    R1 = np.empty([1,4],float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))

    # Now increase n until the required accuracy is reached
    error = 2*H*delta
    while error>H*delta:

        n += 1
        h = H/n

        # Modified midpoint method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)

        # Calculate extrapolation estimates.  Arrays R1 and R2
        # hold the two most recent lines of the table
        R2 = R1
        R1 = np.empty([n,4],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
        for m in range(1,n):
            epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
            R1[m] = R1[m-1] + epsilon
        error = np.abs(epsilon[0])

    # Set r equal to the most accurate estimate we have,
    # before moving on to the next big step
    r = R1[n-1]


# Plot the results
plt.figure(figsize =(12, 9))
plt.title("Pluto's orbit arouond the Sun", fontsize = 25)
plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.plot(xpoints,ypoints, color = 'black', label = "Pluto's orbit")
plt.scatter([0], [0], color = 'yellow', label = "Sun", linewidth=(20))
plt.legend()
plt.tight_layout()
plt.show()
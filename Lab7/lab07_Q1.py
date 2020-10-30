# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:22:00 2020

Anntara Khan (1002321891)
Max Sours(1003816579)
"""
## LAB 7 Q1

import numpy as np
import matplotlib.pyplot as plt
from time import time 

# Constants
M = 10
G = 1
L = 2
x_0 = 1
y_0 = 0
v_x = 0
v_y = 1 
t_0 = 0
t_f = 10

N = 10000
h = (t_f - t_0) / N

#defining the function
def f(r):
    x = r[0]
    y = r[1]
    dx = r[2]
    dy = r[3]
    f_x = ((-G * M * x) / ((x**2 + y**2) * np.sqrt((x**2 + y**2) + (L**2 / 4)))) 
    f_y = ((-G * M * y) / ((x**2 + y**2) * np.sqrt((x**2 + y**2) + (L**2 / 4))))
    return np.array([dx, dy, f_x, f_y])


tpoints = np.arange(t_0, t_f, h)
# empty lists to store future x and y data for plotting
xpoints = []
ypoints = []

# the vector r that would contain the initial x and y position, and the initial x and y velocity
r = np.array([x_0, v_x, y_0, v_y], float)

##  RK4 with a fixed step size

start1 = time() # record time at the begining of the loop
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h * f(r)
    k2 = h * f(r + 0.5 * k1)
    k3 = h * f(r + 0.5 * k2)
    k4 = h * f(r + k3)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
end1 = time() # record time at the end of the loop

## Part A
## writitng a new rpogram for the adaptive step size, using a function to make it easier to call during each step iteration

# RK4 using adaptive step sizes

def ATS(r, t, h):
    def RK4(r, t, h):
        k1 = h * f(r)
        k2 = h * f(r + 0.5 * k1)
        k3 = h * f(r + 0.5 * k2)
        k4 = h * f(r + k3)
        return (k1 + 2 * k2 + 2 * k3 + k4) / 6

    s_1 = RK4(r, t, h)  # fist step, with h
    s_2 = RK4(r + s_1, t, h) # second step where we add the r from first step to the initital r value, to avoid recursion error 
    r1 = s_1 + s_2 # this gives us a new value from the first 2 steps

    r2 = RK4(r, t, 2 * h) # value of r for the double timestep, just to check the accuracy and not store the value

    # error estimates, x1,x2,y1,y2
    x1 = r1[0]
    x2 = r2[0]
    y1 = r1[1]
    y2 = r2[1]
    epsilon = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) / 30 # eucledean error, sqrt(ex^2+ey^2), eq 8.54 newman

    # Calculate rho, using #modiefied eq 8.53
    rho = h * delta / epsilon

    # Calculate factor to multiply h by
    r_fact = rho**(1/4)
    # multiply the h with the previously noted factor to get h', newman 8.53
    h_prime = h*r_fact
    # Update h accordingly
    # initial condition to check step sizes
    if  rho >= 1: # means that the step size is working
        # update t
        t = t + 2 * h
        # Prevent h from blowing up
        if r_fact > 6: # if the multiplication factor is greater than 4(or any arbitrary positive integer between 2 - 6 gives best results) we use double step 
            h *= 2 
        else: # otherwise we use h', which is supposed to be th perfect stepsize
            h = h_prime 
        return r1, h, t 
    else: # else statment for when we get poor accuracy,so we must repeat prev step with smaller h
        return ATS(r, t, h_prime) 


delta = 1e-6   # target accuracy 
h = (t_f - t_0) / 10000  # initial step size

# empty lists to store future t, x and, y data for plotting
tpoints2 = []
xpoints2 = []
ypoints2 = []

# initial conditions
r = np.array([x_0, v_x, y_0, v_y], float)  
t = t_0 

# while loop to run adaptive RK4 for the same amount of time as RK4
start2 = time() # record time at the begining of the loop
while(t < t_f):
    tpoints2.append(t)
    xpoints2.append(r[0])
    ypoints2.append(r[1])
    fin_r, h, t = ATS(r, t, h)
    r += fin_r
end2 = time() # record time at the end of the loop

# plotting all the data in one plot 
plt.figure(figsize = (9, 8))    
plt.title("Impact of adaptive step size", fontsize = 20)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xpoints, ypoints, label = 'RK4')
plt.plot(xpoints2, ypoints2, 'k.', label = 'ARK4')
plt.legend()
plt.show()

## Part B
# to measure the elapsed time for RK4, and ARK4
clocktime1 = end1-start1
clocktime2 = end2-start2

#prinitng out the values
print ("the time it takes to run RK4 is ", clocktime1, "seconds")
print ("the time it takes to run adaptive RK4 is ", clocktime2, "seconds")

## Part C
dtpoints = np.array(tpoints2[1:]) - np.array(tpoints2[:-1])

#plotting timestep as a function of time
plt.figure()
plt.title("Timestep as a function of Time")
plt.xlabel("Time (s)")
plt.ylabel("Time Step")
plt.plot(tpoints2[:-1], dtpoints)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:22:00 2020

Anntara Khan (1002321891)
Max Sours(1003816579)
"""

#LAB  5 Q1(B)

import numpy as np
import matplotlib.pyplot as plt

#constants
G = 1
M = 10
L = 2
#r^2 = x^2+y^2

'''following function takes 2 2nd orderd differential equation and 
returns 2 first order equation, i.e we get the distances and the 
velocitites in x and y direction from acceletarion in x and y direction'''

def f(r):
    x = r[0]
    y = r[1]
    dx = r[2]
    dy = r[3]
    f_x = ((-G * M * x) / ((x**2 + y**2) * np.sqrt((x**2 + y**2) + (L**2 / 4)))) 
    f_y = ((-G * M * y) / ((x**2 + y**2) * np.sqrt((x**2 + y**2) + (L**2 / 4))))
    return np.array([dx, dy, f_x, f_y])

#initital condition
t0 = 0.0
t1 = 10.0
N = 1000
h = (t1 - t0) / N

#setting an array for time to plot 
tpoints = np.arange(t0, t1, h)
#empty lists to store future x and y data for plotting
xpoints = []
ypoints = []

#the vector r that would contain the initial x and y position, and the initial x and y velocity
r = np.array([1.0, 0.0, 0.0, 1.0] , float)

#for loop to implement RK4
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h * f(r)
    k2 = h * f(r+ 0.5 * k1)
    k3 = h * f(r + 0.5 * k2)
    k4 = h * f(r + k3)
    r += (k1 + 2 * k2 + 2 * k3 + k4 ) / 6

#plottng the data
plt.figure()    
plt.plot(xpoints,ypoints)
plt.title("orbit of the ball bearing")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
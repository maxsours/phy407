# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:48:56 2020
Anntara Khan (1002321891)
Max Sours(1003816579)
"""
#LAB 2 Q2(B)

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
from math import pi, cos, sin

"""this code will take a function J_m(x) (bessel function) and integrate it 
using the simpson's rule with 1000 points to get the function J(m,x) 
the first 3 bessel functions are then plotted in a graph.
"""
#defining the finction J  that calculates the value of the bessel function 
def J(m,x):
   def J_m(r): #defining the Bessel function
       return cos((m * r) - (x * sin(r)))
   n = 1000 
   x_0 = 0.0
   x_f = pi
   h = (x_f - x_0) / n
   def simprule(lower, upper, func, slices): #defining the function for integration (taken from Q2.A)
       s1 = np.sum([J_m(x) for x in np.arange(x_0 + h, x_f, 2 * h)])
       s2 = np.sum([J_m(x) for x in np.arange(x_0 + 2 * h, x_f, 2 * h)])
       return h / 3 * (J_m(x_f) + J_m(x_0) + 4 * s1 + 2 * s2)
   return simprule(x_0, x_f, J_m, h)

x = np.linspace(0, 20, 1000) #1000 points between 0 to 20

J0 = [J(0, i) for i in x] #first bessel function calculated using J(m,x)
J1 = [J(1, i) for i in x] #second bessel function calculated using J(m,x)
J2 = [J(2, i) for i in x] #third bessel function calculated using J(m,x)

#Plots the first 3 bessel function
plt.plot(x, J0)
plt.plot(x, J1)
plt.plot(x, J2)
plt.title("Bessel Function")
plt.xlabel('values of x')
plt.ylabel('J(x)')
plt.legend(['J0', 'J1', 'J2'])
plt.savefig('Bessel Function.png')
plt.show()  

"""
this program will take the given intesity function I(r) and plot it over the distance 
from the focal plane, r , where r is between 0 and 1 micrometer. 
"""
#defining the intensity function
def I(r,k):
    '''I is undefined at r = 0, so we used the limit of J1(x)/x as r approaches 0, 
    which is equal to 1/2, so we replace j(kr)/r with half to obtain (k/2)^2
    we have tried if r is equal to zero retun (k/2)^2 but then the plot is 2 straing 
    so instead we will be using np.nan'''
    if (r < 10**-10 ): #when r is very very close to 0, numpy will ignore the value when plotting
        return np.nan
    else: #for all other vallues it will return the following
        return (J(1, k*r)/(k*r))**2
    
l = 500 * (10**-9)
k = (2*pi)/l
r = np.linspace(0, 10**-6, 1000) #1000 points between 0 to 10^-6

intensity = [I(a, k) for a in r] 

#plots the intensity over distance
plt.plot (r, intensity)
plt.title("intensity over distance")
plt.xlabel('distance in the focal plane')
plt.ylabel('intensity')
plt.savefig('intensity over distance.png')
plt.show()

#for the density plot
points = 500
separation = 20.0

# Make an array to store the heights
I_x = np.empty([points,points] ,float) 
for i in range(points):
    y = separation*i
    for j in range(points):
        x = separation*j 
        r = np.sqrt((x)**2+(y)**2) 
        if r < 10**-10:
            I_x[i,j] = (0.5/k)**2
        else:
            I_x[i,j] = (J(1, k*r)/(k*r))**2

plt.imshow(I_x,vmax = 0.01, cmap = 'hot')
plt.show()

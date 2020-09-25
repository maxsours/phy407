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

def J(m,x):
    
   def J_m(r):
       return cos((m * r) - (x * sin(r)))
   n = 1000 
   x_0 = 0.0
   x_f = pi
   h = (x_f - x_0) / n
   def simprule(lower, upper, func, slices):
       s1 = np.sum([J_m(x) for x in np.arange(x_0 + h, x_f, 2 * h)])
       s2 = np.sum([J_m(x) for x in np.arange(x_0 + 2 * h, x_f, 2 * h)])
       return h / 3 * (J_m(x_f) + J_m(x_0) + 4 * s1 + 2 * s2)
   return simprule(x_0, x_f, J_m, h)

x = np.linspace(0, 20, 1000)

J0 = [J(0, i) for i in x]
J1 = [J(1, i) for i in x]
J2 = [J(2, i) for i in x]

plt.plot(x,J0)
plt.plot(x,J1)
plt.plot(x,J2)
plt.title("Bessel Function")
plt.xlabel('values of x')
plt.ylabel('J(x)')
plt.legend(['J0', 'J1', 'J2'])
plt.savefig('Bessel Function.png')
plt.show()  



def I(r,k):
    if (r <= 10**-8):
        return (1/2*k)**2

    return (J(1, k*r)/(k*r))**2
    
l = 500 * (10**-9)
k = (2*pi)/l
r = np.linspace(0, 10**-6, 1000)

intensity = [I(a, k) for a in r]
    
plt.plot (r, intensity)
plt.title("intensity over distance")
plt.xlabel('distance in the focal plane')
plt.ylabel('intensity')
plt.savefig('intensity over distance.png')
plt.show()



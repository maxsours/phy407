# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:48:56 2020

@author: stone
"""

#LAB 2 Q2(B)

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sp
from math import pi, cos, sin


def simprule(lower, upper, func, slices):
    """
    Integrate func from lower to upper using Simpson's rule with the
    inputed slices.
    Parameters
    ----------
    lower : float
        Lower limit of integration.
    upper : float
        Upper limit of integration.
    func : float -> float
        1-D function to be integrated.
    slices: int
        Number of slices with trapezoid rule.
    Returns
    -------
    float :
    Value of the integral using Simpson's rule.
    """
    h = (upper - lower) / slices
    s1 = np.sum([func(x) for x in np.arange(lower + h, upper, 2 * h)])
    s2 = np.sum([func(x) for x in np.arange(lower + 2 * h, upper, 2 * h)])
    return h / 3 * (func(upper) + func(lower) + 4 * s1 + 2 * s2)

n= 1000
x = 20
def J(m,x):
   def J_m(m,x,r):
       return cos((m * r) - (x * sin(r)))


    x_0 = 0.0
    x_f = pi
    h = (x_f-x_0)/n
    #simp_in = J_m(m, x, x_0) + J_m(m, x, x_f)
    for i in range (1, n):
        for j in range (0, x):
            for k in range (0, pi):
                return simprule(x_0, x_f, J_m(i,j,k), h)
   

x = np.linspace(0, 20, 1000)
for i in x:
    J0 = J(0, i)
    J1 = J(1, i)
    J2 = J(2, i)
# plot the points

plt.plot(x,J0)
plt.plot(x,J1)
plt.plot(x,J2)
plt.xlabel('x')
plt.legend(['J0', 'J1', 'J2'])
plt.show()
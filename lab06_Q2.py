# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:22:00 2020

Anntara Khan (1002321891)
Max Sours(1003816579)
"""

#LAB  5 Q2(A)

import numpy as np
import matplotlib.pyplot as plt


#constants
D = 2.0 #dimention
N = 2.0 #number of particles
E = 1.0 #epsilon
S = 1.0 #sigma
m = 1.0 #mass

#part a, defines accleration in x and y direction
def V(r):
    x = r[0]
    y = r[1]
    a_x = (4*E*((S/x)**12-(S/x)**6))
    a_y = (4*E*((S/x)**12-(S/y)**6))
    return ([a_x,a_y])

radius = np.zeroes([2, 100])

#part b
#verlet method

dt = 0.01 #timestep



    

















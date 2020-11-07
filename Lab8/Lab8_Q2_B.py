# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:27:06 2020

Anntara Khan (1002321891)
Max Sours(1003816579)
"""
## LAB 8 Q2

import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1 # [m]
J = 50
dx = 0.02 # [m]
x = np.arange(0, L, dx)
A = 0.002 # [m]
mu = 0.5 # [m]
sigma = 0.05 # [m]
h = 0.01 # [s], timestep
g = 9.81 # [m/s^2]
L = 1 # [m]
H = 0.01 # [m]
eta_b = 0

# initital conditions
fact1 = -(x-mu)**2
fact2 = sigma**2
fact3 = fact1/fact2
A_exp = A*np.exp(fact3)
eta_0 = H + A_exp - np.mean(A_exp)
u_0, u_f = 0, 0

# Intitiallize arrays
u = np.zeros(J)
eta1 = np.zeros(J) 
eta = np.zeros(J) 

# define the function eq 7 (lab manual)
def F(u,eta):
    return ((0.5 * u ** 2) + g * h) , ((eta - eta_b) * u)
t1 = 0 # [s]
t2 = 1 # [s]
t3 = 4 # [s]
t = 0
tend = 5 #not sure
tplot = np.array([0,1,4])
while t < tend:
    

    ## boundary conditions for eta with forward/backwards difference
    eta1[0]  = eta1[0] - (h / dx) * (F[1][1] - F[1][0])
    eta1[J]  = eta1[J] - (h / dx) * (F[1][J] - F[1][J-1])
    
    for j in range(0,J):
        u_new[j] = u[j] + ... # (all in terms of u and eta)
        eta_new[j] = eta[j] + ... # (all in terms of u and eta)
        unew[j]  = unew[j] - (h / (2 * dx)) * (F[0][j+1] - F[0][j-1])
        etanew[j]  = etanew[j] - (h / (2 * dx)) * (F[1][j+1] - F[1][j-1])
        eta = np.copy(etanew)
        u = np.copy(unew)
    if np.any(np.abs(t-tplot)) < 1e-6:
        plt.clf()
        plt.title("shallow water waves")
        plt.xlabel("x")
        Plt.ylabel("eta")
        plt.plot(x, eta)
        plt.draw()
        plt.pause(0.01)
        
    t = t + h
        
        
    
    
    


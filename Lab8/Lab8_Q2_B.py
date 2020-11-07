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
dt = 0.01 # [s], timestep
g = 9.81 # [m/s^2]
H = 0.01 # [m]
eta_b = 0
N = len(x)

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
def F(v):
    return np.array([(0.5 * v[0] ** 2) + g * v[1] , (v[1] - eta_b) * v[0]])

def next_v(v_curr, dt, dx):
    """
    Given current v = (u, eta) for all points and timestep dt, spacial step dx,
    return the next v.

    Parameters
    ----------
    v_curr : 2xL float array
        Current v = (u, eta)
    dt : float
        timestep
    dx : float
        spacial step

    Returns
    -------
    v_next : 2xL float array
        Next values for v = (u, eta)
    """
    v_next = np.zeros(v_curr.shape)
    v_next[1, 0] = v_curr[1, 0] - dt / dx * (F(V_curr[:, 1]) - F(V_curr[:, 0]))[1]
    v_next[1, N - 1] = v_curr[1, N - 1] - dt / dx * (F(V_curr[:, N - 1]) - F(V_curr[:, N - 2]))[1]
    for i in range(1, N-1):
        v_next[:, i] = v_curr[:, i] - dt / (2 * dx) * (F(V_curr[:, i + 1]) - F(V_curr[:, i - 1]))
    return v_next


t1 = 0 # [s]
t2 = 1 # [s]
t3 = 4 # [s]
t = 0
tend = 4 #not sure
tplot = np.array([0,1,4])
while t < tend:
    for j in range (1, J-1):
        fact4 = h / (2 * dx)
        fact5 = h/ dx
        
        #boundary condititons
        if n == 0:

    ## boundary conditions for eta with forward/backwards difference
    eta1[0]  = eta1[0] - (h / dx) * (F[1][1] - F[1][0])
    eta1[J]  = eta1[J] - (h / dx) * (F[1][J] - F[1][J-1])
    
    for j in range(0,J):
        u_new[j] = u[j] + ... # (all in terms of u and eta)
        eta_new[j] = eta[j] + ... # (all in terms of u and eta)
        u_new[j]  = u_new[j] - (h / (2 * dx)) * (F[0][j+1] - F[0][j-1])
        eta_new[j]  = eta_new[j] - (h / (2 * dx)) * (F[1][j+1] - F[1][j-1])
        eta = np.copy(etanew)
        u = np.copy(unew)
    if np.any(np.abs(t-tplot)) < 1e-6:
        plt.clf()
        plt.title("shallow water waves")
        plt.xlabel("x")
        plt.ylabel("eta")
        plt.plot(x, eta)
        plt.draw()
        plt.pause(0.01)
        
    t = t + dt
        
        
    
    
    


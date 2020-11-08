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
v_0 = np.empty((2, N))
v_0[0, :] = np.zeros(N) #u_0
v_0[1, :] = eta_0

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
    v_next[1, 0] = v_curr[1, 0] - dt / dx * (F(v_curr[:, 1]) - F(v_curr[:, 0]))[1]
    v_next[1, N - 1] = v_curr[1, N - 1] - dt / dx * (F(v_curr[:, N - 1]) - F(v_curr[:, N - 2]))[1]
    for i in range(1, N-1):
        v_next[:, i] = v_curr[:, i] - dt / (2 * dx) * (F(v_curr[:, i + 1]) - F(v_curr[:, i - 1]))
    return v_next


t = 0
tend = 4
tplot = np.array([0,1,4])
v = v_0
while t <= tend:
    if np.any(np.abs(t-tplot) < 1e-6):
        plt.clf()
        plt.title("shallow water waves")
        plt.xlabel("x (m)")
        plt.ylabel("eta (m/s)")
        plt.plot(x, v[1, :])
        plt.draw()
        plt.pause(0.01)
    v = next_v(v, dt, dx)
    t = t + dt
        
        
    
    
    


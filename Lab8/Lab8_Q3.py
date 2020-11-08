# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:27:06 2020

Anntara Khan (1002321891)
Max Sours(1003816579)
"""
## LAB 8 Q3

import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1 # [m]
N = 151
x = np.linspace(0, L, N)
dx = L / (N - 1)
A = 2e-4 # [m]
mu = 0.5 # [m]
sigma = 0.1 # [m]
dt = 0.001 # [s], timestep
g = 9.81 # [m/s^2]
H = 0.01 # [m]
eta_bs = H - 4e-4 # [m]
alpha = 8 * np.pi # [m^-1]
x0 = 0.5 # [m]

# initital conditions
A_exp = A*np.exp(-(x / sigma) ** 2)
eta_0 = H + A_exp - np.mean(A_exp)
v_0 = np.empty((2, N))
v_0[0, :] = np.zeros(N) #u_0
v_0[1, :] = eta_0
eta_b = eta_bs / 2 * (1 + np.tanh((x - x0) * alpha))

# define the function eq 7 (lab manual)
def F(v, i):
    """ Calculate flux from given array v = (u, eta), and i = index of v array
    """
    return np.array([(0.5 * v[0, i] ** 2) + g * v[1, i] , (v[1, i] - eta_b[i]) * v[0, i]])

def next_v(v, dt, dx):
    """
    Given current v = (u, eta) for all points and timestep dt, spacial step dx,
    return the next v.

    Parameters
    ----------
    v : 2xN float array
        Current v = (u, eta)
    dt : float
        timestep
    dx : float
        spacial step

    Returns
    -------
    v_next : 2xN float array
        Next values for v = (u, eta)
    """
    v_next = v + 0 # Add 0 so python doesn't copy by reference
    v_half = np.empty((2, N - 1))
    for i in range(N - 1):
        v_half[:, i] = (v[:, i + 1] + v[:, i]) / 2 - dt / (2 * dx) * (F(v, i + 1) - F(v, i))
    # Endpoints require forward and backward different formulas, respecitively
    # Note that only eta is calculated, since u = 0 on the ends
    v_next[1, 0] -= dt / dx * F(v_half, 0)[1]
    v_next[1, N - 1] += dt / dx * F(v_half, N - 2)[1]
    for i in range(1, N-1):
        v_next[:, i] -= dt / dx * (F(v_half, i) - F(v_half, i - 1))
    return v_next


t = 0
tend = 5
tplot = np.array([0,1, 2, 3, 4, 5])
v = v_0
while t <= tend:
    if np.any(np.abs(t-tplot) < 1e-6):
        plt.clf()
        plt.title("shallow water waves at t = " + str(round(t)))
        plt.xlabel("x (m)")
        plt.ylabel("eta (m)")
        plt.plot(x, v[1, :])
        #plt.plot(x, eta_b, "k-")
        plt.draw()
        plt.pause(0.01)
    v = next_v(v, dt, dx)
    t = t + dt
        
        
    
    
    


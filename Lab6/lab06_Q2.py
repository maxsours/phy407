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
D = 2.0 #dimension
N = 2.0 #number of particles
E = 1.0 #epsilon
S = 1.0 #sigma
m = 1.0 #mass

#part a, defines accleration in x and y direction
def LJ_accel(r):
    """
    Return acceleration of a particle affected by another
    particle in Leonard Jones potential.

    Parameters
    ----------
    r : 2x1 array of floats
        Real valued 2-D column vector representing distance
        to the other particle.

    Returns
    -------
    2x1 array of floats
        Acceleration vector of the particle.

    """
    R = np.linalg.norm(r)
    result = 24*E * (2*(S/R)**12 - (S/R)**6) * r # dV/dr
    return result # I'm returning a vector because vectorized operations are more efficient

#part b
#verlet method

"""
PSEUDOCODE

function (a, p1x_0, p2x_0, dt, n):
    Let a be a function that takes a position vector and outputs an acceleration vector
    Let each x_0 be an initial position for each particle.
    Let dt be a float representing timestep increment
    Let n be an integer representing number of iterations
    p1v_{0.5} = 0.5 * dt * a(p1x_0 - p2x_0)
    p2v_{0.5} = 0.5 * dt * a(p2x_0 - p1x_0)
    for i = 1 ... n:
        p1x_i = p1x_{i-1} + p1v_{i - 0.5} * dt # Verlet step 1
        p2x_i = p2x_{i-1} + p2v_{i - 0.5} * dt
        
        p1k = a(p1x_i - p2x_i) * dt # Verlet step 2
        p2k = a(p2x_i - p1x_i) * dt
        
        p1v_i = p1v_{i-0.5} + p1k / 2 # You don't actually need this step (for now, anyway), but it is part of the Verlet method, so I felt obligated to include it here
        p2v_i = p2v_{i-0.5} + p2k / 2
        
        p1v_{i+0.5} = p1v_{i-0.5} + p1k # Verlet step 3
        p2v_{i+0.5} = p2v_{i-0.5} + p2k
    
    plot [p1x_0, ..., p1x_n], [p2x_0, ..., p2x_n]
"""

def A(a, x):
    """
    This is a helper function that computes the acceleration
    of n particles for each particle
    """
    _, n = x.shape
    result = np.empty(x.shape)
    for i in range(n):
        result[:, i] = np.sum([a(x[:, i] - x[:, j]) for j in range(n) if i != j], axis=0)
    return result

def plot_particles(a, x0, dt, m):
    """
    Plot n particles from initial positions given by x0 under
    acceleration function a over m iterations.

    Parameters
    ----------
    a : 2x1 float array -> 2x1 float array
        Vector valued function that takes position and outputs
        acceleration
    x0 : 2xn float array
        Initial positions for the n particles
    dt : float
        Timestep
    m : int
        Number of iterations

    Returns
    -------
    2xnxm array of floats
        Positions of n particles over time
    2xnxm array of floats
        Velocities of n particles over time
    """
    _, n = x0.shape
    x = np.empty((2, n, m))
    v = np.zeros((2, n, m))
    x[:, :, 0] = x0; # initial verlet step
    v_temp = A(a, x[:, :, 0]) * 0.5 * dt
    for i in range(1, m): #do verlet steps
        x[:, :, i] = x[:, :, i - 1] + v_temp * dt
        k = A(a, x[:, :, i]) * dt
        v[:, :, i] = v_temp + k / 2
        v_temp = v_temp + k
    return x, v

if __name__ == "__main__":
    n = 2
    x0 = np.array([[2, 3], [3.5, 4.4]]).transpose()
    x, v = plot_particles(LJ_accel, x0, 0.01, 100)
    for i in range(n):
        plt.plot(x[0, i, :], x[1, i, :], ".")



dt = 0.01 #timestep



    

















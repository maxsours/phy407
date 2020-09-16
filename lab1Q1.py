# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:21:56 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt

# Part 1

def apply_vector_to_scalar(mat, func):
    """
    Apply a function to each individual column of a matrix.
    This is a helper function that makes my life easier.
    
    Parameters
    ----------
    mat : n x m array of type t
        arbitrary matrix
    func : function: n x 1 array of type t -> t
        arbitrary function with the aboe type signature

    Returns
    -------
    1 x m array of type t

    """
    m = mat.shape[1]
    result = np.zeros(m)
    for i in range(m):
        result[i] = func(mat[:, i])
    return result

"""
FUNCTION mercury_orbit(x_0, v_0, delta_t, n):
    INPUTS x_0, v_0: 2x1 array of floats
    INPUTS delta_t, n: float
    LET mu <- standard gravitational parameter of the sun (G * M_sun)
    LET x, v be empty 2xn arrays
    LET t be an empty 1xn array
    ASSIGN t[0] <- 0
    ASSIGN i <- 0
    ASSIGN x[:,0] <- x_0, v[:,0] <- v_0
    WHILE i < n:
        COMPUTE a = -mu * x[:,i] / r^3, where r = magnitude(x[:,i])
        ASSIGN v[:,i+1] <- v[:,i] + a * delta_t
        ASSIGN x[:,i+1] <- x[:,i] + v[:,i+1] * delta_t
        ASSIGN t[i+1] <- t[i] + delta_t
        INCREMENT i
    PLOT v[0,:] vs. t, v[1,:] vs. t, x[1, :] vs x[0, :]
"""
def solar_orbit(x_0, v_0, delta_t, n):
    """
    Return plotting data for orbit of an object going around
    the sun.
    
    Parameters
    ----------
    x_0 : 2x1 float array
        Initial position of object in AU
    v_0 : 2x1 float array
        Initial velocity of object in AU
    delta_t : float
        Increment of time between each iteration in years
    n : int
        Number of iterations
    Returns
    -------
    x: 2xn float array
        n 2x1 position vectors of the object
    v: 2xn float array
        n 2x1 velocity vectors of the object
    t: 1xn float array
        time vector for use as independent variable
    """
    x = np.zeros((2, n))
    v = np.zeros((2, n))
    t = np.zeros(n)
    mu =  39.5 #AU^3 yr^{-2} (mu = GM)
    x[:, 0] = x_0
    v[:, 0] = v_0
    t[0] = 0
    for i in range(n-1):
        r = np.linalg.norm(x[:, i])
        a = -mu * x[:, i] * r ** (-3)
        v[:, i + 1] = v[:, i] + a * delta_t
        x[:, i + 1] = x[:, i] + v[:, i + 1] * delta_t
        t[i + 1] = t[i] + delta_t
    return x, v, t

def solar_orbit_first_correction(x_0, v_0, delta_t, n, alpha):
    """
    Plot orbit of an object going around the sun.
    
    Parameters
    ----------
    x_0 : 2x1 float array
        Initial position of object in AU
    v_0 : 2x1 float array
        Initial velocity of object in AU
    delta_t : float
        Increment of time between each iteration in years
    n : int
        Number of iterations
    alpha : float
        Parameter for reletavistic correction
    Returns
    -------
    x: 2xn float array
        n 2x1 position vectors of the object
    v: 2xn float array
        n 2x1 velocity vectors of the object
    t: 1xn float array
        time vector for use as independent variable
    """
    x = np.zeros((2, n))
    v = np.zeros((2, n))
    t = np.zeros(n)
    mu =  39.5 #AU^3 yr^{-2} (mu = GM)
    x[:, 0] = x_0
    v[:, 0] = v_0
    t[0] = 0
    for i in range(n-1):
        r = np.linalg.norm(x[:, i])
        a = -mu * (1 + alpha / (r ** 2)) * x[:, i] * r ** (-3)
        v[:, i + 1] = v[:, i] + a * delta_t
        x[:, i + 1] = x[:, i] + v[:, i + 1] * delta_t
        t[i + 1] = t[i] + delta_t
    return x, v, t

x, v, t = solar_orbit(np.array([0.47, 0]), np.array([0, 8.17]), 0.0001, 10000)
plt.figure(1)
plt.title("Vx vs. Time")
plt.xlabel("Time (yr)")
plt.ylabel("Velocity (AU/yr)")
plt.plot(t, v[0, :])
plt.figure(2)
plt.title("Vy vs. Time")
plt.xlabel("Time (yr)")
plt.ylabel("Velocity (AU/yr)")
plt.plot(t, v[1, :])
plt.figure(3)
plt.axis("equal")
plt.title("Orbit of Mercury plotted over a year")
plt.xlabel("x position (AU)")
plt.ylabel("y position (AU)")
plt.plot(x[0, :], x[1, :])
plt.figure(4)
plt.title("Angular Momentum over time")
plt.xlabel("Time (yr)")
plt.ylabel("Angular momentum (AU^2 yr^{-1} * Mercury Mass)")
plt.plot(t, apply_vector_to_scalar(x, np.linalg.norm) * apply_vector_to_scalar(v, np.linalg.norm))
x_c, v_c, t_c = solar_orbit_first_correction(np.array([0.47, 0]), np.array([0, 8.17]), 0.0001, 10000, 0.01)
plt.figure(5)
plt.axis("equal")
plt.title("Orbit of Mercury with 1st reletavistic correction")
plt.xlabel("x position (AU)")
plt.ylabel("y position (AU)")
plt.plot(x_c[0, :], x_c[1, :])
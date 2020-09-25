# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:34:50 2020

@author: Anntara Khan(1002321891), Max Sours(1003816579)
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scii
from lab2Q2a import simprule, traprule

def q(u):
    """
    Implements q(u) as described in 3b.

    Parameters
    ----------
    u : float
        Real valued parameter.

    Returns
    -------
    float -> value of q(u)

    """
    alpha = np.pi / 20e-6 # alpha in m^{-1}
    return (np.sin(alpha * u)) ** 2

def q2(u):
    """
    Implements q(u) as described in 3e i.
    """
    alpha = np.pi / 20e-6 #alpha in m^{-1}
    beta = 0.5 * alpha
    return (np.sin(alpha * u) * np.sin(beta * u)) ** 2

def q3(u):
    """
    Implements q(u) as described in 3e ii.
    
    One of the gaps is (-40, -30) the other is at (30, 50)
    """
    return 1 if (np.abs(u + 35e-6) < 5e-6 or np.abs(u - 40e-6) < 10e-6) else 0

"""
FUNC DIFFRACTION():
    lambda = 500 nm
    f = 1 m
    w = 10 * 20 microns
    x = [-5 cm, 5 cm]
    func = sqrt(q(u)) * exp(2*pi*i*x*u/(lambda * f))
    y = |Simpson's Rule(-w/2, w/2, func, 1000)|^2
    plot (x, y)
"""

def diffraction(q, lambda_, f, w, n):
    """
    Return plotting data of the intensity function 

    Parameters
    ----------
    q : float -> float
        q function used to evaluate the intensity function.

    Returns
    -------
    1-D array of floats:
        x-coordinates of plot
    1-D array of floats:
        y-coordinates of plot

    """
    x = np.linspace(-5e-2, 5e-2, n)
    y = np.zeros(n)
    for i in range(n):
        func = lambda u: np.sqrt(q(u)) * np.exp(2j * np.pi * x[i] * u / (lambda_ * f))
        y[i] = np.abs(simprule(-w/2, w/2, func, 1000)) ** 2
        #I, _ = scii.quad(func, -w/2, w/2)
        #y[i] = np.abs(I) ** 2
    return x, y

if __name__ == "__main__":
    lambda_ = 500e-9
    f = 1
    w = 10 * 20e-6
    n = 200
    x, y = diffraction(q, lambda_, f, w, n)
    plt.figure(1)
    plt.plot(x, y)
    plt.ylabel("Intensity")
    plt.xlabel("X position (m)")
    plt.title("Intensity Plot")
    plt.show()
    plt.figure(2)
    n = len(y)
    image_array = np.zeros((n // 10, n))
    for i in range(n // 10):
        image_array[i, :] = y
    plt.title("Density Plot of Intensity Function")
    plt.xlabel("Position (cm)")
    plt.imshow(image_array)
    plt.colorbar()
    plt.xticks(np.arange(0, n+1, n // 10), np.arange(-5, 6))
    
    x, y = diffraction(q2, lambda_, f, w, n)
    plt.figure(3)
    plt.plot(x, y)
    plt.ylabel("Intensity")
    plt.xlabel("X position (m)")
    plt.title("Intensity Plot for 3e i")
    plt.show()
    plt.figure(4)
    n = len(y)
    image_array = np.zeros((n // 10, n))
    for i in range(n // 10):
        image_array[i, :] = y
    plt.title("Density Plot of Intensity for 3e i")
    plt.xlabel("Position (cm)")
    plt.imshow(image_array)
    plt.colorbar()
    plt.xticks(np.arange(0, n+1, n // 10), np.arange(-5, 6))
    
    x, y = diffraction(q3, lambda_, f, w, n)
    plt.figure(3)
    plt.plot(x, y)
    plt.ylabel("Intensity")
    plt.xlabel("X position (m)")
    plt.title("Intensity Plot for 3e ii")
    plt.show()
    plt.figure(4)
    n = len(y)
    image_array = np.zeros((n // 10, n))
    for i in range(n // 10):
        image_array[i, :] = y
    plt.title("Density Plot of Intensity for 3e ii")
    plt.xlabel("Position (cm)")
    plt.imshow(image_array)
    plt.colorbar()
    plt.xticks(np.arange(0, n+1, n // 10), np.arange(-5, 6))
    
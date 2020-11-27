# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:49:13 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt

def mean_value(f, a, b, N):
    """
    Compute integral of f from a to b with N sampled points
    using mean value Monte Carlo method.

    Parameters
    ----------
    f : (float -> float)
        1D function with a domain of [a, b]
    a : float
        Lower limit of integration
    b : float
        Upper limit of integration
    N : int
        Number of points to sample

    Returns
    -------
    float:
        Calculated integral of f from a to b

    """
    samples = (b - a) * np.random.rand(N) + a
    return (b - a) * np.mean(f(samples))
    

def importance_sampling(f, a, b, N):
    """
    Compute integral of f from a to b with N sampled points
    using importance sampling with p(x) = 0.5x^{-0.5}

    Parameters
    ----------
    f : (float -> float)
        1D function with a domain of [a, b]
    a : float
        Lower limit of integration
    b : float
        Upper limit of integration
    N : int
        Number of points to sample

    Returns
    -------
    float:
        Computed integral

    """
    F = lambda x: 2 / (1 + np.exp(x)) # F = f / p
    # \int_0^x p(x')dx' = sqrt(x) = z --> x = z^2
    samples = np.random.rand(N) ** 2
    return np.mean(F(samples))

def repeat_method(method, f, a, b, N, R):
    """
    Repeat R times Monte Carlo integration method with
    function f with limits [a, b] and number of samples N.

    Parameters
    ----------
    method : (f, a, b, N) - > float
        method of Monte Carlo integration
    f : (float -> float)
        1D function with a domain of [a, b]
    a : float
        Lower limit of integration
    b : float
        Upper limit of integration
    N : int
        Number of points to sample
    R : int
        Number of times to repeat method

    Returns
    -------
    1 x R array of floats:
        Array of results of R integrations

    """
    result = np.zeros(R)
    for i in range(R):
        result[i] = method(f, a, b, N)
    return result
    

if __name__ == "__main__":
    f = lambda x: x ** (-0.5) / (1 + np.exp(x))
    
    I = repeat_method(mean_value, f, 0, 1, 10000, 100)
    plt.hist(I, 10, [0.8, 0.88])
    plt.xlabel("Integral Value")
    plt.title("Histogram of Computed Integrals by Mean Value")
    plt.show()
    
    I = repeat_method(importance_sampling, f, 0, 1, 10000, 100)
    plt.hist(I, 10, [0.8, 0.88])
    plt.xlabel("Integral Value")
    plt.title("Histogram of Computed Integrals by Importance Sampling")
    plt.show()
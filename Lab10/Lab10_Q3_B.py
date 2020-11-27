# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:49:13 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt
from Lab10_Q3_A import mean_value, repeat_method

def importance_sampling(f, a, b, N):
    """
    Compute integral of f from a to b with N sampled points
    using importance sampling with a p(x) = Gaussian(mu = 5, sigma = 1)

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
    w = lambda x: 1 / np.sqrt(2 * np.pi) * np.exp(-(x - 5) ** 2 / 2)
    #Don't need to multiply integral of w here since it is essentially 1 (Random Monte Carlo error is much bigger)
    F = lambda x: f(x) / w(x)
    samples = np.random.normal(5, 1, N)
    return np.mean(F(samples))
    

if __name__ == "__main__":
    f = lambda x: np.exp(-2 * np.abs(x - 5))
    
    I = repeat_method(mean_value, f, 0, 10, 10000, 100)
    plt.hist(I, 10, [0.94, 1.08])
    plt.xlabel("Integral Value")
    plt.title("Histogram of Computed Integrals by Mean Value")
    plt.show()
    
    I = repeat_method(importance_sampling, f, 0, 10, 10000, 100)
    plt.hist(I, 10, [0.94, 1.08])
    plt.xlabel("Integral Value")
    plt.title("Histogram of Computed Integrals by Importance Sampling")
    plt.show()
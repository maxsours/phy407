# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 14:56:14 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    Return True iff x is inside the nth dimensional hypersphere,

    Parameters
    ----------
    x : n x N array of floats
        Point inside the nth dimensional hypercube of sidelength
        1 centered on the origin.

    Returns
    -------
    Whether the point is inside the hypersphere or not

    """
    return np.linalg.norm(x, axis=0) <= 1

def nd_sphere(n, N):
    """
    Calculate the volume of an n-dimensional sphere using
    Monte Carlo mean value method

    Parameters
    ----------
    n : int
        number of dimensions
    N : int
        number of sampled points

    Returns
    -------
    I : float
        Volume of hypersphere.
    E : float
        Approximate error of calculation

    """
    V = 1 << n # 2^n
    samples = 2 * np.random.rand(n, N) - 1
    fs = f(samples)
    I = V * np.mean(fs)
    E = V * np.sqrt(np.mean(fs ** 2) - np.mean(fs) ** 2) / np.sqrt(N)
    return I, E

if __name__ == "__main__":
    n = 10
    N = 1000000
    print(nd_sphere(n, N))
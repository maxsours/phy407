# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:00:37 2020

@author: Anntara Khan(1002321891), Max Sours(1003816579)
"""
import numpy as np
import scipy.special as scis
from time import time

def traprule(lower, upper, func, slices):
    """
    Integrate func from lower to upper using trapezoid rule with the
    inputed slices.

    Parameters
    ----------
    lower : float
        Lower limit of integration.
    upper : float
        Upper limit of integration.
    func : float -> float
        1-D function to be integrated.
    slices: int
        Number of slices with trapezoid rule.

    Returns
    -------
    float :
    Value of the integral using the trapezoid rule.
    """
    h = (upper - lower) / slices
    s = np.sum([func(x) for x in np.arange(lower + h, upper, h)])
    return h * ((func(upper) + func(lower)) / 2 + s)

def simprule(lower, upper, func, slices):
    """
    Integrate func from lower to upper using Simpson's rule with the
    inputed slices.

    Parameters
    ----------
    lower : float
        Lower limit of integration.
    upper : float
        Upper limit of integration.
    func : float -> float
        1-D function to be integrated.
    slices: int
        Number of slices with trapezoid rule.

    Returns
    -------
    float :
    Value of the integral using Simpson's rule.
    """
    h = (upper - lower) / slices
    s1 = np.sum([func(x) for x in np.arange(lower + h, upper, 2 * h)])
    s2 = np.sum([func(x) for x in np.arange(lower + 2 * h, upper, 2 * h)])
    return h / 3 * (func(upper) + func(lower) + 4 * s1 + 2 * s2)

def time_code(func, n):
    """
    Time now long it takes code to run by running it n times 
    and taking the average.

    Parameters
    ----------
    func : thunk
        An argumentless function containing the code to run (Used
        to delay the evaluation of the code inside until runtime).
    n : int
        Number of iterations.

    Returns
    -------
    float: time in seconds needed to evaluate the code.

    """
    start = time()
    for _ in range(n):
        func()
    end = time()
    return (end - start) / n

dawson_traprule = lambda x, N: np.exp(-1 * x ** 2) * traprule(0, x, lambda t: np.exp(t ** 2), N)
dawson_simprule = lambda x, N: np.exp(-1 * x ** 2) * simprule(0, x, lambda t: np.exp(t ** 2), N)
print("Q2a i:")
print("Trapezoid Rule:", dawson_traprule(4, 8))
print("Simpson's Rule:", dawson_simprule(4, 8))
print("Exact Value:", scis.dawsn(4))
print("")
print("Q2a ii:")
Nt = 200000
Ns = 1000
print("Trapezoid Rule Error: ", dawson_traprule(4, Nt) - scis.dawsn(4))
print("Number of Slices:", Nt)

print("Simpson's Rule Error:", dawson_simprule(4, Ns) - scis.dawsn(4))
print("Number of Slices:", Ns)

print("Traprule Time:", time_code(lambda: dawson_traprule(4, Nt), 10))
print("Simprule Time:", time_code(lambda: dawson_simprule(4, Ns), 10))
print("Scipy Function Time:", time_code(lambda: scis.dawsn(4), 1000))

print("")
print("Q2a iii:")
print("Traprule Error for N = 64:", np.abs(dawson_traprule(4, 32) - dawson_traprule(4, 64)) / 3)
print("Simprule Error for N = 64:", np.abs(dawson_simprule(4, 32) - dawson_simprule(4, 64)) / 15)
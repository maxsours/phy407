# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:43:07 2020

@author: Max Sours
"""
import numpy as np
import sys

def sign(x):
    """
    Compute the sign (that is, if it's positive or negative)
    of x.
    
    Return -1 iff x < 0
    Return 0 iff x = 0
    Return 1 iff x > 0
    """
    if (x == 0):
        return 0
    return 1 if x > 0 else -1

def f(x):
    """
    Define f(x) = 5e^-x + x - 5

    Parameters
    ----------
    x : float
        A real scalar value.

    Returns
    -------
    float: 
        f evaluated at x

    """
    return 5 * np.exp(-1 * x) + x - 5

def df(x):
    """
    Compute the derivative of f (the previous function) at x

    Parameters
    ----------
    x : float
        A real scalar value.

    Returns
    -------
    float: 
        f' evaluated at x

    """
    return -5 * np.exp(-1 * x) + 1

def binary_search(f, lower, upper, error):
    """
    Perform binary search to find a root of f within the bounds
    [lower, upper] to the specified error.
    
    Parameters
    ----------
    f : (float -> float)
        A continuous real-valued scalar function defined in
        the range [lower, upper].
    lower: float
        Lower limit of binary search
    upper: float
        Upper limit of binary search
    error : float
        Maximum error of result

    Returns
    -------
    float:
        root of f
    float:
        number of iterations
    """
    a = lower
    b = upper
    count = 0
    if sign(f(a)) == sign(f(b)): # This shouldn't happen if I choose my limits right.
        print("No root detected. Choose different limits.", file = sys.stderr)
        return np.nan(), 0
    while b - a > error:
        m = (b + a) / 2
        count += 1
        if sign(f(a)) == sign(f(m)): #If both f(a) and f(m) are the same sign, then the zero is betwen m and b
            a = m
        else:
            b = m
    return m, count

def newtons_method(f, df, x0, error):
    """
    Perform Newton's Method to find a root of f given initial
    position x0 to a specified error
    
    Parameters
    ----------
    f : (float -> float)
        A continuous real-valued scalar function defined in
        the range [lower, upper].
    df: (float -> float)
        Derivative of f with respect to x
    x0: float
        Starting position
    error : float
        Maximum error of result

    Returns
    -------
    float:
        root of f
    float:
        number of iterations
    """
    x = x0
    count = 0
    while np.abs(f(x)) > error:
        x = x - f(x) / df(x)
        count += 1
    return x, count

def relaxation_method(f, x0, error):
    """
    Perform relaxation method to find a root of f given initial
    position x0 to a specified error
    
    Parameters
    ----------
    f : (float -> float)
        A continuous real-valued scalar function defined in
        the range [lower, upper].
    x0: float
        Starting position
    error : float
        Maximum error of result

    Returns
    -------
    float:
        root of f
    float:
        number of iterations
    """
    x = x0
    count = 0
    while np.abs(f(x)) > error:
        # So I get to the next line of code by doing the 
        # following:
        # 0 = f(x)
        # 0 = -f(x)
        # x = -f(x) + x
        # This last equation is stable, unlike the obvious
        # fixed point equation of x = f(x) + x
        x = -1 * f(x) + x
        count += 1
    return x, count

def print_methods(x0):
    """
    Print the output of each of the three methods for a given
    starting position x0. (For binary search, x0 is the upper
    limit)
    """
    print("Binary Search:", binary_search(f, 3, x0, 1e-6))
    print("Newton's Method:", newtons_method(f, df, x0, 1e-6))
    print("Relaxation Method:", relaxation_method(f, x0, 1e-6))
    

if __name__ == "__main__":
    # Part b of the exersize
    print("For x0 = 5:")
    print_methods(5)
    print("For x0 = 100:")
    print_methods(100)
    print("For x0 = 10^10:")
    print_methods(1e10)
    # Part c of exersize
    x, _ = newtons_method(f, df, 3, 1e-6)
    h = 6.62e-34
    c = 3e8
    k = 1.36e-23
    lambda_ = 502.0e-9
    print("Temperature =", h * c /(k * x * lambda_))
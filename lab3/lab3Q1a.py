# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:10:34 2020

@author: Max Sours and Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
import scipy.special as scis

def gaussian_quadrature(f, a, b, n):
    """
    Integrate the function f from a to b using gaussian quadrature
    with n slices.
    
    Code is based on example on p.170 in the textbook.

    Parameters
    ----------
    f : (float -> float)
        1-D continuous function.
    a : float
        Lower limit of integration.
    b : float
        Upper limit of integration.
    n : int
        Number of slices.

    Returns
    -------
    Approximate value of f integrated from a to b.

    """
    x, w = gaussxwab(n, a, b)
    return np.sum([w[i] * f(x[i]) for i in range(n)])

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


if __name__ == "__main__":
    dawson_traprule = lambda x, N: np.exp(-1 * x ** 2) * traprule(0, x, lambda t: np.exp(t ** 2), N)
    dawson_simprule = lambda x, N: np.exp(-1 * x ** 2) * simprule(0, x, lambda t: np.exp(t ** 2), N)
    dawson_quadrature = lambda x, N: np.exp(-1 * x ** 2) * gaussian_quadrature(lambda t: np.exp(t ** 2), 0, x, N)
    trule_err = []
    srule_err = []
    quad_err = []
    trule_rerr = []
    srule_rerr = []
    quad_rerr = []
    d_4 = scis.dawsn(4)
    for n in np.logspace(3, 11, num=9, base=2):
        n = int(n)
        print("Number of Slices =", n)
        print("Trapezoid Rule:", dawson_traprule(4, n))
        print("Simpson's Rule:", dawson_simprule(4, n))
        print("Gaussian Quadrature:", dawson_quadrature(4, n))
        print("")
        trule_err.append(np.abs(dawson_traprule(4, 2*n) - dawson_traprule(4, n)))
        srule_err.append(np.abs(dawson_simprule(4, 2*n) - dawson_simprule(4, n)))
        quad_err.append(np.abs(dawson_quadrature(4, 2*n) - dawson_quadrature(4, n)))
        trule_rerr.append(np.abs((dawson_traprule(4, n) - d_4) / d_4))
        srule_rerr.append(np.abs((dawson_simprule(4, n) - d_4) / d_4))
        quad_rerr.append(np.abs((dawson_quadrature(4, n) - d_4) / d_4))
    
    plt.title("Comparing Error Measures for Various Integration Techniques")
    plt.loglog(np.logspace(3, 11, num=9, base=2), trule_err, label = "Traprule Error Approx")
    plt.loglog(np.logspace(3, 11, num=9, base=2), srule_err, label = "Simprule Error Approx")
    plt.loglog(np.logspace(3, 11, num=9, base=2), quad_err, label = "Quadrature Error Approx")
    plt.loglog(np.logspace(3, 11, num=9, base=2), trule_rerr, label = "Traprule Error")
    plt.loglog(np.logspace(3, 11, num=9, base=2), srule_rerr, label = "Simprule Error")
    plt.loglog(np.logspace(3, 11, num=9, base=2), quad_rerr, label = "Quadrature Error")
    plt.xlabel("Number of Slices")
    plt.ylabel("Error")
    plt.legend()
    plt.show()

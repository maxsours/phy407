# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:00:37 2020

@author: Anntara Khan(1002321891), Max Sours(1003816579)
"""
import numpy as np
import scipy as sci

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
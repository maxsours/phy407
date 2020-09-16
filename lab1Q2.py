# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:38:19 2020

@author: maxso
"""
import numpy as np
import matplotlib.pyplot as plt

"""
FUNCTION insect_pop(x_0, r, p_max)
    INPUT x_0, r: float
    INPUT p_max: int
    LET x be an empty 1xp_max array
    ASSIGN p <- 0
    WHILE p < p_max:
        COMPUTE x[p + 1] <- r * x[p](1 - x[p])
        INCREMENT p
    PLOT x, [0 , 1, ... , p_max]
"""

def insect_pop(x_0, r, p_max):
    """
    Return plots for the population of insects over time

    Parameters
    ----------
    x_0 : float
        Initial population of insects (as a fraction of max capacity)
    r : float
        Growth rate of population.
    p_max : int
        Maximum number of years for the plot.

    Returns
    -------
    x : 1xp_max float array
        Array of population (for plotting)
    p : 1xp_max int array
        Array of years (for plotting)
    """
    x = np.zeros(p_max)
    x[0] = x_0
    for i in range(p_max - 1):
        x[i + 1] = r * x[i] * (1 - x[i])
    return x, np.array(range(p_max))

x1, p1 = insect_pop(0.1, 2, 50)
plt.plot(p1, x1, label="r = 2")
x2, p2 = insect_pop(0.1, 3, 50)
plt.plot(p2, x2, label="r = 3")
x3, p3 = insect_pop(0.1, 4, 50)
plt.plot(p3, x3, label ="r = 4")
plt.legend()
plt.title("Insect Population for Various Growth Rates")
plt.xlabel("Number of Years")
plt.ylabel("Population of insects (as a fraction of max population)")
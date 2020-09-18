# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:38:19 2020

@author: Anntara Khan(1002321891), Max Sours(1003816579)
"""
import numpy as np
import matplotlib.pyplot as plt

#Part a

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

#Part b

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

#Part c

plt.figure(1)
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

#Part d

plt.figure(2)
for r in np.arange(2, 4, 0.005):
    x, p = insect_pop(0.1, r, 2000)
    length = 100 if r < 3 else 1000
    plt.plot(r*np.ones(length), x[-length:], "k.", markersize = 0.1)
    plt.title("Bifurcation Diagram")
    plt.xlabel("Maximum Growth Rate")
    plt.ylabel("Normalized Population")

#Part e

plt.figure(3)
for r in np.arange(3.738, 3.745, 0.00001):
    x, p = insect_pop(0.1, r, 2000)
    length = 100 if r < 3 else 1000
    plt.plot(r*np.ones(length), x[-length:], "k.", markersize = 0.1)
    plt.title("Bifurcation Diagram for r between 3.738 and 3.745")
    plt.xlabel("Maximum Growth Rate")
    plt.ylabel("Normalized Population")
    
#Part f
    
plt.figure(4)
x4, p4 = insect_pop(0.1, 3.8, 50)
x5, p5 = insect_pop(0.10001, 3.8, 50)
plt.plot(p4, x4, label = "x0 = 0.1")
plt.plot(p5, x5, label = "x0 = 0.10001")
plt.legend()
plt.title("Population Graphs for two initial conditions with r = 3.8")
plt.xlabel("Iterations")
plt.ylabel("Normalized Population")

#Part g

plt.figure(5)
plt.semilogy(p4, np.abs(x4 - x5), label="Measured Difference")
a = 0.00001
y = 0.45
plt.semilogy(p4[:24], a * np.exp(y * p4[:24]), label = "Exponential Fit - a = {0}, y = {1}".format(a, y))
plt.legend()
plt.title("Difference in Plots over Several Iterations")
plt.xlabel("Iterations")
plt.ylabel("Difference in Normalized Population")
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:07:37 2020

@author: Max Sours and Anntara Khan
"""
from lab3Q1a import gaussian_quadrature
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def P(u_10, T_a, t_h):
    """
    Calculate P as described in equation 2 of the lab.
    """
    mean_u = 11.2 + 0.365 * T_a + 0.00706 * T_a ** 2 + 0.9 * np.log(t_h)
    delta = 4.3 + 0.145 * T_a + 0.00196 * T_a ** 2
    I = gaussian_quadrature(lambda u: np.exp(-1 * (mean_u - u) ** 2 / (2 * delta ** 2)), 0, u_10, 100)
    return 1 / (np.sqrt(2 * np.pi) * delta) * I

if __name__ == "__main__":
    plt.clf()
    u_10s = (6, 8, 10)
    colours = ('r','g', 'b')
    t_hs = (24, 48, 72)
    lines=(':','-','--')
    T_a = np.linspace(-45, 5, 100) #T_a \in [-35, 5] deg C
    for (u_10, colour) in zip(u_10s, colours):
        for (t_h, line) in zip(t_hs, lines):
            plot_str = colour + line
            plt.plot(T_a, P(u_10, T_a, t_h), plot_str)
            print("Max Temp for (" + str(u_10) + ", " + str(t_h) + ") is", T_a[np.where(P(u_10, T_a, t_h) == np.max(P(u_10, T_a, t_h)))[0][0]])
    plt.title("Probability of blown snow as a function of Temperature")
    plt.xlabel("Temperature (deg C)")
    plt.ylabel("Probability of Blown Snow")
    custom_lines = [Line2D([0], [0], color='b', lw=8),
                Line2D([0], [0], color='g', lw=8),
                Line2D([0], [0], color='r', lw=8),
                Line2D([0], [0], color='k', lw=2, ls=':'),
                Line2D([0], [0], color='k', lw=2, ls='-'),
                Line2D([0], [0], color='k', lw=2, ls='--')]
    plt.legend(custom_lines, ["u_10 = 10", "u_10 = 8", "u_10 = 6", "t_h = 24", "t_h = 48", "t_h = 72"])
    plt.show()
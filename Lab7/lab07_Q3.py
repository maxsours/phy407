# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:30:38 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scii

# Code based off squarewell.py

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
a = 5.2918e-11     # Bohr radius
e0 = 8.8542e-12    # Permativity of free space
h = 0.002 * a
rinf = 20 * a
n = 2
l = 1

# Potential function
def V(r):
    return -1 * e ** 2 / (4 * np.pi * e0 * r)

def f(x,r,E):
    R = x[0] # S = r^2(dR/dr)
    S = x[1] # dS/dr = l(l + 1)R + 2mr^2/hbar^2 (V(r) - E)R
    fR = S / r ** 2
    fS = (2*m * (r/hbar)**2)*(V(r)-E)*R + l * (l + 1) * R
    return np.array([fR,fS])

def RK4(f, x, r, h):
    """
    Do a step of 4th order Runge-Kutta.
    Where
    f(x, r) = dx/dr
    x, r  are the inputs to f
    h is the increment of x to the next x value
    output the next y value
    """
    k1 = h * f(x, r)
    k2 = h * f(x+0.5*k1,r+0.5*h)
    k3 = h * f(x+0.5*k2,r+0.5*h)
    k4 = h * f(x+k3,r+h)
    return (k1+2*k2+2*k3+k4)/6
    
    

# Calculate the wavefunction for a particular energy
def solve(E):
    Rh = 0.0 # Set R(h), S(h)
    Sh = 1.0
    x = np.array([Rh,Sh])
    for r in np.arange(h,rinf,h):
        x += RK4(lambda x, r: f(x, r, E), x, r, h)

    return x[0]

def evaluate(E):
    """
    Evaluate the function for a specific value of E

    Parameters
    ----------
    E : float
        energy of the system

    Returns
    -------
    2xk array of f values evaluated for k values of r
    """
    Rh = 0.0
    Sh = 1.0
    r = np.arange(h, rinf, h)
    x = np.empty((2, r.size))
    x[:, 0] = np.array([Rh, Sh])
    for i in np.arange(1, r.size):
        x[:, i] = x[:, i - 1] + RK4(lambda x, r: f(x, r, E), x[:, i - 1], r[i - 1], h)
    return x, r

def analytic(r, n, l):
    """
    Evaluate r with a specified function given n, l. Correct
    R functions for each n, l obtained from
    http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/hydwf.html

    Parameters
    ----------
    r : 1xk float array
        r values to compute the analytic funciton for
    n : float
        n value for waveform
    l : float
        l value for waveform

    Returns
    -------
    1xk float array
        R values evaluated at each r

    """
    # The constants in front are to scale the R function to
    # roughly match the numerical solution in magnitude
    if n == 1 and l == 0:
        return 0.005 * np.exp(-1 * r / a)
    if n == 2 and l == 0:
        return 0.002 * (2 - r / a) * np.exp(r / (-2 * a))
    if n == 2 and l == 1:
        return 6e-6 * r / a * np.exp(r / (-2 * a))
    return r # default case - should never be used

# Main program to find the energy using the secant method
E1 = -15 * e / n ** 2
E2 = -13 * e / n ** 2
R2 = solve(E1)

target = e/1000
while abs(E1-E2)>target:
    R1, R2 = R2, solve(E2)
    E1, E2 = E2,E2- R2*(E2-E1)/(R2-R1)

print("E =",E2/e,"eV")

x, r = evaluate(E2)
normal = scii.simps(x[0, :] ** 2, r)
plt.title("R(r) for when n = " + str(n) + ", l = " + str(l))
plt.ylabel("R")
plt.xlabel("r(m)")
plt.plot(r, x[0, :] / normal, label = "Numerical Solution")
plt.plot(r, analytic(r, n, l), label = "Analytic Solution")
plt.legend()


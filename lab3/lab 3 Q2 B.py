# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:44:11 2020

@author: Max Sours and Anntara Khan
"""

import numpy as np
import math as math
import matplotlib.pyplot as plt


x_val = np.linspace(-10, 10, 100)

def psi(n,x):
    def H(n):
        if n==0:
            return 1
        elif n==1:
            return 2*x
        else:
            return 2 * x * H(n-1) - 2 * (n-1) * H(n-2)
    return (((np.exp((-x**2)/2)) *H(n)) / np.sqrt((2**n) * (math.factorial(n)) * np.sqrt(math.pi)))

psi30 = [psi(30, i) for i in x_val]

plt.plot (x_val, psi30) 
plt.title("Harmonic oscillator Function")
plt.xlabel("x")  
plt.ylabel ("PSI") 
plt.show()

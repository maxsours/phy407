# -*- coding: utf-8 -*-
"""
@author: Anntara Khan(1002321891), Max Sours(1003816579)
"""
import numpy as np
import scipy as sp
import math as math
import matplotlib.pyplot as plt

x_val = np.linspace(-4, 4, 100)

def psi(n,x):
    def H(n):
        if n==0:
            return 1
        elif n==1:
            return 2*x
        else:
            return 2*x*H(n-1)-2*(n-1)*H(n-2)
    return (((np.exp(-(x**2)/2))*H(n))/np.sqrt((2**n)*(math.factorial(n))*np.sqrt(math.pi)))

psi0 = [psi(0, i) for i in x_val]
psi1 = [psi(1, i) for i in x_val]
psi2 = [psi(2, i) for i in x_val]
psi3 = [psi(3, i) for i in x_val]
  
plt.plot (x_val, psi0)
plt.plot (x_val, psi1)
plt.plot (x_val, psi2)
plt.plot (x_val, psi3)  
plt.title("Harmonic Osccilator")
plt.xlabel('x')
plt.ylabel('psi')
plt.legend(['n = 0', 'n = 1', 'n = 2', 'n = 3'])  
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:06:55 2020

@author: annta
"""

import numpy as np
import scipy as sp
import math as math
import matplotlib.pyplot as plt

x_val = np.linspace(-4, 4, 20)

def psi(n,x):
    def H(n,x):
        if n==0:
            return 1
        elif n==1:
            return 2*x
        else:
            return 2*x*H(x,n-1)-2*(n-1)*H(x,n-2)
    return (((np.exp(-(x**2)/2))*H(n,x))/np.sqrt((2**n)*(math.factorial(n))*np.sqrt(math.pi)))

psi0 = [psi(0, i) for i in x_val]
psi1 = [psi(1, i) for i in x_val]
psi2 = [psi(2, i) for i in x_val]
psi3 = [psi(3, i) for i in x_val]

plt.plot (x_val, psi0)
plt.plot (x_val, psi1)
plt.plot (x_val, psi2)
plt.plot (x_val, psi3)    
plt.show()

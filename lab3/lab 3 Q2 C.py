# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:50:50 2020

@author: annta
"""
'''
from gaussxw import gaussxwab
from math import exp
def f(z):
return exp(-z**2/(1-z)**2)/(1-z)**2 
N 50
a 0.0
b 1.0
x,w = gaussxwab(N,a,b)
s = 0.0
fork in range(N):
s += w[k]•f(x[k])
print(s) '''

import scipy.integrate as integrate
import numpy as np
import math as math
import matplotlib.pyplot as plt 
from gaussx import gaussxwab

def E(n, x):
    
    def X(n, x):
        
        def psi(n, x):
            
            def H(n, x):
                if n == 0:
                    return 1
                elif n == 1:
                    return 2 * x
                else:
                    return 2 * x *H(x, n-1) -2 * (n-1) * H(x, n-2)
            
            n_psi = (((np.exp(-(x**2)/2)) * H(n,x)) / np.sqrt((2**n) * (math.factorial(n)) * np.sqrt(math.pi)))
            return x * (abs(n_psi))
    
    def P(n, x):
        
        def xd_psi(n, x):
            
            def d_H(n, x):
                if n.all == 0:
                    return 0
                elif n.all == 1:
                    return 2
                else:
                    return -x * d_H(x, n-1) + 2 * (n-1) * d_H(x, n-2)
            d_psi = (((np.exp(-(x**2)/2))* d_H(n,x)) / np.sqrt((2**n) * (math.factorial(n)) * np.sqrt(math.pi))) 
            
            return (abs(d_psi))
        
        return integrate.quad (xd_psi(n, x), -np.inf, np.inf)
    return X(n, x) + P(n, x)

N = 100
a = 0.0
b = 1.0
x,w = gaussxwab(N,a,b)
s = 0.0
n = np.linspace(0, 15, 100)
for k in range(N):
    s += w[k]*E(n, x[k])
print(s) 
    
    

















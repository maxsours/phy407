# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:50:50 2020

@author: annta
"""
import scipy.integrate as integrate
import numpy as np
import math as math
import matplotlib.pyplot as plt 
from gaussx import gaussxwab
def E(n, x):
    def psi_x(n, x):
        def psi(n,x):
            def H(n):
                if n == 0:
                    return 1
                elif n == 1:
                    return 2*x
                else:
                    return 2 * x * H(n-1) - 2 * (n-1) * H(n-2)
            return (((np.exp((-x**2)/2)) *H(n)) / np.sqrt((2**n) * (math.factorial(n)) * np.sqrt(math.pi)))
        return (x**2)*(abs(psi(n, x)))**2
    
    N = 100
    z = 15
    a = -np.inf
    b = np.inf
    x,w = gaussxwab(N,a,b)
    s1 = 0.0
    
    for k in range(N):
        for i in range(z):
            s += w[k]*psi_x(z, x[k])
    
    print(s1)
    
    def psi_p(n, x):
        def xd_psi(n, x):
            def d_H(n):
                if n == 0:
                    return 0
                elif n == 1:
                    return 2
                else:
                    return -x * d_H(x, n-1) + 2 * (n-1) * d_H(x, n-2)
            d_psi = (((np.exp(-(x**2)/2))* d_H(n,x)) / np.sqrt((2**n) * (math.factorial(n)) * np.sqrt(math.pi))) 
            return (abs(d_psi))
        N = 100
        z = 15
        a = -np.inf
        b = np.inf
        x,w = gaussxwab(N,a,b)
        s2 = 0.0
        
        for k in range(N):
            for i in range(z):
                s += w[k]*psi_p(z, x[k])
        
        print(s2)
    

















# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:13:47 2020

@author: annta
"""
'''this program uses scipys Bessel functinos to plot same graph as Q2.b(1)'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

x = np.linspace(0, 20, 1000)

for v in range (0, 3):
    plt.plot(x, sp.jv(v, x))
    plt.title("Scipy Bessel function")
    plt.xlabel('values of x')
    plt.ylabel('J(x)')
    plt.legend(['J0', 'J1', 'J2'])
    plt.savefig('spipy bessel.png')
    plt.show

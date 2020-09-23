# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:38:01 2020

@author: 
    Anntara Khan (1002321891)
    Max Sours ()
"""
#LAB2 QUESTION 1
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sp

DX = -np.exp(-(.5)**3)

def func(x):
        return np.exp(-x**2)

def derive(x, h):
        return (func(x+h)-func(x))/h
    
def central_difference(x, h):
    return (func(x+h)-func(x-h))/h

h_range = np.logspace(-16, 0, num = 17)
error = []


for h in h_range:
    
    dx1 = derive(0.5, h)
    error.append(dx1-DX)

for h in h_range:
    
    dx1 = central_difference(0.5, h_range)
    error1 = dx1-DX
    
plt.loglog(h_range, error)
plt.plot(error1, h_range)
plt.title('comparing errors')
plt.xlabel('steps (h)')
plt.ylabel('error')
plt.savefig('steps over error.png')
plt.show





    



    

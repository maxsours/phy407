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
"""
the derivative of the function, f(x) = e^(-x^2) is -2xe^(-x^2)
the first fuction is to define f(x) in python for using in the the rest of the funtions
the second fuction would take the first function and derive it by taking the slope of 
a small change forward (x+h) in x.
the 3rd fuction would take the first function and derive it by taking the slope of the 
small change forward and backward 
the functions are implemented for small change of h from 0 to 10^-16
and then the error is taken by taking the difference between the analytic value and the
numeric value (for both forward difference and central difference)
"""
x = 0.5
DX = -2*x*(np.exp(-x**2))

def func(x):
        return np.exp(-x**2)
    
def derive(x, h):
        return (func(x+h)-func(x))/h
    
def central_difference(x, h):
    return (func(x+h)-func(x-h))/h

h_range = np.logspace(-16, 0, num = 17)
error = []

for h in h_range:
    dx1 = derive(x, h)
    error.append(dx1-DX)
    e = np.abs(error)

for h in h_range:
    dx1 = central_difference(x, h_range)
    error1 = dx1-DX
    
plt.loglog(h_range, error)
plt.plot(error1, h_range)
plt.title('comparing errors')
plt.xlabel('steps (h)')
plt.ylabel('error')
plt.savefig('steps over error.png')
plt.show

print (dx1)
print (e)

    



    

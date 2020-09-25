# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:38:01 2020

@author: 
    Anntara Khan (1002321891)
    Max Sours (1003816579)
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
x = 0.5 #value of x is given
DX = -2*x*(np.exp(-x**2)) #numeric derivation of the function

#defining the function 
def func(x):
        return np.exp(-x**2)

#defining the derivative function using forward difference scheme
def derive(x, h):
        return (func(x+h)-func(x))/h

#defining the derivative function using central difference scheme
def central_difference(x, h):
    return (func(x+h)-func(x-h))/(2 * h)

#creating an array for h
h_range = np.logspace(-16, 0, num = 17)
#setting an empty list for errors
error = []

#doing the derivation, and checking the error (Q1.C)
dx1 = derive(x, h_range)
error = np.abs(dx1-DX)
    
#doing the derivation, and checking the error (Q1.D)
dx1 = central_difference(x, h_range)
error1 = np.abs(dx1-DX)

#plotting everything togeather
plt.loglog(h_range, error, label = "Regular Derivative")
plt.loglog(h_range, error1, label = "Central Difference")
plt.title('Comparing Errors')
plt.xlabel('steps (h)')
plt.ylabel('error')
plt.legend()
plt.show()


    

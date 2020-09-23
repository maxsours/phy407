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

h_range = np.arange(-16,0) #not sure if it shouold be 1 or 0

for h in h_range:
        
    def func(x):
        return np.exp(-x**2)
        
    def derive(x):
        return (func(x+h)-func(x))/h
    
    dx1 = derive(0.5)
    dx2 = sp.derivative(func, 0.5)

    error = dx1-dx2
    print (error)
   
plt.plot(error, h_range)
plt.show



    



    
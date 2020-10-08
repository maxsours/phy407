
"""
Created on Tue Oct  6 13:32:48 2020

Anntara Khan (1002321891)
Max Sours(1003816579)
"""

#LAB 4 Q3(B)

import numpy as np
import matplotlib.pyplot as plt

def func(x,c):
    return (1-np.exp(-c*x))

def relax_method(c):
    x_0 = 1
    w = 0.01
    accuracy = 10**-6
    error = 1
    count = 0
    while error>accuracy:
        x = ((1 + w) * func(x_0,c)) - (w * x_0)
        error = np.abs(func(x,c) - func(x_0,c))
        x_0  = x
    return x
    
x_1 = relax_method(2)

def relax_method_count(c):
    x_0 = 1
    w = 0.5
    accuracy = 10**-6
    error = 1
    count = 0
    while error>accuracy:
        count = count + 1
        x = ((1 + w) * func(x_0,c)) - (w * x_0)
        error = np.abs(func(x,c) - func(x_0,c))
        x_0  = x
    return count
C_1 = relax_method_count(2)

print (x_1, C_1)    

x_val = []

c = np.linspace(0, 3, 300)

for i in range(len(c)):
    y_val = relax_method(c[i])
    x_val.append(y_val)
    
plt.plot(c,x_val)
plt.title("over relaxation method")
plt.xlabel("C")
plt.ylabel("X")
plt.show()

    
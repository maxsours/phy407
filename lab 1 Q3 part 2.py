# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:43:33 2020

@author: stone
"""


import numpy as np
import matplotlib.pyplot as plt
from time import time # import the "time" function from the "time" module

'''
psuedo code
A and B will be two constant matrices, with  N colums and rows, the marices will be created using numpy.ones.
A will be a NxN matrix made of 3
B will be a NxN matrix made of 5
N is selected to be 200, we're using a for loop to run the through every value of N from 0 to 200, 
in every iteration the for loop will save the time it took to run each iteration, 
and save it onto a list that will be used to plot the N vs Time plot. 
For the matrix multiplication numpydot is used, which calculates the dot product of 2 matrices in this case A and B, for every value of N.
using matplotlib the N over Time is plotted, the slope of the graph is the speed of the program
'''
N = 200 #size of the matrix
N1 = [0] #list to plot the y-axis
A = np.ones([N, N], float)*3 #the matrix A
B = np.ones([N, N], float)*5 #the matrix B

start1 = time() #saves the start time
T = [start1] #list to plot the x-axis
#for loop to run the calculation
for i in range(N):
      C = np.dot(A,B) #find the dotproduct of matrix A & B for 0-200
      T.append(time()) #adds to the list everytime the for loop runs
      N1.append(i) #adds to the list everytime the for loop runs
end1 = time() #saves the end time
diff1 = (end1-start1) # the time it took for the function to run
slope = n/diff1 #calculates the slope aka the speed of the program
print (slope) #prints the value of the slope
plt.plot(T, N1) #plots the graph
plt.xlabel('time')
plt.ylabel('N')
plt.savefig('N over Time (npdot).png')
plt.show()

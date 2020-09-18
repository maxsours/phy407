# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:46:48 2020

@author: Anntara Khan, Max Sours
"""

import numpy as np
import matplotlib.pyplot as plt
from time import time 

'''
psuedo code
A and B will be two constant matrices, with  N colums and rows, the marices will be created using numpy.ones.
A will be a NxN matrix made of 3
B will be a NxN matrix made of 5
N is selected to be 200, we're using a for loop to run the through every value of N from 0 to 200, 
in every iteration the for loop will save the time it took to run each iteration, 
and save it onto a list that will be used to plot the N vs Time plot. 
The for loop also multiplies the metrices A and B to Get the matrix C for every value of N.
using matpltlib the N over Time is plotted, the slope of the graph is the speed of the program
'''
N = 200 #size of the matrix
N1 = [0] #list to plot the y-axis
A = np.ones([N, N], float)*3 #the matrix A
B = np.ones([N, N], float)*5 #the matrix B

start1 = time() #saves the start time
T = [start1] #list to plot the x-axis
C = np.zeros([N,N] ,float) #defining the Matrix C
#for loop to run the calculation
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j] += A[i,k]*B[k,j] #multiplies the matrix for 0-200
            T.append(time()) #adds to the list everytime the for loop runs
            N1.append(i) #adds to the list everytime the for loop runs
end1=time() #saves the end time
diff1 = (end1-start1) # the time it took for the function to run
slope = N/diff1 #calculates the slope aka the speed of the program
print ("therefore the speed of matrix multiplication is ", slope, "iterations per second") #prints the value of the slope
plt.plot(T, N1) #plots the graph
plt.xlabel('time')
plt.ylabel('N')
plt.savefig('N over Time (matrix multiply).png')
plt.show()


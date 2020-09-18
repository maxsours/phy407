# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:46:48 2020

@author: Anntara Khan(1002321891), Max Sours(1003816579)
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
N_range = np.arange(2,80)

time_byhand = []
time_dot = []
for N in N_range:
    A = np.ones([N, N], float)*3 #the matrix A
    B = np.ones([N, N], float)*5 #the matrix B
    C1 = np.zeros([N,N] ,float) #defining the Matrix C
    start1 = time() #saves the start time
    
    #nested for loops implement matrix multiplication as done by hand
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C1[i,j] += A[i,k]*B[k,j]
    end1=time()
    time_byhand.append(end1-start1) # the time it took for the function to run
    
    start2 = time()
    C2 = np.dot(A, B)
    end2 = time()
    time_dot.append(end2 - start2)
    assert(C1.all() == C2.all()) # The two methods should create the same matrix
    
plt.figure(1)
plt.plot(N_range, time_byhand, label = "By Hand")
plt.plot(N_range, time_dot, label = "Numpy Dot")
plt.title('N over Time (matrix multiply)')
plt.xlabel('N')
plt.ylabel('Time')
plt.legend()
plt.figure(2)
plt.plot(N_range**3,time_byhand, label = "By Hand")
plt.plot(N_range ** 3, time_dot, label = "Numpy Dot")
plt.title('N^3 over Time (matrix multiply)')
plt.xlabel('N^3')
plt.ylabel('Time')
plt.legend()
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:46:48 2020

@author: Anntara Khan, Max Sour
"""

import numpy as np
import matplotlib.pyplot as plt
from time import time # import the "time" function from the "time" module

'''
psedo code
A and B will be two constant matrices, with  N colums and rows, the marices will be created using numpy.ones.
A will be a NxN matrix made of 3
B will be a NxN matrix made of 5

'''


 

N = 5
#N1 = np.arange(0, N, 1)
A = np.ones([N, N], float)*3
B = np.ones([N, N], float)*5

# save start time
start1 = time()
# run your calculation
C = np.zeros([N,N] ,float)
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j] += A[i,k]*B[k,j] 
            print (C)
end1=time()
# the difference is the elapsed time (in seconds)
diff1 = (end1-start1)

#T1 = np.arange(start1, end1, 0.01)

#print (T1)
plt.plot(diff1, N)
plt.xlabel('time')
plt.ylabel('N')
plt.show()

'''
# save start time
start2 = time()
# run your calculation
for i in range(N):
      C= np.dot(A,B)
      print(C)

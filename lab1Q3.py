# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:46:48 2020

@author: Anntara Khan, Max Sours
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
N = 1000
A = np.ones([N, N], float)*3
B = np.ones([N, N], float)*5
#C = np.ones([N, N], float)


# save start time
start = time()
# run your calculation
for i in range(N):
    for j in range(N):
        for k in range (N):
            C=A[i,k]*B[k,j]
            print(C)

# here are lines indented in the for loop
# here are more lines indented in the for loop
# save the end time
end=time()
# the difference is the elapsed time (in seconds)
diff=end-start
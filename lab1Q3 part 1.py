# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:46:48 2020

@author: Anntara Khan, Max Sours
"""

import numpy as np
import matplotlib.pyplot as plt
from time import time # import the "time" function from the "time" module

'''
psuedo code
A and B will be two constant matrices, with  N colums and rows, the marices will be created using numpy.ones.
A will be a NxN matrix made of 3
B will be a NxN matrix made of 5

'''

N = 200
N1 = [1]
A = np.ones([N, N], float)*3
B = np.ones([N, N], float)*5

# save start time
start1 = time()
# run your calculation
T = [start1] 
C = np.zeros([N,N] ,float)
#print (T)
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j] += A[i,k]*B[k,j] 
            T.append(time())
            N1.append(i)
            #print (C)
            #print (T)
end1=time()
# the difference is the elapsed time (in seconds)
diff1 = (end1-start1)

#T1 = np.arange(start1, end1, 0.01)

#print (T1)
plt.plot(T, N1)
plt.xlabel('time')
plt.ylabel('N')
plt.savefig('N over time2.png')
plt.show()


# save start time
start2 = time()
# run your calculation
for i in range(N):
      C= np.dot(A,B)
      T.append(time())
      N1.append(i)
      #print(C)


# here are lines indented in the for loop
# here are more lines indented in the for loop
# save the end time
end2=time()
# the difference is the elapsed time (in seconds)
diff2=end2-start2

print (diff2)
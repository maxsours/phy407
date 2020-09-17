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

'''

N = 200
N1 = [1]
A = np.ones([N, N], float)*3
B = np.ones([N, N], float)*5

# save start time
start1 = time()
# run your calculation
T = [start1] 

# save start time
start = time()
# run your calculation
for i in range(N):
      C = np.dot(A,B)
      T.append(time())
      N1.append(i)
      #print(C)


# here are lines indented in the for loop
# here are more lines indented in the for loop
# save the end time
end=time()
# the difference is the elapsed time (in seconds)
diff=end-start
print (diff)

plt.plot(T, N1)
plt.xlabel('time')
plt.ylabel('N')
plt.savefig('N over time.png')
plt.show()
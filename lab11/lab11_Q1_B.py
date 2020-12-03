""" 
parts of the code is taken from salesman.py

Anntara Khan (1002321891)
Max Sours(1003816579)

"""
# import modules
#from random import random, standard_normal
from numpy.random import random, standard_normal
import numpy as np
import matplotlib.pyplot as plt

# choosing the initital values
Tmax = 10 #using the same value as salesman.py
Tmin = 1e-3 # really small number that's grater than 0
tau = 1e2 # guessing the cooling time
x0 = 2 # given in the question

## PART A ##

def f(x):
    return (x ** 2) - (np.cos(4 * np.pi * x))

# setting the dependednt variables fro the initital values

y = f(x0) # value of the function at 2
t = 0 # initial time
T = Tmax # setting intial temp to Tmax, and as it cools down T will update till it reaches Tmin
x = x0 #setting x to the initial value
xpoints = [] #empty list to store the x values

# MAIN LOOP

while T>Tmin:
	
	t = t + 1 # moving forward in time
	T = Tmax * np.exp(-t / tau) # cooling down
	
	x_0 = x # saves the value of x at the begining of the loop
	y_0 = y # saves the value of y at the begining of the loop
	x = standard_normal() # random gaussian generator, to get a new value of x to complete the loop
	y = f(x) # new y based on the new random x
	xpoints.append(x) #stores the new value of x in the list
	delta_y = y - y_0 # get the change in y for probability acceptance
	
    # probability acceptance, if failed switches x and y to the initially saved value
	if random() >= np.exp(-delta_y / T):
		x = x_0
		y = y_0	

#prints the final value of x and f(x) at the end of the while loop
print("the final value of x at the end would be, ", x)
print("the final value of f(x) at the end would be, ", y)

plt.figure()
plt.title("For f(x), Value of x over Time")
plt.xlabel("Time")
plt.ylabel("X")
plt.plot(xpoints, 'g_', linewidth = .01)
plt.show()

#------------------------------------------------------------------------------#

# PART B #

def g(x):
	if x>0 and x<50:
		return (np.cos(x) + np.cos(np.sqrt(2) * x) + np.cos(np.sqrt(3) * x))
	else:
		print("x is out of bounds")

y = f(x0) # value of the function at 2
t = 0 # initial time
T = Tmax # setting intial temp to Tmax, and as it cools down T will update till it reaches Tmin
x = x0 #setting x to the initial value
xpoints = [] #empty list to store the x values

# MAIN LOOP

while T>Tmin:
	
	t = t + 1 # moving forward in time
	T = Tmax * np.exp(-t / tau) # cooling down
	
	x_0 = x # saves the value of x at the begining of the loop
	y_0 = y # saves the value of y at the begining of the loop
	x = standard_normal() # random gaussian generator, to get a new value of x to complete the loop
	y = f(x) # new y based on the new random x
	xpoints.append(x) #stores the new value of x in the list
	delta_y = y - y_0 # get the change in y for probability acceptance
	
    # probability acceptance, if failed switches x and y to the initially saved value
	if random() >= np.exp(-delta_y / T):
		x = x_0
		y = y_0	

#prints the final value of x and f(x) at the end of the while loop
print("the final value of x at the end would be, ", x)
print("the final value of g(x) at the end would be, ", y)

plt.figure()
plt.title("For g(x), Value of x over Time")
plt.xlabel("Time")
plt.ylabel("X")
plt.plot(xpoints, 'r_', linewidth = .01)
plt.show()



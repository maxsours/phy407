""" 
Modifying 'L11-Ising1D-start.py' from the lab manual 

Anntara Khan (1002321891)
Max Sours(1003816579)

"""
# import modules
import numpy as np
from random import randrange
import matplotlib.pyplot as plt

## LAB 11, Newman 10.9 ##

# random number generator
rand_num_gen = np.random.default_rng()
# define constants
kB = 1.0
T = 1.0
J = 1.0
B = 1/(kB * T)
num_dipoles = 100
N = 100
t = 1000000

## PART A

def energyfunction(J, dipoles):
    """ function to calculate energy """
    energy = -J*np.sum(dipoles[0:-1]*dipoles[1:])
    return energy

def acceptance(d_E):
    """ Function for acceptance probability; using Metropolis acceptance formula """
    P_a = 1 if d_E <= 0 else np.exp(-d_E * B)
    return True if rand_num_gen.random() < P_a else False
  # result is True of False

def dipole():
    """ Function to generate array of dipoles and initialize diagnostic quantities"""
    d_0 = np.empty([N, N], dtype = int)
    def random_dipole():
        x = randrange(0, 2, 1)
        if x == 0:
            return 1
        else:
            return -1
    for i in range(0, N):
        for j in range (0,N):
            d_0[i, j] = random_dipole()
    return d_0

def rev(spin):
    """ Function to flip the spin"""
    return 1 if spin == -1 else -1

dipoles_0 = dipole()
dipoles = dipole()


energy = []  # empty list; to add to it, use energy.append(value)
magnet = []  # empty list; to add to it, use magnet.append(value)
flips = [0]  # counting the number of flips starting at 0

# setting the initial values 
E = energyfunction(J, dipoles) # energy before the first timestep
energy.append(E)
magnet.append(np.sum(dipoles)) # magnetization before the first timestep


## main loop

for a in range(t):
    i = rand_num_gen.integers(0, N) # generates a random number between 0 to N
    j = rand_num_gen.integers(0, N) # generates a random number between 0 to N
    
    picked = randrange(N)  # choose a victim
    dipoles[picked] *= -1  # propose to flip the victim
    Enew = energyfunction(J, dipoles)  # compute Energy of proposed new state
    d_E = Enew - E
    # calculate acceptance probability
    if acceptance(d_E):
        dipoles[i, j] = rev(dipoles[i, j])
        energy.append(d_E) # if the new probability is accepted the new energy is stored
        magnet.append(np.sum(dipoles)) # if the new probability is accepted the new magnetization is stored
        flips.append(a)


# plots the energy after each flip
plt.figure()
plt.title("At T = 1, Energy after each Flip")
plt.ylabel("Energy")
plt.xlabel("Flips")
plt.plot (flips, energy)
plt.show

# plots the magnetization after each flip
plt.figure()
plt.plot(flips, magnet)
plt.title("At T = 1, Magnetization after each Flip")
plt.ylabel("Magnetization")
plt.xlabel("Flips")
plt.show()

# plots the initial state
plt.figure()
plt.title("At T = 1, Initial State")
plt.imshow(dipoles_0)

# plots the state after 1000000 steps
plt.figure()
plt.title("At T = 1, State After 1000000 Steps")
plt.imshow(dipoles)

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:44:53 2020

@author: Max Sours and Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt
from time import time


def calculate_voltage(omega = 0):
    # Code modelled after laplace.py
    # Constants
    M = 100         # Grid squares on a side
    V = 1.0         # Voltage at top wall
    target = 1e-6   # Target accuracy
    
    # Create arrays to hold potential values
    phi = np.zeros([M+1, M+1], float)
    phi[20:80, 20] = V # Initial conditions here
    phi[20:80, 80] = -1 * V
    
    # Return true iff the square given by i, j is part of the boundary condition (not including if it's an edge)
    boundary_condition = lambda i, j: (j == 20 or j == 80) and i >= 20 and i < 80
    
    # Main loop
    delta = 1.0
    while delta > target:
        delta = 0.0 # Needed to calculate maximum delta. This value should be immediately replaced in the first iteration
        for i in range(M+1):
            for j in range(M+1):
                if not (i == 0 or i == M or j == 0 or j == M or boundary_condition(i, j)):
                    new_phi = (1 + omega) * (phi[i+1, j] + phi[i-1, j] 
                                             + phi[i, j+1] + phi[i, j-1])/4 - omega * phi[i, j]
                    # Since there aren't two different arrays to compare, delta has to be calculated here and compared to the max value of delta found so far
                    new_delta = np.abs(new_phi - phi[i, j])
                    delta = new_delta if new_delta > delta else delta
                    phi[i, j] = new_phi
    return phi

if __name__ == "__main__":
    omega = 0.5
    start = time() # I'm timing how long the algorithm takes for each omega to compare the different values
    phi = calculate_voltage(omega)
    end = time()
    print("Time for omega = " + str(omega) + ":", end - start)
    
    plt.contour(phi) # Plot the contour plot
    plt.title("Voltage Contour Plot, $\omega$ = " + str(omega))
    plt.xlabel("x")
    plt.ylabel("y")
    cbar = plt.colorbar()
    cbar.set_label("Voltage (V)")
    plt.show()
    
    # Plot stream plot, as shown by the code in the Lab
    x = np.arange(101)
    Ey, Ex = np.gradient(-phi, x, x)
    # careful about order
    fig = plt.figure(figsize=(6, 3))
    strm = plt.streamplot(x, x, Ex, Ey, color=phi, linewidth=2, cmap='autumn')
    cbar = fig.colorbar(strm.lines)
    cbar.set_label('Potential $V$')
    plt.title('Electric field lines, $\omega$ =' + str(omega))
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:41:16 2020

@author: Max Sours, Anntara Khan
"""
import struct
import numpy as np
import matplotlib.pyplot as plt

"""
PSEUDOCODE

function READ_ELEV(filepath):
    file = open(filepath, "rb")
    let elev_array be an 1201 x 1201 array of ints
    let grad_array be an 1201 x 1201 array of 2-D vectors
    while int val = file.readtwobytes() until done:
        store val in next open slot of elev_array
    for val in elev_array:
        let grad be a 2-D vector
        
        if val on west border:
            grad.x = (east(val) - val) / dist
        if val on east border:
            grad.x = (val - west(val)) / dist
        otherwise:
            grad.x = central_difference(east(val), west(val))
        
        if val is on north border:
            grad.y = (val - south(val)) / dist
        if val on south border:
            grad.y = (north(val) - val) / dist
        otherwise:
            grad.y = central_difference(north(val), south(val))
            
        store grad in next open slot of grad_array
    
    calculate I = -(cos(theta)(dw/dx) + sin(theta)(dw/dy)) / sqrt((dw/dx)^2 + (dw/dy)^2 + 1)
    plot2D(elev_array)
    plot2D(I)
"""

def read_elevation(filepath):
    """
    Read elevation data from filepath, then output arrays of elevation and
    intensity data.
    """
    h = 83 #distance between elevation measures
    N = 1201
    theta = np.pi / 6
    elev_array = np.zeros((N, N))
    grad_array = np.zeros((N, N, 2))
    I_array = np.zeros((N, N))
    # Read the elevation data as described in Question 3, and store in the elvation array
    f = open(filepath, "rb")
    for i in range(N):
        for j in range(N):
            buf = f.read(2)
            val = struct.unpack(">h", buf)[0]
            elev_array[i][j] = val
    f.close()
    # Populate the gradient array
    for i in range(N):
        for j in range(N):
            #This if statements handle the border cases
            if j == 0:
                grad_array[i][j][0] = (elev_array[i][j+1] - elev_array[i][j]) / h
            elif j == N - 1:
                grad_array[i][j][0] = (elev_array[i][j] - elev_array[i][j-1]) / h
            else:
                grad_array[i][j][0] = (elev_array[i][j+1] - elev_array[i][j-1]) / (2 * h)
            
            if i == 0:
                grad_array[i][j][1] = (elev_array[i][j] - elev_array[i-1][j]) / h
            elif i == N - 1:
                grad_array[i][j][1] = (elev_array[i-1][j] - elev_array[i][j]) / h
            else:
                grad_array[i][j][1] = (elev_array[i-1][j] - elev_array[i+1][j]) / (2 * h)
    
    # Populate intensities
    for i in range(N):
        for j in range(N):
            denom = np.sqrt(grad_array[i][j][0] ** 2 + grad_array[i][j][1] ** 2 + 1)
            numer = np.cos(theta) * grad_array[i][j][0] + np.sin(theta) * grad_array[i][j][1]
            I_array[i][j] = -1 * numer / denom
    
    return elev_array, I_array

if __name__ == "__main__":
    elev_array, I_array = read_elevation("N46E006.hgt")
    plt.figure(1)
    plt.title("Elevation Map of Lake Geneva")
    plt.imshow(elev_array, vmin = 0, cmap="gray") #vmin needs to be set to 0 since the incorrect measurements record as a large negative number
    plt.colorbar()
    plt.figure(2)
    plt.title("Intensity Map of Lake Geneva")
    plt.imshow(I_array, cmap = "gray")
    plt.figure(3)
    plt.title("Zoomed in on Evian")
    plt.imshow(I_array[700:900, 600:800], cmap = "gray")
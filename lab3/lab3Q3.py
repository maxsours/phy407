# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:41:16 2020

@author: Max Sours, Anntara Khan
"""
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
        if val is on north border:
            grad.x = (val - south(val)) / dist
            grad.y = central_difference(east(val), west(val))
        if val on south border:
            grad.x = (north(val) - val) / dist
            grad.y = central_difference(east(val), west(val))
        if val on west border:
            grad.x = central_difference(north(val), south(val))
            grad.y = (east(val) - val) / dist
        if val on east border:
            grad.x = central_difference(north(val), south(val))
            grad.y = (val - west(val)) / dist
        otherwise:
            grad.x = central_difference(north(val), south(val))
            grad.y = central_difference(east(val), west(val))
        store grad in next open slot of grad_array
    
    calculate I = -(cos(theta)(dw/dx) + sin(theta)(dw/dy)) / sqrt((dw/dx)^2 + (dw/dy)^2 + 1)
    plot2D(elev_array)
    plot2D(I)
"""
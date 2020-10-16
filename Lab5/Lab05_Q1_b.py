# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:53:51 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt

dow = np.loadtxt("dow.txt")

dow_fft = np.fft.rfft(dow)

dow_fft[len(dow_fft) // 10:] = 0 # Set all but top 10% of terms to 0

smoothed_dow10 = np.fft.irfft(dow_fft) # Get the inverse fourier transform of top 10% of terms

dow_fft[len(dow_fft) // 50:] = 0  # Set all but top 2% of terms to 0

smoothed_dow2 = np.fft.irfft(dow_fft) # Get the inverse transform with top 2% of terms

#This is the plotting code
plt.plot(range(len(dow)), dow, ":", label = "Dow Data")
plt.plot(range(len(smoothed_dow10)), smoothed_dow10, label = "Smoothed Dow (10%)")
plt.plot(range(len(smoothed_dow2)), smoothed_dow2, label = "Smoothed Dow (2%)")
plt.title("Dow from late 2006 to Dec 31 2010")
plt.xlabel("Days since late 2006")
plt.ylabel("Dow")
plt.legend()
plt.show()
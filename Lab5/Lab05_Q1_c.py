# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:41:33 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

dow = np.loadtxt("dow2.txt")

dow_fft = np.fft.rfft(dow)
dow_fft[len(dow_fft) // 50:] = 0  # Set all but top 2% of terms to 0
smoothed_dow = np.fft.irfft(dow_fft) # Get the inverse transform with top 2% of terms

dow_dct = fft.dct(dow)
dow_dct[len(dow_dct) // 50:] = 0
smoothed_dow2 = fft.idct(dow_dct)

#This is the plotting code
plt.plot(range(len(dow)), dow, ":", label = "Dow Data")
plt.plot(range(len(smoothed_dow)), smoothed_dow, label = "Smoothed Dow (FFT)")
plt.plot(range(len(smoothed_dow2)), smoothed_dow2, label = "Smoothed Dow (DCT)")
plt.title("Dow from 2004 to 2008")
plt.xlabel("Days since 2004")
plt.ylabel("Dow")
plt.legend()
plt.show()
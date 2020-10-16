# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 21:50:38 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt

sunspot_data = np.loadtxt("sunspots.txt")

plt.plot(sunspot_data[:, 0], sunspot_data[:, 1])
plt.xlabel("Months Since Jan 1749")
plt.ylabel("Number of Sunspots")
plt.title("Sunspot Observations")
plt.show()

sunspot_fft = np.fft.rfft(sunspot_data[: , 1])

plt.semilogx(range(len(sunspot_fft)), np.abs(sunspot_fft) ** 2)
plt.title("Fourier Transform of Sunspot Observations")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()

sunspot_zoom = sunspot_fft[20:30]

plt.plot(range(20, 30), np.abs(sunspot_zoom) ** 2)
plt.title("Fourier Transform of Sunspot Observations (Zoomed In)")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.show()
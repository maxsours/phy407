# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:48:56 2020
Anntara Khan (1002321891)
Max Sours(1003816579)
"""

#LAB  5 Q1(D)

import numpy as np
import matplotlib.pyplot as plt

piano = np.loadtxt("piano.txt", float)
trumpet = np.loadtxt("trumpet.txt", float)
d = 44100
#piano = np.array()
#trumpet = np.array()
#print(piano)

plt.plot (piano)
plt.title("piano note")
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.show()


plt.figure()
plt.plot (trumpet)
plt.title("trumpet note")
plt.xlabel(' (hz)')
plt.ylabel('amplitude')
plt.show ()

dft_piano = np.fft.fft(piano)
freq = np.fft.fftfreq(piano.shape[-1], 1/d)

plt.figure()
plt.plot(freq, ((abs(dft_piano))**2))
plt.title("FFT piano freq")
plt.xlabel('frequency (hz)')
plt.ylabel('amplitude')
plt.xlim(0,2000)
#plt.ylim (0, 2)
plt.show() 

dft_trumpet = np.fft.fft(trumpet)
freq = np.fft.fftfreq(trumpet.shape[-1], 1/d)

plt.figure()
plt.plot(freq, (abs(dft_trumpet))**2)
plt.title("FFT trumpet freq")
plt.xlabel('frequency (hz)')
plt.ylabel('amplitude')
plt.xlim(0,2000)
plt.show() 
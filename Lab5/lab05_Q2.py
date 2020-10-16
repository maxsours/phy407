# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:21:41 2020

@author: annta
"""
import numpy as np
import matplotlib.pyplot as plt

#constants
sigma = 25
e = 1e-3

#Q2(A)

#loading the file into the program
blur = np.loadtxt("blur.txt", float)

#plots out the blurred image in grayscale, using density plot
plt.title("Blurred Image")
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(blur, cmap='gray')
plt.show()

#Q2(B)

#to create the same sized matrix as the blurred image data
x1, y1 = blur.shape

#pointspread function
pointspread_func = np.empty((x1, y1))
for i in range(x1):
    ip = i
    if (ip > (x1 / 2)):
        ip -= x1
    for j in range(y1):
        jp = j
        if (jp > (y1 / 2)):
            jp -= y1
        pointspread_func[i, j] = (np.exp(-(ip ** 2 + jp ** 2) / (2. * sigma ** 2)))

#plots the point spread fucntion
plt.figure()
plt.title("point spread function")
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(pointspread_func, cmap='gray')
plt.show()

#Q2(C)

#takes the 2 dimensional fourier transformation of the blurred image and the point spread function
fft_image = np.fft.rfft2(blur)
fft_psf = np.fft.rfft2(pointspread_func)

#size of the fourier transformed matrix
x2, y2 = fft_image.shape

#creating an empty matrix that would store the filtered data, when we divde the blurred image data with the gaussian function
i_div_g = np.zeros((x2, y2), dtype = np.complex_)

#creating the actual filtered data matrix
for i in range(x2):
    for j in range(y2):
        if np.abs(fft_psf[i, j]) <= e:
            i_div_g[i, j] = fft_image[i, j] / (x2 * y2)
        else:
            i_div_g[i, j] = fft_image[i, j] / (fft_psf[i, j] * x2 * y2)

#reverse fourier transform to get the image back
image_unblurred = np.fft.irfft2(i_div_g)

#plotting the image
plt.figure()
plt.title("Unblurred Image")
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(image_unblurred, cmap='gray')
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:59:20 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt
from dcst import dct, idct, dst, idst, dst2, idst2

# part (b)

def dsct2(f):
    """ Takes DST along x, then DCT along y
    IN: f, the input 2D numpy array
    OUT: b, the 2D transformed array """
    M = f.shape[0] # Number of rows
    N = f.shape[1] # Number of columns
    a = np.zeros((M, N)) # Intermediate array
    b = np.zeros((M, N))# Final array
    # Take transform along x
    for j in range(N):
        a[:, j] = dst(f[:, j])
    # Take transform along y
    for i in range(M):
        b[i, :] = dct(a[i, :])
    return b

def idsct2(b):
    """ Takes iDCT along y, then iDST along x
    IN: b, the input 2D numpy array
    OUT: f, the 2D inverse-transformed array """
    M = b.shape[0] # Number of rows
    N = b.shape[1] # Number of columns
    a = np.zeros((M, N)) # Intermediate array
    f = np.zeros((M, N)) # Final array
    # Take inverse transform along y
    for i in range(M):
        a[i, :] = idct(b[i, :])
    # Take inverse transform along x
    for j in range(N):
        f[:, j] = idst(a[:, j])
    return f

def dcst2(f):
    """ Takes DCT along x, then DST along y
    IN: f, the input 2D numpy array
    OUT: b, the 2D transformed array """
    M = f.shape[0] # Number of rows
    N = f.shape[1] # Number of columns
    a = np.zeros((M, N)) # Intermediate array
    b = np.zeros((M, N))# Final array
    # Take transform along x
    for j in range(N):
        a[:, j] = dct(f[:, j])
    # Take transform along y
    for i in range(M):
        b[i, :] = dst(a[i, :])
    return b

def idcst2(b):
    """ Takes iDST along y, then iDCT along x
    IN: b, the input 2D numpy array
    OUT: f, the 2D inverse-transformed array """
    M = b.shape[0] # Number of rows
    N = b.shape[1] # Number of columns
    a = np.zeros((M, N)) # Intermediate array
    f = np.zeros((M, N)) # Final array
    # Take inverse transform along y
    for i in range(M):
        a[i, :] = idst(b[i, :])
    # Take inverse transform along x
    for j in range(N):
        f[:, j] = idct(a[:, j])
    return f

# part (c)

def EMfield(omega):
    """
    Calculate electromagnetic field over time with driving frequency
    omega. Return traces H_x(x=0.5, y=0), H_y(x=0, y=0.5), and
    E_z(x=0.5, y=0.5)

    Parameters
    ----------
    omega : float
        driving frequency

    Returns
    -------
    1xN float array
        H_x(x=0.5, y=0)
        
    1xN float array
        H_y(x=0, y=0.5)
        
    1xN float array
        E_z(x=0.5, y=0.5)

    """
    dt = 0.01 # define constants
    N = 2000
    Lx = 1
    Ly = 1
    J0 = 1
    m = 1
    n = 1
    c = 1
    P = 32
    Dx = np.pi * c * dt / (2 * Lx)
    Dy = np.pi * c * dt / (2 * Ly)
    
    # define arrays
    Xp = np.linspace(0, Lx, P + 1)
    Yp = np.linspace(0, Ly, P + 1)
    x, y = np.meshgrid(Xp, Yp) #xvals, yvals to calculate J
    p, q = np.meshgrid(np.arange(P + 1), np.arange(P + 1))
    Hx = np.zeros((P + 1, P + 1)) # initially set these 3 to 0
    Hy = np.zeros((P + 1, P + 1))
    Ez = np.zeros((P + 1, P + 1))
    Jz = np.zeros((P + 1, P + 1))
    Hx_trace = np.zeros(N) # these 3 will be returned
    Hy_trace = np.zeros(N)
    E_trace = np.zeros(N)
    
    for i in range(N):
        t = i * dt
        X = dsct2(Hx)
        Y = dcst2(Hy)
        E = dst2(Ez)
        J = dst2(Jz)
        pDx = p * Dx
        qDy = q * Dy
        
        E_new = ((1 - pDx ** 2 - qDy ** 2) * E + 2*qDy*X + 2*pDx*Y + dt*J) / (1 + (pDx)**2 + (qDy)**2)
        X_new = X - qDy * (E_new + E)
        Y_new = Y - pDx * (E_new + E)
        
        Ez = idst2(E_new)
        Hx = idsct2(X_new)
        Hy = idcst2(Y_new)
        Jz = J0 * np.sin(m * np.pi * x / Lx) * np.sin(n * np.pi * y / Ly) * np.sin(omega * t)
        E_trace[i] = Ez[P // 2, P // 2]
        Hx_trace[i] = Hx[P // 2, 0]
        Hy_trace[i] = Hy[0, P // 2]
        
    
    return Hx_trace, Hy_trace, E_trace
    

if __name__ == "__main__":
    load_vals = False
    Hx, Hy, E = EMfield(3.75)
    t = np.arange(0, 20, 0.01)
    plt.plot(t, Hx, "--", label = "Hx")
    plt.plot(t, Hy, ":", label = "Hy")
    plt.plot(t, E, "-", label = "Ez")
    plt.title("Sample traces with omega = 3.75")
    plt.xlabel("Time")
    plt.ylabel("Field intensity")
    plt.legend()
    plt.show()
    # part (d)
    L = 100
    Omega = np.linspace(0, 9, L)
    maxE = np.zeros(L)
    for i in range(L):
        _, _, E = EMfield(Omega[i])
        maxE[i] = np.max(np.abs(E))
    plt.plot(Omega, maxE)
    np.savez("MaxE", maxE=maxE)
    plt.title("Max E as a function of omega")
    plt.xlabel("Driving frequency")
    plt.ylabel("Max Amplitude of E")
    plt.show()
    
    # part (e)
    omega11 = np.pi * np.sqrt(2)
    Hx, Hy, E = EMfield(omega11)
    plt.plot(t, Hx, "--", label = "Hx")
    plt.plot(t, Hy, ":", label = "Hy")
    plt.plot(t, E, "-", label = "Ez")
    plt.title("Traces with omega = omega^{1,1}")
    plt.xlabel("Time")
    plt.ylabel("Field Intensity")
    plt.legend()
    plt.show()
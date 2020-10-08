# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:53:16 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import scipy.linalg as scil
from time import time
import matplotlib.pyplot as plt
import SolveLinear


def solve_LU(A, v):
    """
    Solve Ax = v for x by using LU decomposition.
    """
    P, L, U = scil.lu(A)
    return np.linalg.inv(U) @ np.linalg.inv(L) @ np.linalg.inv(P) @ v

def time_matmul(N):
    """
    Time three different types of matrix multiplication: 
    gaussian elimation, partial pivoting, and LU factorization
    and return the time each of them took.
    """
    A = np.random.rand(N, N)
    v = np.random.rand(N)
    # This is a list of functions that all take an NxN matrix A
    # and a Nx1 vector v as arguments, and return an Nx1 vector x
    # such that Ax = v
    functions = [SolveLinear.GaussElim, SolveLinear.PartialPivot, solve_LU]
    times = []
    err = 1e-3
    # Iterate through the three functions, time each one, and
    # make sure they actually compute close to the right value
    for f in functions:
        start = time()
        x = f(A, v)
        assert(np.linalg.norm(v - np.dot(A, x)) < err)
        end = time()
        times.append(end - start)
    return times[0], times[1], times[2]

if __name__ == "__main__":
    # Initialize arrays and lists for data storage
    N = np.arange(5, 400, 5)
    gausselim_times = []
    partialpivot_times = []
    lu_times = []
    for n in N:
        # Calculate time and then store each time in the correct list
        gausselim_time, partialpivot_time, lu_time = time_matmul(n)
        gausselim_times.append(gausselim_time)
        partialpivot_times.append(partialpivot_time)
        lu_times.append(lu_time)
    # Plot the data
    plt.title("Solving Linear Equations Using Different Methods")
    plt.xlabel("N")
    plt.ylabel("Time (sec)")
    plt.loglog(N, gausselim_times, label="Gaussian Elimination")
    plt.loglog(N, partialpivot_times, label = "Partial Pivoting")
    plt.loglog(N, lu_times, label = "LU Factorization")
    plt.legend()
    plt.show()
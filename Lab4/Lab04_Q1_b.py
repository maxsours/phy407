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
    and return the time each of them took and the error of
    each method.
    """
    A = np.random.rand(N, N)
    v = np.random.rand(N)
    # This is a list of functions that all take an NxN matrix A
    # and a Nx1 vector v as arguments, and return an Nx1 vector x
    # such that Ax = v
    functions = [SolveLinear.GaussElim, SolveLinear.PartialPivot, solve_LU]
    times = []
    errors = []
    # Iterate through the three functions, time each one, and
    # make sure they actually compute close to the right value
    for f in functions:
        start = time()
        x = f(A, v)
        end = time()
        errors.append(np.linalg.norm(v - np.dot(A, x)))
        times.append(end - start)
    return times, errors

if __name__ == "__main__":
    # Initialize arrays for data storage
    N = np.arange(5, 400, 5)
    times = np.zeros((3, (400 - 5) // 5)) #row 0 for gausselim, row 1 for partialpivot, row 2 for lu
    errors = np.zeros(np.shape(times))
    for i in range(len(N)):
        # Calculate times and errors and then store each in their correct array
        t, e = time_matmul(N[i])
        times[:, i] = t
        errors[:, i] = e
    print("Average Errors:")
    print("Gaussian Eliminaiton:", np.mean(errors[0, :]))
    print("Partial Pivots:", np.mean(errors[1, :]))
    print("Lu Factorization:", np.mean(errors[2, :]))
    # Plot the data
    plt.title("Solving Linear Equations Using Different Methods")
    plt.xlabel("N")
    plt.ylabel("Time (sec)")
    plt.loglog(N, times[0, :], label="Gaussian Elimination")
    plt.loglog(N, times[1, :], label = "Partial Pivoting")
    plt.loglog(N, times[2, :], label = "LU Factorization")
    plt.legend()
    plt.show()
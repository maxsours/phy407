# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:53:16 2020

@author: Max Sours, Anntara Khan
"""
import numpy as np
import matplotlib.pyplot as plt
import SolveLinear

#Define constants
Rodd = 1000
Reven = 2000
C1 = 1e-6
C2 = 0.5 * 1e-6
xp = 3
omega = 1000

# Determine coefficients of matrix and vector
A = np.array([[1/Rodd + 1/Reven + (1j) * omega * C1, -1j * omega * C1, 0], 
              [-1j * omega * C1, 1/Reven + 1/Rodd + 1j * omega * C1 + 1j * omega * C2, -1j * omega * C2],
              [0, -1j * omega * C2, 1/Reven + 1/Rodd + 1j * omega * C2]])
v =  np.array([1/Rodd + 0j, 1/Reven + 0j, 1/Rodd + 0j]) * xp

x = SolveLinear.PartialPivot(A, v)

print("First Configuration:")

for i in range(len(x)):
    # Print output
    print("V"+str(i+1)+" amplitude:", np.abs(x[i]))
    print("V"+str(i+1)+" phase (deg):", np.angle(x[i]) * 180 / np.pi)
    print("")

t = np.linspace(0, 4e-3 * np.pi, 200)
oscillation = np.exp(1j * omega * t)
#Plot for first configuration
plt.plot(t, (x[0] * oscillation).real, label = "V1")
plt.plot(t, (x[1] * oscillation).real, label = "V2")
plt.plot(t, (x[2] * oscillation).real, label = "V3")
plt.title("Voltage Oscillations for First Configuration")
plt.xlabel("Time (sec)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.show()

# Now simulate the second configuration, redefining A and going
# through the same steps as before.
print("\nSecond Configuration:")

# Determine coefficients of matrix and vector
A = np.array([[1/Rodd + 1/Reven + (1j) * omega * C1, -1j * omega * C1, 0], 
              [-1j * omega * C1, 1/Reven + 1/Rodd + 1j * omega * C1 + 1j * omega * C2, -1j * omega * C2],
              [0, -1j * omega * C2, 1/(1j * Reven) + 1/Rodd + 1j * omega * C2]])

x = SolveLinear.PartialPivot(A, v)

for i in range(len(x)):
    # Print output
    print("V"+str(i+1)+" amplitude:", np.abs(x[i]))
    print("V"+str(i+1)+" phase (deg):", np.angle(x[i]) * 180 / np.pi)
    print("")

t = np.linspace(0, 4e-3 * np.pi, 200)
oscillation = np.exp(1j * omega * t)
#Plot for first configuration
plt.plot(t, (x[0] * oscillation).real, label = "V1")
plt.plot(t, (x[1] * oscillation).real, label = "V2")
plt.plot(t, (x[2] * oscillation).real, label = "V3")
plt.title("Voltage Oscillations for Second Configuration")
plt.xlabel("Time (sec)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.show()

from scipy.linalg import solve_banded
import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 9.109e-31  # electron mass
L = 10e-8  # m
x0 = L / 3
sigma = L / 25  # m
k = 500 / L  # 1/m
h_bar = 6.626e-34
N = 3000  #time step in seconds  
P = 1024  # number of spatial slices
a = L / P  # spatial distance between points
h = 1e-18  # time segments tao
V_0 = 6e-17
x_1 = L / 4

# defining the function for psi from eq 20 to use in eq 3 where psi0 = 1/sqrt(psi)
def intpsy(x):
    return (np.exp((-(x - x0) ** 2 / (2 * sigma ** 2)) + (1j * k * x)))
# integrate using scipy integrate
int_psi = scipy.integrate.quad(intpsy, -L/2, L/2)
# int_psi will retunr two values, only using the first one as the seond is the absolute error and unecessary in this case

# rearranging eq 3 we get psi0
psi0 = 1 / np.sqrt(int_psi[0])


def psi_0(x):
    return (psi0*(np.exp((-(x - x0) ** 2 / (2 * sigma ** 2)) + (1j * k * x))))

# initial conditions
x_points = np.linspace(0, L, P - 1)
psi = np.array(list(map(psi_0, x_points)), complex)


# Create the matrix A and B, from eq 14, lab manual.
A = -(h_bar ** 2) / (2 * m * a ** 2)
B = []
V = 0
for i in range(P - 1):
    for j in np.arange(-5e-8, 5e-8):
        b1 = V * (i * a - L / 2) - 2 * A
        B.append(b1)
        V = V + (V_0 * (((j / x_1) ** 2) - 1) ** 2)
    
# to get the Hamiltonian matrix, eq 14, lab manual
D = np.diag(B, k = 0) # k = 0 means diagonal
Sup = A * np.eye(P - 1, k = 1) # PxP matrix, with ones on 1st super-diagonal
Sub = np.conj(A * np.eye(P - 1, k = -1)) # PxP matrix, with ones on 1st sub-diagonal
H = D + Sub + Sup

# define the identity matrix
I = np.identity(P - 1)
 
# define L and R from eq 17, lab manual
L_vec = I + 1j * (h / 2 * h_bar) * H
R = I - 1j * (h / 2 * h_bar) * H

# reformatted L_vec to be solved with solve_banded
L_vec_banded = np.zeros((3, L_vec.shape[0]))
L_vec_banded[0, 1:] = L_vec.diagonal(1)
L_vec_banded[1, :] = L_vec.diagonal()
L_vec_banded[2, :-1] = L_vec.diagonal(-1)


# Main loop
# store the wavefunction at each time step in a list
solution = [psi]
for i in range(N):
    x = np.matmul(R, psi)
    print (x.shape)
    psi = solve_banded((1, 1), L_vec_banded, x)
    solution.append(psi)

plt.plot(x_points, abs(solution[0]) ** 2)
plt.plot(x_points, abs(solution[150]) ** 2)
plt.plot(x_points, abs(solution[300]) ** 2)
plt.xlabel("x (m)")
plt.ylabel("$\psi(x)$")
plt.show()
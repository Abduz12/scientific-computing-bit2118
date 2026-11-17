# Task 8 (related case): Temperature along a metal rod with 10 interior points
# (left end held at 80 C, right end held at 30 C)
import numpy as np
import matplotlib.pyplot as plt

n = 10
A = 2 * np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n)
b[0] = 80.0      # left boundary temperature
b[-1] = 30.0     # right boundary temperature

def jacobi(A, b, tol=1e-8, max_iter=5000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=5000):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))
print("Direct solution:", np.round(x_exact, 3))
print("Max difference, Jacobi vs direct:", np.max(np.abs(x_j - x_exact)))

positions = np.arange(1, n + 1)
plt.plot(positions, x_exact, marker="o", label="Direct solution")
plt.plot(positions, x_j, linestyle="--", label="Jacobi")
plt.plot(positions, x_gs, linestyle=":", label="Gauss-Seidel")
plt.xlabel("Position along the rod (grid point)")
plt.ylabel("Temperature (C)")
plt.title("Steady temperature along a rod")
plt.legend()
plt.grid(True)
plt.show()

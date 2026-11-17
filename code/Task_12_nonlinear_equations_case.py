# Task 12 (related case): Where a thrown ball's path meets a sloping hillside
import numpy as np
from scipy.optimize import root

# Path of the ball:  y = x - 0.05*x^2   (x = distance, y = height, in metres)
# Hillside:          y = 0.3*x + 2

def equations(z):
    x, y = z
    return [
        y - (x - 0.05 * x**2),
        y - (0.3 * x + 2.0)
    ]

for guess in ([3.0, 3.0], [11.0, 5.0]):
    solution = root(equations, guess)
    x, y = solution.x
    print("Initial guess:", guess)
    print(f"Intersection: x = {x:.4f} m, y = {y:.4f} m")
    print("Largest residual:", np.max(np.abs(equations(solution.x))))
    print("Converged:", solution.success)
    print()

# Task 6 (related case): Mesh currents in a two-loop electrical circuit (Kirchhoff's voltage law)
import numpy as np

# Loop 1: 12 V source, 10 ohm resistor, 5 ohm resistor shared with loop 2
#         10*i1 + 5*(i1 - i2) = 12   ->   15*i1 - 5*i2 = 12
# Loop 2: 6 V source, 20 ohm resistor, same shared 5 ohm resistor
#         5*(i2 - i1) + 20*i2 = 6    ->   -5*i1 + 25*i2 = 6

A = np.array([
    [15.0, -5.0],
    [-5.0, 25.0]
])
b = np.array([12.0, 6.0])

currents = np.linalg.solve(A, b)
residual = b - A @ currents

print(f"Loop 1 current i1: {currents[0]:.4f} A")
print(f"Loop 2 current i2: {currents[1]:.4f} A")
print(f"Current through shared 5 ohm resistor: {currents[0] - currents[1]:.4f} A")
print("Verification A @ currents:", A @ currents)
print("Residual norm:", np.linalg.norm(residual))

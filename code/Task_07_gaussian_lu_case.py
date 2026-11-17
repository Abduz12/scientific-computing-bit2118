# Task 7 (related case): Steady room temperatures in a three-room building, solved for
# three different outside temperatures with one LU factorisation
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Room 1 and room 3 have an outside wall (coupling 2); room 2 is in the middle.
#   3*T1 - T2        = 2*T_out + heat1
#  -T1 + 2*T2 - T3   =           heat2
#        -T2 + 3*T3  = 2*T_out + heat3
A = np.array([
    [ 3.0, -1.0,  0.0],
    [-1.0,  2.0, -1.0],
    [ 0.0, -1.0,  3.0]
])
heating = np.array([4.0, 0.0, 2.0])      # heat input expressed in degrees of warming

lu, piv = lu_factor(A)                    # factor once

for name, t_out in [("Morning", 15.0), ("Afternoon", 24.0), ("Night", 12.0)]:
    b = np.array([2 * t_out, 0.0, 2 * t_out]) + heating
    T = lu_solve((lu, piv), b)
    residual = np.linalg.norm(b - A @ T)
    print(f"{name} (outside {t_out:.0f} C): "
          f"room temperatures = {np.round(T, 2)}, residual = {residual:.1e}")

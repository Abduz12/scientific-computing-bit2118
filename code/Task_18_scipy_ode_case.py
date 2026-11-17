# Task 18 (related case): Capacitor discharging through a resistor
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# dV/dt = -V / (R*C)
R = 2200.0        # ohms
C = 0.0047        # farads
V0 = 9.0          # initial voltage (V)
tau = R * C       # time constant (s)

def discharge(t, V):
    return [-V[0] / (R * C)]

t_eval = np.linspace(0, 40, 801)
solution = solve_ivp(discharge, (0, 40), [V0], t_eval=t_eval, rtol=1e-9, atol=1e-11)

exact = V0 * np.exp(-solution.t / tau)
voltage = solution.y[0]

v_at_tau = np.interp(tau, solution.t, voltage)
below_one = solution.t[np.argmax(voltage < 1.0)]
exact_below_one = tau * np.log(V0 / 1.0)

print("Solver success:", solution.success)
print(f"Time constant RC: {tau:.2f} s")
print(f"Voltage at t = RC: {v_at_tau:.3f} V ({v_at_tau / V0:.1%} of the starting voltage)")
print(f"Voltage at 20 s: {np.interp(20, solution.t, voltage):.3f} V")
print(f"Voltage first below 1 V at about t = {below_one:.2f} s (exact {exact_below_one:.2f} s)")
print(f"Maximum error against exact solution: {np.max(np.abs(voltage - exact)):.3e} V")

plt.plot(solution.t, voltage, label="solve_ivp")
plt.plot(solution.t, exact, linestyle="--", label="Exact")
plt.axvline(tau, linestyle=":", linewidth=0.8, label="t = RC")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("Capacitor discharging")
plt.legend()
plt.grid(True)
plt.show()

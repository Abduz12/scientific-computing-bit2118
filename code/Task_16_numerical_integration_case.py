# Task 16 (related case): Distance travelled by a bus from speed readings
import numpy as np
from scipy.integrate import simpson

# np.trapezoid exists in NumPy 2.0+; older NumPy calls it np.trapz
trapezoid = getattr(np, "trapezoid", None) or np.trapz

time_min = np.array([0, 10, 20, 30, 40, 50, 60], dtype=float)
speed_kmh = np.array([0.0, 30.0, 45.0, 50.0, 40.0, 25.0, 0.0])

time_hours = time_min / 60.0            # integrate speed (km/h) over time (h) -> km

distance_trapezoid = trapezoid(speed_kmh, time_hours)
distance_simpson = simpson(speed_kmh, x=time_hours)

print(f"Distance using trapezoidal rule: {distance_trapezoid:.3f} km")
print(f"Distance using Simpson's rule: {distance_simpson:.3f} km")
print(f"Difference between estimates: {abs(distance_simpson - distance_trapezoid):.3f} km")
print(f"Average speed over the hour: {distance_simpson / 1.0:.2f} km/h")

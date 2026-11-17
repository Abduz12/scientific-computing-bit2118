# Task 13 (related case): River water level recorded every 3 hours
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24], dtype=float)
level_m = np.array([1.20, 1.15, 1.10, 1.35, 1.80, 1.65, 1.40, 1.25, 1.20])

linear = interp1d(hours, level_m, kind="linear")
cubic = CubicSpline(hours, level_m)

# Estimates every 15 minutes
times = np.linspace(0, 24, 97)

target = 7.5   # 07:30
print(f"Linear estimate at 07:30: {float(linear(target)):.3f} m")
print(f"Cubic estimate at 07:30: {float(cubic(target)):.3f} m")
print(f"Highest estimated level (cubic): {cubic(times).max():.3f} m "
      f"at hour {times[cubic(times).argmax()]:.2f}")

plt.scatter(hours, level_m, label="3-hourly readings")
plt.plot(times, linear(times), label="Linear")
plt.plot(times, cubic(times), label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Water level (m)")
plt.title("River water level interpolation")
plt.legend()
plt.grid(True)
plt.show()

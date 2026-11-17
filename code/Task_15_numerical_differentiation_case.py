# Task 15 (related case): Acceleration of a cyclist from speed readings
import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)         # seconds
speed = np.array([0.0, 1.8, 3.5, 5.1, 6.4, 7.4, 8.1])       # metres per second

acceleration = np.zeros_like(speed)

# Forward difference at the start
acceleration[0] = (speed[1] - speed[0]) / (time[1] - time[0])

# Central differences for interior points
for i in range(1, len(time) - 1):
    acceleration[i] = (speed[i + 1] - speed[i - 1]) / (time[i + 1] - time[i - 1])

# Backward difference at the end
acceleration[-1] = (speed[-1] - speed[-2]) / (time[-1] - time[-2])

for t, v, a in zip(time, speed, acceleration):
    print(f"t={t:.0f}s, speed={v:.1f}m/s, estimated acceleration={a:.2f}m/s^2")

plt.plot(time, acceleration, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated acceleration (m/s^2)")
plt.title("Cyclist acceleration from speed data")
plt.grid(True)
plt.show()

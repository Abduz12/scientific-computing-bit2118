# Task 17 (related case): A cup of tea cooling in a room
import numpy as np
import matplotlib.pyplot as plt

T_ambient = 22.0      # room temperature (C)
T_initial = 85.0      # tea temperature when poured (C)
k = 0.08              # cooling constant per minute (assumed)
h = 0.5               # step size (minutes)
end_time = 20.0
drinkable = 60.0      # temperature at which the tea is comfortable to drink (C)

def cooling_rate(T):
    return -k * (T - T_ambient)

time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + h * cooling_rate(temperature[i])

exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

first_below = time[np.argmax(temperature <= drinkable)]
exact_time = -np.log((drinkable - T_ambient) / (T_initial - T_ambient)) / k

print(f"Euler temperature after {end_time:.0f} min: {temperature[-1]:.2f} C")
print(f"Exact temperature after {end_time:.0f} min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1] - exact[-1]):.4f} C")
print(f"Euler: tea first at or below {drinkable:.0f} C at t = {first_below:.1f} min")
print(f"Exact: tea reaches {drinkable:.0f} C at t = {exact_time:.2f} min")

plt.plot(time, temperature, marker="o", markersize=3, label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.axhline(drinkable, linestyle="--", linewidth=0.8, label="Drinkable (60 C)")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a cup of tea")
plt.legend()
plt.grid(True)
plt.show()

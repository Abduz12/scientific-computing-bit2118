# Task 14 (related case): Monthly sales growth and a short forecast
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

months = np.arange(1, 9, dtype=float)
sales = np.array([120, 135, 150, 172, 190, 215, 240, 270], dtype=float)

# Exponential growth model: sales = a * exp(b * month)
def model(x, a, b):
    return a * np.exp(b * x)

parameters, covariance = curve_fit(model, months, sales, p0=[100, 0.1])
a, b = parameters

predicted = model(months, a, b)
rmse = np.sqrt(np.mean((sales - predicted) ** 2))

print(f"Fitted model: sales = {a:.2f} * exp({b:.4f} * month)")
print(f"Monthly growth rate: {np.exp(b) - 1:.2%}")
print(f"RMSE: {rmse:.2f} units")
print(f"Forecast for month 9: {model(9, a, b):.1f} units")
print(f"Forecast for month 10: {model(10, a, b):.1f} units")

x_plot = np.linspace(1, 10, 200)
plt.scatter(months, sales, label="Recorded sales")
plt.plot(x_plot, model(x_plot, a, b), label="Fitted growth curve")
plt.xlabel("Month")
plt.ylabel("Units sold")
plt.title("Monthly sales growth and forecast")
plt.legend()
plt.grid(True)
plt.show()

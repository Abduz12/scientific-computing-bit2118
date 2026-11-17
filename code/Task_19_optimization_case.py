# Task 19 (related case): Cheapest mix of two foods that meets protein and energy needs
import numpy as np
from scipy.optimize import minimize

# x = servings of beans, y = servings of rice per day
# Cost per serving (KSh):  beans = 15, rice = 10
# Protein per serving (g): beans = 9,  rice = 3    -> need at least 45 g
# Energy per serving (kcal): beans = 130, rice = 200 -> need at least 1200 kcal

def cost(z):
    x, y = z
    return 15 * x + 10 * y

constraints = [
    {"type": "ineq", "fun": lambda z: 9 * z[0] + 3 * z[1] - 45},
    {"type": "ineq", "fun": lambda z: 130 * z[0] + 200 * z[1] - 1200},
]
bounds = [(0, None), (0, None)]

solution = minimize(cost, x0=[5, 5], method="SLSQP", bounds=bounds, constraints=constraints)
x, y = solution.x

print("Optimization success:", solution.success)
print(f"Beans servings: {x:.3f}")
print(f"Rice servings: {y:.3f}")
print(f"Protein: {9 * x + 3 * y:.1f} g, energy: {130 * x + 200 * y:.1f} kcal")
print(f"Minimum daily cost: KSh {solution.fun:.2f}")

# Whole servings only
best = None
for a in range(0, 21):
    for b in range(0, 21):
        if 9 * a + 3 * b >= 45 and 130 * a + 200 * b >= 1200:
            c = 15 * a + 10 * b
            if best is None or c < best[0]:
                best = (c, a, b)
print("Best whole-serving plan (cost, beans, rice):", best)

# Task 10 (related case): Break-even quantity of a small business
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

price = 40.0       # selling price per unit (KSh)
fixed = 1500.0     # fixed costs (KSh)
variable = 10.0    # variable cost per unit (KSh)
crowding = 0.02    # extra cost that grows with q^2 (overtime, congestion)

def profit(q):
    revenue = price * q
    cost = fixed + variable * q + crowding * q**2
    return revenue - cost

# Bisection on a bracket where profit changes sign
solution = root_scalar(profit, bracket=[10, 200], method="bisect", xtol=1e-10)

# Fixed-point form: q = (fixed + crowding*q^2) / (price - variable)
def g(q):
    return (fixed + crowding * q**2) / (price - variable)

q = 100.0
history = [q]
for _ in range(100):
    q_new = g(q)
    history.append(q_new)
    if abs(q_new - q) < 1e-10:
        break
    q = q_new

print(f"Break-even quantity (bisection): {solution.root:.4f} units")
print(f"Break-even quantity (fixed point): {history[-1]:.4f} units")
print("Fixed-point iterations:", len(history) - 1)
print(f"Revenue at break-even: KSh {price * solution.root:.2f}")

quantities = np.linspace(0, 300, 400)
plt.plot(quantities, profit(quantities))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Units sold")
plt.ylabel("Profit (KSh)")
plt.title("Break-even point")
plt.grid(True)
plt.show()

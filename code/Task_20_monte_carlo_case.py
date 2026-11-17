# Task 20 (related case): Probability that a shop runs out of stock in a day
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

rng = np.random.default_rng(42)

stock = 25            # units in stock at the start of the day
mean_demand = 18      # average customers wanting the item per day
N = 100_000

# Daily demand is random with a Poisson distribution
demand = rng.poisson(mean_demand, N)
stockout = demand > stock

estimate = stockout.mean()
exact = poisson.sf(stock, mean_demand)       # exact probability for comparison

print(f"Estimated stock-out probability: {estimate:.4%}")
print(f"Exact probability (Poisson): {exact:.4%}")
print(f"Stock-out days: {stockout.sum()} out of {N}")

running = np.cumsum(stockout) / np.arange(1, N + 1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

plt.semilogx(indices + 1, running[indices], label="Simulation")
plt.axhline(exact, linestyle="--", linewidth=0.8, label="Exact value")
plt.xlabel("Number of simulated days")
plt.ylabel("Estimated stock-out probability")
plt.title("Monte Carlo estimate of stock-out risk")
plt.legend()
plt.grid(True)
plt.show()

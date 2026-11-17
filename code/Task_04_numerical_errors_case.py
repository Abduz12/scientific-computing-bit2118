# Task 4 (related case): Round-off in money calculations
import numpy as np

# Ten payments of 0.10 should add up to exactly 1.00
payments = [0.10] * 10
total = 0.0
for payment in payments:      # explicit loop: plain floating-point addition
    total += payment
print("Sum of ten 0.10 payments:", total)
print("Exact comparison with 1.0:", total == 1.0)
print("Tolerance comparison with 1.0:", np.isclose(total, 1.0))

# Working in whole cents avoids the problem
total_cents = sum([10] * 10)
print("Sum in cents:", total_cents, "-> shillings:", total_cents / 100)

# Compound interest: 1000 at 1% per month for 12 months
balance = 1000.0
for _ in range(12):
    balance = balance * 1.01
formula = 1000.0 * 1.01 ** 12

print(f"Balance by repeated multiplication: {balance:.10f}")
print(f"Balance by formula:                 {formula:.10f}")
print(f"Difference between the two methods: {abs(balance - formula):.3e}")

# Rounding the balance to cents introduces a (much larger) rounding error
rounded = round(balance, 2)
abs_err = abs(balance - rounded)
print(f"Rounded balance: {rounded:.2f}")
print(f"Absolute rounding error: {abs_err:.6f}")
print(f"Relative rounding error: {abs_err / balance:.6%}")

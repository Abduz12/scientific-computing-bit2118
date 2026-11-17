# Task 11 (related case): Effective yearly interest rate of a loan
from scipy.optimize import root_scalar

# The lender pays out 100,000 now and receives five yearly repayments of 30,000.
# The interest rate is the rate that makes the net present value zero.
cash_flows = [100000, -30000, -30000, -30000, -30000, -30000]

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)

print(f"Loan interest rate using Newton-Raphson: {newton.root:.4%}")
print(f"Loan interest rate using Secant method: {secant.root:.4%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")
print(f"Total repaid: {-sum(cash_flows[1:])}, total interest: {-sum(cash_flows)}")

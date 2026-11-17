# Task 11: Root Finding: Newton-Raphson and Secant Methods

**Program file:** [`code/Task_11_newton_secant.py`](../code/Task_11_newton_secant.py)

**Mathematical concept:** Newton-Raphson uses the tangent (needs the derivative); the secant method estimates the slope from two points.

## 1. Inputs and mathematical operation

**Inputs**

- `cash_flows`: -10,000 investment then four yearly inflows
- Newton start 0.10; secant starts 0.05 and 0.20

**Mathematical operation**

- Define NPV(rate) and its derivative
- Find the rate where NPV = 0 (the internal rate of return, IRR)
- Check NPV at the solution

## 2. Baseline output

```text
IRR using Newton-Raphson: 11.542461%
IRR using Secant method: 11.542461%
NPV at Newton solution: 0.000000
```

## 3. Change an input or parameter

**What I changed:** Changed the last cash inflow `2500` to `1000`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Last cash inflow | 2500 | 1000 | IRR 11.54% → 6.46% |

New output (last inflow 2500 -> 1000):

```text
IRR using Newton-Raphson: 6.458595%
IRR using Secant method: 6.458595%
NPV at Newton solution: -0.000000
```

**How and why the result changes:** Reducing the final inflow from 2500 to 1000 reduces the total return, so the rate that makes NPV zero falls from 11.54% to 6.46%. Newton-Raphson and the secant method still agree, and the NPV at the solution is zero. The IRR is lower because the investor gets less money back for the same 10,000 invested (total inflows 11,500 instead of 13,000).

## 4. Meaning of the output

The IRR of 11.542461% is the yearly rate at which the present value of the four inflows equals the 10,000 invested, so NPV is zero there. An investor can compare it with the cost of borrowing: if money costs less than about 11.5% per year, the project is worthwhile. Newton-Raphson (which uses the derivative) and the secant method (which uses two starting points) converge to the same value, and the NPV at the solution prints as 0.000000, confirming the root.

## 5. Related real-world case

- **Scenario:** A lender pays out KSh 100,000 and receives five yearly repayments of KSh 30,000. What yearly interest rate does the borrower effectively pay?
- **Assumptions:**
  - Repayments are made at the end of each year
  - The rate is constant over the five years
  - There are no fees or penalties
- **Input data:** cash_flows = [100000, −30000, −30000, −30000, −30000, −30000]; Newton starts at 0.10 and the secant method at 0.05 and 0.20.
- **Modified program:** [`code/Task_11_newton_secant_case.py`](../code/Task_11_newton_secant_case.py)

**Output:**

```text
Loan interest rate using Newton-Raphson: 15.2382%
Loan interest rate using Secant method: 15.2382%
NPV at Newton solution: 0.000000
Total repaid: 150000, total interest: 50000
```

**Interpretation:** The effective interest rate is 15.2382% per year, found by both Newton-Raphson and the secant method. The borrower repays 150,000 in total, so 50,000 is interest. That is 50% of the amount borrowed over five years, but only about 15.2% a year because the borrower repays gradually and does not keep the full 100,000 for the whole time. This is how effective rates can be compared across loans with different repayment schedules.

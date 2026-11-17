# Task 4: Floating-Point Arithmetic and Numerical Errors

**Program file:** [`code/Task_04_numerical_errors.py`](../code/Task_04_numerical_errors.py)

**Mathematical concept:** Computers store most real numbers approximately in binary, so results carry round-off error and exact equality tests can fail.

## 1. Inputs and mathematical operation

**Inputs**

- `0.1 + 0.2` compared with `0.3`
- `true_value = sqrt(2)` and `approx_value = 1.414`
- `x` values 1e-4, 1e-8 and 1e-12 for the stable and unstable formulas

**Mathematical operation**

- Exact comparison (`==`) versus tolerance comparison (`np.isclose`)
- Absolute error = |true - approx| and relative error = absolute error / |true|
- Compare (sqrt(1+x) - 1)/x with the algebraically equal 1/(sqrt(1+x) + 1)

## 2. Baseline output

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00021356
Relative error: 0.01510114%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
```

## 3. Change an input or parameter

**What I changed:** Changed `approx_value = 1.414` to `1.41421` and added `1e-16` to the list of `x` values.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| approx_value | 1.414 | 1.41421 | Absolute error 0.00021356 → 0.00000356; relative error 0.0151% → 0.000252% |
| x values | 1e-4, 1e-8, 1e-12 | added 1e-16 | Direct formula gives 0.000000000000 (wrong); stable formula gives 0.500000000000 |

New output (approx 1.414 -> 1.41421; add x=1e-16):

```text
0.1 + 0.2 = 0.30000000000000004
Exact comparison: False
Tolerance-based comparison: True
Absolute error: 0.00000356
Relative error: 0.00025190%
x=1e-04: direct=0.499987500624, stable=0.499987500625
x=1e-08: direct=0.499999996961, stable=0.499999998750
x=1e-12: direct=0.500044450291, stable=0.500000000000
x=1e-16: direct=0.000000000000, stable=0.500000000000
```

**How and why the result changes:** A closer approximation of the square root of 2 reduced the absolute error from about 0.000214 to about 0.0000036 and the relative error from 0.0151% to 0.00025%, so more correct digits give a smaller error. The second change shows round-off. For x = 1e-16, the number 1 + x is stored as exactly 1.0, so sqrt(1 + x) − 1 becomes 0 and the direct formula returns 0 instead of about 0.5. The stable formula 1 / (sqrt(1 + x) + 1) has no subtraction of nearly equal numbers, so it still returns 0.5. The direct formula was already losing accuracy at 1e-8 (0.49999999696) and 1e-12 (0.50004445), so its error grows as x gets smaller.

## 4. Meaning of the output

`0.1 + 0.2` prints 0.30000000000000004, so the exact comparison with 0.3 is False, but `np.isclose` says True because it accepts a very small difference. Computers store 0.1 and 0.2 in binary and cannot represent them exactly. The second block shows that approximating the square root of 2 by 1.414 gives an absolute error of 0.00021356 and a relative error of 0.0151%. The last block compares two formulas that are equal in mathematics (the true value tends to 0.5) but behave differently on a computer. For small x the direct formula subtracts two almost equal numbers and loses digits, while the rewritten stable formula keeps its accuracy. The lessons are to use a tolerance when comparing floating-point numbers and to choose numerically stable formulas.

## 5. Related real-world case

- **Scenario:** Money calculations: adding ten payments of KSh 0.10 and computing 12 months of compound interest on KSh 1000 at 1% per month.
- **Assumptions:**
  - Payments and balances are stored as floating-point numbers
  - The payments are added with an explicit loop so that every Python version gives the same result
  - Interest is 1% per month, compounded monthly, and rounded to cents only at the end
- **Input data:** `payments = [0.10] * 10` and an opening balance of 1000.0.
- **Modified program:** [`code/Task_04_numerical_errors_case.py`](../code/Task_04_numerical_errors_case.py)

**Output:**

```text
Sum of ten 0.10 payments: 0.9999999999999999
Exact comparison with 1.0: False
Tolerance comparison with 1.0: True
Sum in cents: 100 -> shillings: 1.0
Balance by repeated multiplication: 1126.8250301320
Balance by formula:                 1126.8250301320
Difference between the two methods: 0.000e+00
Rounded balance: 1126.83
Absolute rounding error: 0.004970
Relative rounding error: 0.000441%
```

**Interpretation:** Adding 0.10 ten times gives 0.9999999999999999, not 1.0, so the exact comparison fails but `np.isclose` passes. Adding the same amounts in whole cents (10 cents ten times) gives exactly 100 cents, so using integers for money removes the problem. The compound-interest balance is KSh 1126.83 when rounded. Repeated multiplication and the formula agree to about 12 digits, while rounding to cents introduces an absolute error of 0.00497, a relative error of 0.00044%. Round-off is tiny in one calculation, but in banking, where millions of transactions are added, it can accumulate, so systems store money in cents or compare with a tolerance.

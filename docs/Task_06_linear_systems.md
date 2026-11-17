# Task 6: Solution of Systems of Linear Equations

**Program file:** [`code/Task_06_linear_systems.py`](../code/Task_06_linear_systems.py)

**Mathematical concept:** A system Ax = b has coefficient matrix A, unknown vector x and known results b; solving it finds the x that reproduces b.

## 1. Inputs and mathematical operation

**Inputs**

- `A`: CPU and memory used per server of each type
- `b`: total CPU (20) and memory (72) observed

**Mathematical operation**

- Solve Ax = b with `np.linalg.solve`
- Verify with `A @ solution` and the residual b - Ax

## 2. Baseline output

```text
Type A servers: 3
Type B servers: 4
Verification A @ solution: [20. 72.]
Residual: [0. 0.]
Residual norm: 0.0
```

## 3. Change an input or parameter

**What I changed:** Changed `b = np.array([20.0, 72.0])` to `b = np.array([26.0, 76.0])`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Totals b (CPU, memory) | [20, 72] | [26, 76] | Type A servers 3 → 5; Type B servers 4 → 3; residual still 0 |

New output (b [20, 72] -> [26, 76]):

```text
Type A servers: 5
Type B servers: 3
Verification A @ solution: [26. 76.]
Residual: [0. 0.]
Residual norm: 0.0
```

**How and why the result changes:** Changing the totals changes the right-hand side b, so the solution of Ax = b changes while the matrix A (CPU and memory per server) stays the same. Check: 4(5) + 2(3) = 26 CPU units and 8(5) + 12(3) = 76 GB. The residual is still zero, which confirms the new answer. A is invertible (determinant 4 x 12 − 2 x 8 = 32), so there is exactly one solution for every b, but a b that does not match whole servers would give fractions, which cannot be real servers.

## 4. Meaning of the output

The unknowns are the number of Type A servers (3) and Type B servers (4). Type A uses 4 CPU units and 8 GB, Type B uses 2 CPU units and 12 GB, and the observed totals were 20 CPU units and 72 GB: 3 x 4 + 4 x 2 = 20 and 3 x 8 + 4 x 12 = 72. `A @ solution` reproduces b exactly and the residual b − Ax is zero (norm 0.0), which proves that the solution fits both equations. A residual far from zero would mean the answer is wrong.

## 5. Related real-world case

- **Scenario:** Currents in a circuit with two loops that share a 5-ohm resistor: loop 1 has a 12 V source and a 10-ohm resistor, loop 2 has a 6 V source and a 20-ohm resistor.
- **Assumptions:**
  - Steady direct current with ideal sources and resistors
  - Both mesh currents i1 and i2 flow in the same (clockwise) direction
  - Kirchhoff's voltage law is applied to each loop
- **Input data:** A = [[15, −5], [−5, 25]] and b = [12, 6].
- **Modified program:** [`code/Task_06_linear_systems_case.py`](../code/Task_06_linear_systems_case.py)

**Output:**

```text
Loop 1 current i1: 0.9429 A
Loop 2 current i2: 0.4286 A
Current through shared 5 ohm resistor: 0.5143 A
Verification A @ currents: [12.  6.]
Residual norm: 8.881784197001252e-16
```

**Interpretation:** The solution is i1 = 0.9429 A and i2 = 0.4286 A. The current through the shared 5-ohm resistor is the difference i1 − i2 = 0.5143 A, in the direction of loop 1 because loop 1 has the stronger source. The residual norm is about 1e-15, so the currents satisfy both loop equations. Writing a circuit as Ax = b lets the same code handle circuits with many more loops.

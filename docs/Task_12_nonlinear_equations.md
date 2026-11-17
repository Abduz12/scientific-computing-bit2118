# Task 12: Polynomial and Nonlinear Equation Solving

**Program file:** [`code/Task_12_nonlinear_equations.py`](../code/Task_12_nonlinear_equations.py)

**Mathematical concept:** A nonlinear system needs a numerical solver that searches for values making every residual close to zero.

## 1. Inputs and mathematical operation

**Inputs**

- Circle x^2 + y^2 = 4
- Parabola y = x^2 - 1
- Initial guesses [1, 1] and [-1, 1]

**Mathematical operation**

- Write the two equations as residuals
- Solve with `scipy.optimize.root`
- Check the residuals and the `success` flag

## 2. Baseline output

```text
Initial guess: [1.0, 1.0]
Intersection: [1.51748991 1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.51748991  1.30277564]
Residuals: [np.float64(-2.4780177909633494e-13), np.float64(-2.4158453015843406e-13)]
Converged: True
```

## 3. Change an input or parameter

**What I changed:** Changed the circle equation `x**2 + y**2 - 4` to `x**2 + y**2 - 9`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Circle | x² + y² = 4 | x² + y² = 9 | Intersections (±1.517, 1.303) → (±1.836, 2.372) |

New output (circle x^2+y^2 = 4 -> 9):

```text
Initial guess: [1.0, 1.0]
Intersection: [1.83637723 2.37228132]
Residuals: [np.float64(-1.3891110484109959e-12), np.float64(1.4597212327771558e-12)]
Converged: True

Initial guess: [-1.0, 1.0]
Intersection: [-1.83637723  2.37228132]
Residuals: [np.float64(-1.3855583347321954e-12), np.float64(1.4601653219870059e-12)]
Converged: True
```

**How and why the result changes:** A larger circle (radius 3 instead of 2) crosses the same parabola at different points, further from the origin and higher up: (±1.836, 2.372). Both starting guesses still converged, with residuals of about 1e-12, so the solver found both intersections. The symmetric pair of solutions comes from the x² in the equations: if (x, y) is a solution then (−x, y) is too. Choosing a starting guess on each side of the y-axis let the solver find each one.

## 4. Meaning of the output

The circle x² + y² = 4 and the parabola y = x² − 1 intersect at two points, (1.517, 1.303) and (−1.517, 1.303). The guess [1, 1] converged to the right-hand point and [−1, 1] to the left-hand one. The residuals are about 1e-13, essentially zero, so both equations are satisfied, and `Converged: True` confirms that the solver succeeded. A nonlinear system can have several solutions, so the starting guess decides which one the solver finds.

## 5. Related real-world case

- **Scenario:** Where does the path of a thrown ball cross a sloping roof line? The ball follows y = x − 0.05x² and the roof edge is the line y = 0.3x + 2 (x is horizontal distance and y is height, both in metres).
- **Assumptions:**
  - No air resistance, so the path is a parabola
  - The roof edge is a straight line
  - The ball is thrown from the ground at x = 0, so it starts below the roof line
- **Input data:** Starting guesses [3, 3] and [11, 5].
- **Modified program:** [`code/Task_12_nonlinear_equations_case.py`](../code/Task_12_nonlinear_equations_case.py)

**Output:**

```text
Initial guess: [3.0, 3.0]
Intersection: x = 4.0000 m, y = 3.2000 m
Largest residual: 0.0
Converged: True

Initial guess: [11.0, 5.0]
Intersection: x = 10.0000 m, y = 5.0000 m
Largest residual: 0.0
Converged: True
```

**Interpretation:** The path and the roof line intersect at (4 m, 3.2 m) and (10 m, 5 m), with residuals of zero. The ball starts below the roof line, rises through it at x = 4 m, stays above it between x = 4 m and x = 10 m, and drops back below it at x = 10 m, which happens to be the highest point of the throw. So the ball clears a roof edge only for horizontal distances between 4 m and 10 m.

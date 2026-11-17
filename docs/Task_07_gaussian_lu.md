# Task 7: Gaussian Elimination and LU Decomposition

**Program file:** [`code/Task_07_gaussian_lu.py`](../code/Task_07_gaussian_lu.py)

**Mathematical concept:** LU decomposition factors A once into lower and upper triangular matrices so many different b vectors can be solved cheaply.

## 1. Inputs and mathematical operation

**Inputs**

- `A`: 3 x 3 coefficient matrix reused every time
- `measurement_sets`: three different b vectors

**Mathematical operation**

- Factor A once with `lu_factor`
- Solve each b with `lu_solve`
- Residual norm for each solution, and comparison with `np.linalg.solve`

## 2. Baseline output

```text
Measurement set 1
Solution: [5. 5. 5.]
Residual norm: 0.0

Measurement set 2
Solution: [5.31707317 5.26829268 4.75609756]
Residual norm: 1.7763568394002505e-15

Measurement set 3
Solution: [4.90243902 5.6097561  5.53658537]
Residual norm: 0.0

Direct solution for first set: [5. 5. 5.]
```

## 3. Change an input or parameter

**What I changed:** Changed the first row of `A` from `[4.0, -1.0, 0.0]` to `[6.0, -1.0, 0.0]`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| A[0][0] | 4.0 | 6.0 | First solution [5, 5, 5] → [3.254, 4.524, 4.841] |

New output (A[0][0] 4.0 -> 6.0):

```text
Measurement set 1
Solution: [3.25396825 4.52380952 4.84126984]
Residual norm: 3.552713678800501e-15

Measurement set 2
Solution: [3.46031746 4.76190476 4.58730159]
Residual norm: 0.0

Measurement set 3
Solution: [3.19047619 5.14285714 5.38095238]
Residual norm: 4.351167857633658e-15

Direct solution for first set: [3.25396825 4.52380952 4.84126984]
```

**How and why the result changes:** Changing one entry of A changes the model, so all the unknowns change, not only the first one. A larger diagonal entry makes the first equation more dominated by x1, so x1 falls from 5 to about 3.25, and the other unknowns shift because the equations are coupled. LU factorisation was still done once and reused for all three measurement sets. The residual norms remain around 1e-15 and the direct `np.linalg.solve` answer matches the LU answer, so the change affected the model but not the accuracy.

## 4. Meaning of the output

A is the fixed coefficient matrix of the model and each b is a new set of measurements. The program computes the factors once with `lu_factor` and then solves each case with `lu_solve`. For the first measurement set the answer is exactly [5, 5, 5]; check: 4(5) − 5 = 15, −5 + 4(5) − 5 = 10 and −5 + 3(5) = 10, which matches b. The other two sets give slightly different unknowns. Residual norms from 0 to 2e-15 show that every solution fits its equations, and the direct solution matches. Reusing the factorisation saves work when the same A is used with many b vectors.

## 5. Related real-world case

- **Scenario:** Steady temperatures of three rooms in a row (rooms 1 and 3 have an outside wall) for three outside temperatures: morning 15 C, afternoon 24 C and night 12 C. Heaters in rooms 1 and 3 give 4 and 2 degrees of warming.
- **Assumptions:**
  - Steady state: temperatures no longer change
  - Heat flows only between neighbouring rooms and through the outside walls (coupling 2 for each outside wall)
  - The heater effect is expressed as degrees of warming
  - The building (matrix A) does not change during the day
- **Input data:** A = [[3, −1, 0], [−1, 2, −1], [0, −1, 3]], heating = [4, 0, 2], outside temperatures 15, 24 and 12 C.
- **Modified program:** [`code/Task_07_gaussian_lu_case.py`](../code/Task_07_gaussian_lu_case.py)

**Output:**

```text
Morning (outside 15 C): room temperatures = [16.83 16.5  16.17], residual = 0.0e+00
Afternoon (outside 24 C): room temperatures = [25.83 25.5  25.17], residual = 0.0e+00
Night (outside 12 C): room temperatures = [13.83 13.5  13.17], residual = 0.0e+00
```

**Interpretation:** The room temperatures are about 16.8, 16.5 and 16.2 C when it is 15 C outside, 25.8, 25.5 and 25.2 C at 24 C, and 13.8, 13.5 and 13.2 C at 12 C. Each room is between about 1.2 and 1.8 degrees warmer than outside because of the heaters. Room 1 is warmest because it has the strongest heater and room 3 is the coolest. Every temperature moves by the same amount as the outside temperature (9 degrees from morning to afternoon), as expected in a model where the outside temperature only enters through the right-hand side. The matrix A was factorised once and reused for all three times.

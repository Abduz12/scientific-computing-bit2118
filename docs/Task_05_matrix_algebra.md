# Task 5: Matrix Algebra and Matrix Operations

**Program file:** [`code/Task_05_matrix_algebra.py`](../code/Task_05_matrix_algebra.py)

**Mathematical concept:** Matrices organise numbers in rows and columns; multiplying by a matrix can rotate, scale or otherwise transform every point consistently.

## 1. Inputs and mathematical operation

**Inputs**

- `points`: four corners of a unit square
- Rotation angle 45 degrees
- Scale factors 2.0 (x) and 1.5 (y)

**Mathematical operation**

- Build the rotation and scaling matrices
- Combine them: transformation = rotation @ scale
- Transform all points: points @ transformation.T
- Determinant of the transformation

## 2. Baseline output

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

## 3. Change an input or parameter

**What I changed:** Changed `np.deg2rad(45)` to `np.deg2rad(90)`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Rotation angle | 45 degrees | 90 degrees | Points turn by 90 degrees instead of 45; determinant stays 3.0 |

New output (angle 45 -> 90 degrees):

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.22464680e-16 -1.50000000e+00]
 [ 2.00000000e+00  9.18485099e-17]]
Transformed points:
 [[ 0.00000000e+00  0.00000000e+00]
 [ 1.22464680e-16  2.00000000e+00]
 [-1.50000000e+00  2.00000000e+00]
 [-1.50000000e+00  9.18485099e-17]]
Determinant: 2.9999999999999996
```

**How and why the result changes:** With 90 degrees the matrix entries 1.22e-16 and 9.18e-17 are just round-off for 0, so the transformation is a quarter turn combined with the scaling: the corner (1, 0) goes to (0, 2) and (0, 1) goes to (−1.5, 0). The shape is a rectangle 1.5 wide and 2 high. The determinant stayed at 3.0 (printed as 2.9999999999999996 because of round-off) because a rotation does not change area; only the scale factors 2.0 x 1.5 = 3.0 do. So the angle changes where the points go, not how much area the shape covers.

## 4. Meaning of the output

The original points are the corners of a 1 x 1 square. The program scales the square by 2 in the x direction and 1.5 in the y direction, then rotates it by 45 degrees, using one combined matrix. The transformed points show the new corners, for example (1, 0) moves to (1.414, 1.414) and (0, 1) moves to (−1.061, 1.061). The determinant is 3, which is the factor by which the area of the shape increases (2 x 1.5 = 3, since rotation does not change area). One matrix multiplication moved all four points consistently, which is how graphics programs transform whole objects.

## 5. Related real-world case

- **Scenario:** Position of the elbow and the tip of a two-link robot arm (link 1 = 3 m, link 2 = 2 m) with the shoulder at 40 degrees and the elbow bent by 0, 30, 60 and 90 degrees.
- **Assumptions:**
  - The arm moves in a flat 2-D plane with its base at the origin
  - Angles are measured anticlockwise from the x-axis, and the elbow angle is relative to link 1
  - The links are rigid
- **Input data:** L1 = 3.0, L2 = 2.0, theta1 = 40, theta2 in [0, 30, 60, 90].
- **Modified program:** [`code/Task_05_matrix_algebra_case.py`](../code/Task_05_matrix_algebra_case.py)

**Output:**

```text
theta2= 0 deg: elbow=[2.298 1.928], tip=[3.83  3.214], reach=5.000 m
theta2=30 deg: elbow=[2.298 1.928], tip=[2.982 3.808], reach=4.837 m
theta2=60 deg: elbow=[2.298 1.928], tip=[1.951 3.898], reach=4.359 m
theta2=90 deg: elbow=[2.298 1.928], tip=[1.013 3.46 ], reach=3.606 m
```

**Interpretation:** The elbow stays at (2.298, 1.928) because only the shoulder angle moves it. The tip position changes with the elbow angle. With the arm straight (theta2 = 0) the tip is 5.000 m from the base, the maximum reach 3 + 2. As the elbow bends, the reach shrinks to 4.837 m, 4.359 m and 3.606 m at 90 degrees. Rotation matrices let a program find where the end of the arm is for any joint angles, which is the basis of robot control.

# Task 9: Eigenvalues and Eigenvectors

**Program file:** [`code/Task_09_eigenvalues.py`](../code/Task_09_eigenvalues.py)

**Mathematical concept:** An eigenvector keeps its direction under a matrix A and is only scaled by the eigenvalue: Av = lambda v.

## 1. Inputs and mathematical operation

**Inputs**

- `A`: adjacency matrix of a 4-node network (A, B, C, D)

**Mathematical operation**

- Compute eigenvalues and eigenvectors with `np.linalg.eig`
- Take the dominant eigenvalue and its eigenvector, normalise it to sum to 1
- Verify Av = lambda v

## 2. Baseline output

```text
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```

## 3. Change an input or parameter

**What I changed:** Added a road/link between nodes A and D by changing the first row to `[0., 1., 1., 1.]` and the last row to `[1., 1., 1., 0.]`.

| Parameter changed | Original value | New value | Result |
|---|---|---|---|
| Links | no A–D link | A–D link added | Dominant eigenvalue 2.5616 → 3.0; importance of A, B, C, D from 0.219, 0.281, 0.281, 0.219 → all 0.25 |

New output (add link A-D):

```text
Dominant eigenvalue: 3.0
Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500
Verification error: 2.220446049250313e-16
```

**How and why the result changes:** Adding the A–D link connects every node to every other node (a complete network of four nodes), so no node is more central than another: all four importance scores become 0.25. The dominant eigenvalue rises from 2.56 to 3.0, which equals the number of connections of each node, and a larger dominant eigenvalue means the network is more densely connected. Before the link, B and C were more influential because they were connected to three nodes while A and D were connected to two.

## 4. Meaning of the output

The adjacency matrix shows which nodes are linked. The dominant eigenvalue is 2.5616 and its eigenvector, normalised to add up to 1, gives each node's importance: B and C score 0.2808 and A and D score 0.2192. B and C are more influential because each is connected to three nodes, including the other well-connected node. The tiny verification error (1.5e-15) shows that Av = λv is satisfied, so this really is an eigenvalue and eigenvector pair.

## 5. Related real-world case

- **Scenario:** Importance of five road junctions (A to E) in a small road network with roads A–B, B–C, B–D, C–D and D–E.
- **Assumptions:**
  - Roads are two-way and all roads count equally
  - A junction is important if it connects to many other important junctions
  - Only the layout is used (no traffic volume or road length)
- **Input data:** A 5 x 5 symmetric adjacency matrix for the five junctions.
- **Modified program:** [`code/Task_09_eigenvalues_case.py`](../code/Task_09_eigenvalues_case.py)

**Output:**

```text
Dominant eigenvalue: 2.3028
Eigenvector-based importance of each junction:
D: 0.2676
B: 0.2676
C: 0.2324
E: 0.1162
A: 0.1162
Verification error: 1.2262814116578437e-15
```

**Interpretation:** The dominant eigenvalue is 2.3028. Junctions B and D are the most important (0.2676 each) because each has three roads, C comes next (0.2324) because it joins B and D, and A and E are the least important (0.1162 each) because they are dead ends joined to only one junction. If the council wants to place a traffic signal or relieve congestion, B and D are the first junctions to examine, since a problem at either one would disturb the most routes.

# Task 9 (related case): Importance of road junctions in a small road network
import numpy as np

# Junction order: A, B, C, D, E
# Roads: A-B, B-C, B-D, C-D, D-E
A = np.array([
    [0., 1., 0., 0., 0.],
    [1., 0., 1., 1., 0.],
    [0., 1., 0., 1., 0.],
    [0., 1., 1., 0., 1.],
    [0., 0., 0., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
importance = dominant_vector / dominant_vector.sum()

junctions = ["A", "B", "C", "D", "E"]
print("Dominant eigenvalue:", round(dominant_value, 4))
print("Eigenvector-based importance of each junction:")
for name, score in sorted(zip(junctions, importance), key=lambda p: -p[1]):
    print(f"{name}: {score:.4f}")

v = np.real(eigenvectors[:, index])
print("Verification error:", np.linalg.norm(A @ v - dominant_value * v))

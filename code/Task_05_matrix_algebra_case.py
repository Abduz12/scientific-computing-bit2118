# Task 5 (related case): Position of a two-link robot arm using rotation matrices
import numpy as np

def rotation(degrees):
    a = np.deg2rad(degrees)
    return np.array([
        [np.cos(a), -np.sin(a)],
        [np.sin(a),  np.cos(a)]
    ])

L1, L2 = 3.0, 2.0                 # link lengths in metres
link1 = np.array([L1, 0.0])       # link vectors before rotation
link2 = np.array([L2, 0.0])

theta1 = 40.0                     # shoulder angle (degrees)
for theta2 in [0, 30, 60, 90]:    # elbow angle relative to link 1
    elbow = rotation(theta1) @ link1
    tip = elbow + rotation(theta1 + theta2) @ link2
    reach = np.linalg.norm(tip)
    print(f"theta2={theta2:2d} deg: elbow={np.round(elbow, 3)}, "
          f"tip={np.round(tip, 3)}, reach={reach:.3f} m")

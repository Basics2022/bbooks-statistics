
import numpy as np

v = np.array([0., 1., -.2, 3., -1])

isort = np.argsort(v)
vsort = v[isort]

print(f"isort: {isort}")
print(f"vsort: {vsort}")


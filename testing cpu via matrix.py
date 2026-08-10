import numpy as np

# Set line width to infinity to stop wrapping
np.set_printoptions(linewidth=np.inf)

a = np.random.randint(1000, 10000, size=(30, 10))
b = np.random.randint(1000, 10000, size=(10, 30))
res = np.dot(a, b)

print("Matrix A:\n", a)
print("\nMatrix B:\n", b)
print("Final Result Matrix:\n", res)

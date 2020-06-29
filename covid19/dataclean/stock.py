import numpy as np

x = np.array([1, 2, 3, 4])
x1 = x.reshape(-1,1)
print(x1)
n1 = np.linalg.norm(x)
n2 = np.sqrt(np.dot(x1.T, x1))
print(n1, n2)

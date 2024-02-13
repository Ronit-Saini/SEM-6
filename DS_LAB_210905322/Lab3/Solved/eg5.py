import numpy as np

d = np.array([[1, 2], [4, 5]])
e = np.array([[1, 2], [4, 5]])
print(d - e)
print(d**2)
print(10 * np.sin(d))
print(e < 3)
print()
f = np.array([[1, 2], [4, 5]])
g = np.array([[1, 2], [4, 5]])
print(f)
print(f*g)
print(f.dot(g))
print(f.sum(axis=0))

print()

h = np.array([[1, 2], [4, 5]])
print(h[1:2])
print(h[1][0])
print(h[0:1:2])
print(h[0:-1])

print()
b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))
print(b.sum(axis=1))
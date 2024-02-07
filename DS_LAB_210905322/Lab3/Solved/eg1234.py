import numpy as np

A = np.array([1,23,4])
print(A)

a = np.array([[1, 2], [4, 5]])
print(a.dtype)


print("")

print(np.zeros((2, 4)))

print("")

print(np.ones((2, 4),dtype="int"))

print("")

print(np.arange(10, 30, 5))
print("")
print(np.arange(2,4,0.2))


print("")

print(np.linspace(0, 2, 9))
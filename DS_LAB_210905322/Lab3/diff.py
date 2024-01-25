import numpy as np

lst = np.array([[1, 22, 3], [41, 5, 6], [7, 8, 29]])

print(lst)

print("\nMAX : \n", lst.max())
print(lst.max(axis=0))
print(lst.max(axis=1))

print("\nMIN : \n", lst.min())
print(lst.min(axis=0))
print(lst.min(axis=1))

print("\nSUM : \n", lst.sum())
print(lst.sum(axis=0))
print(lst.sum(axis=1))

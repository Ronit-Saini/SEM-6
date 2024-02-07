import numpy as np

k = np.array([[1, 2], [4, 5]])
sum = 0
print(k.shape[0])
print("for i in range === >")

for i in range(k.shape[0]):
    for j in range(k.shape[0]):
        sum += k[i, j]
print(sum)


#ORRRRRRRRR


print()
print()

print("for i in array === >")

k = np.array([[1, 2], [4, 5]])
sum = 0

for i in k:
    for j in i:
        sum += j
print(sum)



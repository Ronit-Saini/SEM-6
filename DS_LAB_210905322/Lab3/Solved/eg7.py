import numpy as np

a = np.arange(12)**2
print(a)
i = np.array( [ 1,1,3,8,5 ] )
print(a[i])

# the first 12 square numbers
# an array of indices
# the elements of a at the positions i
j = np.array( [ [ 3, 4], [ 9, 7 ] ] ) # a bidimensional array of indices
print(a[j])
# the same shape as j

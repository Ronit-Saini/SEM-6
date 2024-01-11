num = [11,-21,0,45,66,-93]
neg = 0
pos = 0
for i in num:
    if i<0:
        neg = neg + 1
    elif i>0:
        pos = pos + 1
print("Negative = ",neg," Positive = ",pos)
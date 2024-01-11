num = [1,2,3,4]
for i in num:
    if i in num:
        if i%2 == 0:
            num.remove(i)
print(num)
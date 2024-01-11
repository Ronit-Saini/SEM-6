tup = [12,7,38,56,78]
new = ()
for i in tup:
    if i%2==0:
        new = new + (i,)
print(new)

def binarysearch(num,a,b,x):
	if(b>=a):
		c = int((a+b)//2)
		if num[c]==x:
			return c
		elif num[c]>x:
			binarysearch(num,a,c,x)
		elif num[c]<x:
			binarysearch(num,c,b,x)
	else:
		return -1

num = [1,2,3,4,5,6,7,8,9]
hi = binarysearch(num,0,len(num),66)
print(hi)
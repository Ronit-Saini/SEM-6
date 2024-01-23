a = int(input("Enter number A : "))
b = int(input("Enter number B : "))
c = input("Enter +,-,* or / : ")
if(c=='+'):
	result = a + b
elif(c=='-'):
	result = a - b
elif(c=='*'):
	result = a*b
elif(c=='/'):
	result = a/b
else:
	print("Inavlid character !!! ")

print("Result is "+str(result))
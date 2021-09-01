# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 


import math
def pow(n,r=0):
	j=3**r
	i=[]
	if(n<r):
		return i
	if j<=n:
		return [j]+pow(n,r+1)
	else:
		return i	

def recursion_powersof3ton(n):
	# your code goes here
	if(n<=0):
		return None
	elif(n==1):
		return [int(n)]
	elif(n>=1):
		return pow(n,r=0)		



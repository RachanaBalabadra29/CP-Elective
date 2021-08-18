# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

import math
def largestperfectsquare(n):
	# your code goes here
	# d=math.sqrt(n)
	# if(n==d*d):
	# 	return 
	# elif()
	d=int(math.sqrt(n))
	f=(d*d)
	if(n==f):
		return n
	else:
		i=1
		h=[]
		while(i<int(d+1)):
			g=i*i
			h.append(g)
			i+=1
		if(n>h[-1]):
			return h[-1]
		elif(n<h[-1]):
			return h[-2]

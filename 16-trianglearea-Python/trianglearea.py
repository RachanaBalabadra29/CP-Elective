# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.

import math
def trianglearea(s1, s2, s3):
	# your code goes here
	a=float(s1)
	b=float(s2)
	c=float(s3)
	s=(a+b+c)/2.0
	a=math.sqrt(s*(s-a)*(s-b)*(s-c))
	return a

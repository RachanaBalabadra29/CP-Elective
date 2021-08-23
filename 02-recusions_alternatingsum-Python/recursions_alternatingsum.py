# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

# [1,2,3,4,5]
# sum([1,2,3,4,5]) = 1 + sum([2,3,4,5])
#				   = 1 - 2 + sum([3,4,5])

def fun_recursions_alternatingsum(l): 
	x = True
	return fun1(l, x)

def fun1(l, x):
	if len(l)==0:
		return 0
	if x==True:
		x = False
		return l[0] + fun1(l[1:], x)
	else:
		x = True
		return (-1*l[0]) + fun1(l[1:], x)

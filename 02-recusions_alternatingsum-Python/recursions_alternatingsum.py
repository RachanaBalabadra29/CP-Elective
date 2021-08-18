# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l): 
	if(len(l)==0):
		return 0
	add=0
	sub=0
	for i in range(len(l)):
		if(i%2==0):
			add+=l[i]
		else:
			sub+=l[i]
	c=add-sub
	return c

# Write the function isrectangular(L) that takes a possibly-2d 
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.



#([[1, 2, 3], [1, 1]], False), ([[1, 2, 3], [1, 1, 2]], True),
#([[], []], True), ([[1, 2], [1, 1], [1, 2, 3]], False)

def fun_isrectangular(l):
	# Your code goes here...
	c=0
	if(len(l)==0):
		return True
	p=[]
	for i in range(len(l)):
		c=len(l[i])
		p.append(c)
	 
	 
	s=[]   
	for i in p:
	    if i not in s:
	        s.append(i)
	if(len(s)==1):
	     return True
	else:
	     return False




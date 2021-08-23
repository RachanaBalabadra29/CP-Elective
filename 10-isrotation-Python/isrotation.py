# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.


def rotate(m):  #1234 #2341
	m=str(m)
	return m[1:]+m[0]
	

def isrotation(x, y):
	# Your code goes here
	y=str(y)
	x=str(x)
	if(x[::-1]==y):
		return True
	for i in range(len(x)):
		if(rotate(x)==y):
			return True
		x=rotate(x)
	return False

	
# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	# your code goes here
	# b=type(x)
	# if(x==None):
	# 	return False
	# elif(x<=0):
	# 	return False
	# elif(b!=int):
	# 	return False
	# a=x%2
	# if(a==0):
	#  	return True
	# elif((x%2==0) and x>0):
	# 	return True
	
	
	# elif(x==int or x==str or x==list):
	# 	return False
	if(type(x)==int) and x>0 and x%2==0:
		return True
	else:
		return False
	

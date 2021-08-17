# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.


# (-24, False),
# 	(0, False),
# 	(26011, True),
# 	(14, False),
# 	(2, False),
# 	(5, False),
# 	(5231123123123, True),
# 	(-5231123123123, True),
# 	(-11023, True),
# ])
def hasconsecutivedigits(n):
	# your code goes here
	n=abs(n)
	if(n==0):
		return False
	n=str(n)
	if(len(n)==1):
		return False
	p=[]
	for i in n:
		p.append(i)
	x=1
	for i in p:
		s=p.count(i)
		if(s>x):
			x=s
	if(x>1):
		return True
	else:
		return False
		
